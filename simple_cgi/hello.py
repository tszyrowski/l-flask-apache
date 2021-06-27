""" Example of simple CGI (Common Gateway Interface) in python

ref:
https://docs.python.org/3/library/cgi.html

"""

try:
    from cgi import parse_qs, escape
except ImportError:
    from urllib.parse import parse_qs
    from html import escape

def hello_world(environ, start_response):
    """WSGI application saying Hello <worlded>"""
    parameters = parse_qs(environ.get("QUERRY_STRING", ""))
    print(f"parameters: {parameters}")
    if "subject" in parameters:
        subject = escape(parameters["subject"][0])
    else:
        subject = "worldek"
    start_response("200 OK", [("Content-Type", "text/html")])
    return [f"Hello -  :)  -  {subject}".encode()]

if __name__ == "__main__":
    host = "192.168.1.122"
    port = 8091
    from wsgiref.simple_server import make_server
    srv = make_server(host, port, hello_world)
    print(f"Serving on {host}:{port}")
    srv.serve_forever()