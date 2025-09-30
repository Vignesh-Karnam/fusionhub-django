from celery import shared_task
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
        if "error" in result:
            continue

        product.title = result.get("title")
        product.brand = result.get("brand")
        product.category = result.get("category")
        product.price = result.get("selling_price")
        product.currency = "INR"
        to_update.append(product)

        snapshots.append(ProductSnapshot(
            product=product,
            price=result.get("selling_price"),
            currency="INR",
            rating=result.get("rating"),
            review_count=result.get("review_count"),
            availability=result.get("availability", True),
        ))

    if to_update:
        Product.objects.bulk_update(
            to_update,
            ["title", "brand", "category", "price", "currency"]
        )

    if snapshots:
        ProductSnapshot.objects.bulk_create(snapshots)

    return f"Scraped {len(to_update)} Amazon products"
