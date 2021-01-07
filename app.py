from framework.templates import render_from_file
from framework.uow import UnitOfWork
from framework.utils import parse_body_json
from mappers import MapperRegistry
from settings import urls, middleware
from framework.application import Application, MockApplication, DebugApplication

app = Application(urls, middleware)

UnitOfWork.new_current()
UnitOfWork.get_current().set_mapper_registry(MapperRegistry)


# app = DebugApplication(urls, middleware)


# app = MockApplication(urls, middleware)


@app.add_route('/')
def index(request):
    page = render_from_file('index.html', request)
    return '200 OK', page


@app.add_route('/contacts/')
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
