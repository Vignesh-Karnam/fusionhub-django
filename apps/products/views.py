import csv
import io
from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.timezone import now, timedelta
from django.views.decorators.http import require_POST
from django.views.generic import ListView, TemplateView

from .models import Platform, Product


class ProductsView(LoginRequiredMixin, ListView):
    template_name = 'products/products.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_products'] = Product.objects.count()
        context['platforms_tracked'] = Platform.objects.count()
        last_week = now() - timedelta(days=7)
        context['recent_products'] = Product.objects.filter(created_at__gte=last_week).count()

        # pagination info
        page_obj = context.get('page_obj')
        if page_obj:
            context['current_page'] = page_obj.number
            context['total_pages'] = page_obj.paginator.num_pages

        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request'):
            return render(
                self.request,
                'products/partials/product_rows.html',
                context,
                **response_kwargs
            )
        return super().render_to_response(context, **response_kwargs)


@login_required
@require_POST
def upload_products(request):
    file = request.FILES.get("file")
    if not file:
        return JsonResponse({"error": "No file uploaded"}, status=400)

    # Decode file content
    try:
        decoded_file = file.read().decode("utf-8")
    except UnicodeDecodeError:
        file.seek(0)  # Reset file pointer
        decoded_file = file.read().decode("cp1252")
    io_string = io.StringIO(decoded_file)
    reader = csv.DictReader(io_string)

    new_products = []
    for row in reader:
        try:
            platform = Platform.objects.get(name=row.get("platform"))
        except Platform.DoesNotExist:
            continue

        product = Product.objects.create(
            user=request.user,
            platform=platform,
            product_id=row.get("product_id"),
            title=row.get("title") or None,
            url=row.get("url"),
            brand=row.get("brand") or None,
            created_at=now(),
        )
        new_products.append(product)

    # Render only the table rows (for HTMX swap)
    return render(request, "products/partials/product_rows.html", {"products": new_products})
