from settings import urls, middleware
from views import not_found


class Application:
    def __init__(self, urls, middleware):
        self.urls = urls
        self.middleware = middleware

    def __call__(self, environ, start_response):
        # pprint(environ)

        request = {}
        path = self.url_check(environ['PATH_INFO'])
        if path in self.urls:
            code, page = urls[path](request)

            for item in middleware:
                item(request)

        else:
            code, page = not_found(request)

        start_response(code, [('Content-Type', 'text/html')])
        return [page.encode(encoding='utf-8')]

    @staticmethod
    def url_check(url: str):
        return url if url[-1] == '/' else url + '/'
