from requests import get
from requests import post


def basic_get(uri, debug=False):
    if debug:
        print "Sending basic HTTP GET request to %s" % uri
    return get(uri)


def basic_post(uri, headers=None, body=None, debug=False):
    if debug:
        print "Sending basic HTTP POST request to %s" % uri
    return post(uri, headers=headers, data=body)
