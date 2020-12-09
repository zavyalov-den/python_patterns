from framework.templates import render_from_file


def index(request):
    page = render_from_file('index.html', request)
    return '200 OK', page


def contacts(request):
    page = render_from_file('contacts.html', request)
    return '200 OK', page


def not_found(request):
    page = render_from_file('404.html', request)
    return '404 NOT FOUND', page
