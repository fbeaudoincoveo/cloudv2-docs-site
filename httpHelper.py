from requests import get
from requests import post


def basic_get(uri):
    return get(uri)


def basic_post(uri, headers=None, body=None):
    return post(uri, headers, body)
