from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient
import time

def synchronous_fetch(url):
    http_client = HTTPClient()
    t1 = time.time()
    response = http_client.fetch(url)
    print time.time() - t1
    return response.body

def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()
    t1 = time.time()
    def handle_response(response):
        print time.time() - t1
    print 'here'
    http_client.fetch(url, callback=handle_response)
    time.sleep(6)
