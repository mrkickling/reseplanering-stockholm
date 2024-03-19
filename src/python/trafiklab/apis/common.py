import requests


def make_request(url, method, **kwargs):
    """Send a request using method and kwargs"""
    print(url)
    return requests.request(method, url, **kwargs)
