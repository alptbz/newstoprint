import requests

_endpoint_url = ""


def init(endpoint_url):
    global _endpoint_url
    _endpoint_url = endpoint_url


def send_data(timestamp, content):
    requests.post(_endpoint_url, json={"timestamp": timestamp, "content": content})

