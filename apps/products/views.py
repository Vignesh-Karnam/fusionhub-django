import csv
import io

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.timezone import now
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from .models import Product, Platform


class ProductsView(LoginRequiredMixin, TemplateView):
    template_name = 'products/products.html'


@login_required
@require_POST
def upload_products(request):
    file = request.FILES.get("file")
    if not file:
        return JsonResponse({"error": "No file uploaded"}, status=400)

    # Decode file content
    decoded_file = file.read().decode("utf-8")
    io_string = io.StringIO(decoded_file)
    reader = csv.DictReader(io_string)

    new_products = []
    for row in reader:
        try:
            platform = Platform.objects.get(id=row.get("platform_id"))
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
    return render(request, "products/product_rows.html", {"products": new_products})
