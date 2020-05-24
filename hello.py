def app(environ, start_response):
    body = bytes(environ['QUERY_STRING'].replace('&', '\n'), 'utf-8')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [body]
