from celery import shared_task
from .services.amazon_scraper import AmazonScraper
# from scraper.models import Product


@shared_task
def scrape_product(platform, product_id):
    if platform == "amazon":
        amazon_scraper = AmazonScraper()
        result = amazon_scraper.fetch_product(product_id)
    # elif platform == "flipkart":
    #     result = scrape_flipkart(url)
    else:
        result = {"error": f"Unsupported platform: {platform}"}

    # if "title" in result and result["title"]:
    #     Product.objects.create(
    #         platform=platform,
    #         url=url,
    #         title=result["title"],
    #         price=result.get("price"),
    #     )

    return result
