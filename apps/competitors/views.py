import csv
import io

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.timezone import now
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from ..core.models import Platform
from .models import Competitor
from ..products.models import Product


class CompetitorsView(LoginRequiredMixin, TemplateView):
    template_name = 'competitors/competitors.html'


@login_required
@require_POST
def upload_competitors(request):
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

    new_competitors = []
    for row in reader:
        try:
            platform = Platform.objects.get(name=row.get("platform"))
        except Platform.DoesNotExist:
            continue
        try:
            product = Product.objects.get(product_id=row.get("product_id"))
        except Product.DoesNotExist:
            continue

        competitor = Competitor.objects.create(
            product=product,
            platform=platform,
            competitor_id=row.get("competitor_id"),
            title=row.get("title") or None,
            url=row.get("url"),
            brand=row.get("brand") or None,
            last_price=row.get("last_price") or None,
            added_by_user=True,
            confirmed=True,
        )
        new_competitors.append(competitor)
    return render(request, "competitors/partials/competitor_rows.html", {"competitors": new_competitors})
