from celery import shared_task
from django.utils.timezone import now
from ..products.models import Product, ProductSnapshot
from .services.amazon_scraper import AmazonScraper


@shared_task
def scrape_all_amazon_products():
    """
    Scrape all Amazon products and update details + snapshots.
    """
    scraper = AmazonScraper()
    products = Product.objects.filter(platform__name__iexact="amazon")
    snapshots = []
    to_update = []

    for product in products:
        result = scraper.fetch_product(product.product_id)
        if not result or "error" in result:
            continue

        product.title = result.get("title") or product.title
        product.brand = result.get("brand") or product.brand
        product.category = result.get("category") or product.category
        product.price = result.get("selling_price") or product.price
        product.currency = result.get("currency") or "INR"
        product.url = result.get("url") or product.url

        to_update.append(product)

        snapshots.append(
            ProductSnapshot(
                product=product,
                price=result.get("selling_price"),
                currency=result.get("currency") or "INR",
                rating=result.get("rating"),
                review_count=result.get("review_count"),
                availability=result.get("availability", True),
                created_at=now(),
            )
        )

    if to_update:
        Product.objects.bulk_update(
            to_update,
            ["title", "brand", "category", "price", "currency", "url"],
        )

    if snapshots:
        ProductSnapshot.objects.bulk_create(snapshots)

    return f"Scraped {len(to_update)} Amazon products, saved {len(snapshots)} snapshots"
