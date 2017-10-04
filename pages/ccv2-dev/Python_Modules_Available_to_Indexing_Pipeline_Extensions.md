---
layout: content-2-panel
title: Python Modules Available to Indexing Pipeline Extensions
categories: migrated
---

# Python Modules Available to Indexing Pipeline Extensions

An indexing pipeline extension Python script runs in a separate non-persistent isolated OS instance for each source item going through the Coveo Cloud V2 indexing pipeline.

The OS instance comes with Python 2.7.x.  In your indexing pipeline extension Python script, you can import to use the following modules:

-   Modules from the standard Python library (see  [The Python Standard Library](https://docs.python.org/2.7/library/)) 
-   `requests` - HTTP library for Python (see [Requests: HTTP for Humans](http://docs.python-requests.org/en/master/))
-   `boto3` - Amazon Web Services (AWS) SDK for Python (see [Boto 3 Documentation](https://boto3.readthedocs.io/en/latest/))
-   `pymongo` - Python driver for MongoDB(see [pymongo 2.7.2](https://pypi.python.org/pypi/pymongo/2.7.2))
-   `msgpack-python` - MessagePack (de)serializer (see [msgpack-python 0.4.8](https://pypi.python.org/pypi/msgpack-python/))
-   `pytz` - World timezone definitions, modern and historical (see [pytz 2016.10](https://pypi.python.org/pypi/pytz/))
-   `redis` - The Python interface to the Redis key-value store (see redis 2.10.5).

 

Note:

> If you would like to use a Python module that is not currently supported, contact [Coveo Support](https://coveocommunity.force.com/) to suggest the addition of the module to the OS instance.


