from framework.utils import url_check
from settings import urls, middleware
from views import not_found
from pprint import pprint


class Application:
    def __init__(self, urls, middleware):
        self.urls = urls
        self.middleware = middleware

    def __call__(self, environ, start_response):
        pprint(environ)

        request = self.request_init(environ)
        if request['PATH'] in self.urls:
            for item in middleware:
                item(request)
            code, page = urls[request['PATH']](request)
        else:
            code, page = not_found(request)

        print("request: ")
        pprint(request)

        start_response(code, [('Content-Type', 'text/html')])
        return [page.encode(encoding='utf-8')]

    def request_init(self, env, request=None):
        if request is None:
            request = {}

        request['PATH'] = url_check(env['PATH_INFO'])
        request['ARGS'] = env['QUERY_STRING']
        request['METHOD'] = env['REQUEST_METHOD']
        request['DATA'] = self.data_to_dict(env['wsgi.input'].read().decode(encoding='utf=8'))
        return request

    def data_to_dict(self, data):
        print('raw data: \n', data)
        res = {}
        try:
            arr = data.split('&')
            for item in arr:
                key, value = item.split('=')
                res[key] = value
        except:
            res = {}

        return res
