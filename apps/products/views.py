import csv
import io

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Total products
        context['total_products'] = Product.objects.count()

        # Total platforms tracked
        context['platforms_tracked'] = Platform.objects.count()

        # Products added in last 7 days (recent)
        last_week = now() - timedelta(days=7)
        context['recent_products'] = Product.objects.filter(created_at__gte=last_week).count()

        return context


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
