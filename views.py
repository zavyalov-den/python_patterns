from debug import debug
from framework.templates import render_from_file
from framework.utils import parse_query_string, parse_body_json
from models import TrainingApp

courses_app = TrainingApp()


@debug
def category_list(request):
    if request['METHOD'] == 'GET':
        page = render_from_file('category_list.html', object_list=courses_app.categories)
        return '200 OK', page
    if request['METHOD'] == 'POST':
        pass


def course_list(request):
    if request['METHOD'] == 'GET':
        print('courses: ')
        print(courses_app.courses)
        page = render_from_file('course_list.html', object_list=courses_app.courses)
        return '200 OK', page
    if request['METHOD'] == 'POST':
        pass


def create_category(request):
    if request['METHOD'] == 'GET':
        page = render_from_file('create_category.html')
        return '200 OK', page
    if request['METHOD'] == 'POST':
        data = request['DATA']

        print(data)

        name = data['name']
        category_id = data.get('category_id')

        category = None
        if category_id:
            category = courses_app.get_category_by_id(int(category_id))

        courses_app.create_category(name, category)

        # courses_app.categories.append(new_category)

        # редирект?
        # return '302 Moved Temporarily', render('create_course.html')
        # Для начала можно без него
        return '200 OK', render_from_file('create_category.html')


def create_course(request):
    if request['METHOD'] == 'GET':
        page = render_from_file('create_course.html', categories=courses_app.categories)
        return '200 OK', page
    if request['METHOD'] == 'POST':
        data = request['DATA']

        print(data)

        name = data['name']
        category_id = data.get('category_id')
        print(category_id)
        category = None
        if category_id:
            category = courses_app.get_category_by_id(int(category_id))

        courses_app.create_course('online', name, category)
        print(courses_app.courses)

        # редирект?
        # return '302 Moved Temporarily', render('create_course.html')
        # Для начала можно без него
        return '200 OK', render_from_file('create_course.html')


def not_found(request):
    page = render_from_file('404.html', request)
    return '404 NOT FOUND', page
