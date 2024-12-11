import sys
import config
import services.news_service as news_service
import services.notifications_service as notifications_service
import services.translation_service as translation_service

if __name__ == '__main__':
    # Initialization
    notifications_service.init(config.enabled_notification_outputs, config.pos_printer_ip, config.webhook_site_endpoint_url)

    # Input: Get the news
    news = news_service.get_news(config.news_api_url)

    # Check input
    if not (news and "results" in news and len(news["results"]) > 0 and "summary" in news["results"][0]):
        print("No news found")
        sys.exit(1)

    # Process input
    first_news_summary_text = news["results"][0]["summary"]

    first_news_summary_text_translated = translation_service.translate(first_news_summary_text)

    # Output the news
    notifications_service.send_notifications(first_news_summary_text_translated)

    print("Done")

