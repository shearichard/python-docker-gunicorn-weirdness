'''
Adapted from https://github.com/benoitc/gunicorn/blob/master/examples/test.py
'''

from gunicorn import __version__


def app(environ, start_response):
    """Simplest possible application object"""
    data = b'Hello, World!\nThis is being used as a test of how pip install behaves in some circumstances\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])

