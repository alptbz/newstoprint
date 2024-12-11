from datetime import datetime

import services.posprinter_service as posprinter
import services.webhook_site_service as webhook_site_service

_config = {}

def init(config, printer_address, webhook_site_endpoint_url):
    global _config
    _config = config
    posprinter.init(printer_address)
    webhook_site_service.init(webhook_site_endpoint_url)


def send_notifications(content):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if "pos_printer" in _config and _config["pos_printer"]:
        posprinter.print_pos([timestamp, content])
    if "webhook_site" in _config and _config["webhook_site"]:
        webhook_site_service.send_data(timestamp, content)