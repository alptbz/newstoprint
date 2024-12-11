import requests


def get_news(url):
    response = requests.get(url)
    return response.json()
