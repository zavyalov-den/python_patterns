from framework.templates import render_from_file
from framework.utils import parse_query_string, parse_body_json


def index(request):
    page = render_from_file('index.html', request)
    return '200 OK', page


def contacts(request):
    if request['METHOD'] == 'GET':
        page = render_from_file('contacts.html', request)
        return '200 OK', page
   
    if request['METHOD'] == 'POST':
        body = parse_body_json(request)
        print(body)
        if body['topic'] and body['msg'] and body['email']:
            print(f'User with email {body["email"]} had sent a message. Topic {body["topic"]}: \n {body["msg"]}')

        page = render_from_file('contacts.html', request)
        return '200 OK', page


def not_found(request):
    page = render_from_file('404.html', request)
    return '404 NOT FOUND', page
