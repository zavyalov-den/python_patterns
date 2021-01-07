from debug import debug
from framework.cbv import ListView, CreateView
from framework.templates import render_from_file
from framework.utils import parse_query_string, parse_body_json
from mappers import MapperRegistry, UnitOfWork
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


class StudentListView(ListView):
    # queryset = courses_app.students
    template_name = 'student_list.html'

    def get_queryset(self):
        mapper = MapperRegistry.get_current_mapper('student')
        return mapper.all()


class StudentCreateView(CreateView):
    template_name = 'student_create.html'

    def create_obj(self, data: dict):
        name = data['name']
        obj = courses_app.create_user('student', name)
        # courses_app.students.append(obj)

        obj.mark_new()
        UnitOfWork.get_current().commit()


class AddStudentByCourseCreateView(CreateView):
    template_name = 'student_add.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['courses'] = courses_app.courses
        context['students'] = courses_app.students
        return context

    def create_obj(self, data: dict):
        course_name = data['course_name']
        course = courses_app.get_course_by_name(course_name)
        student_name = data['student_name']
        student = courses_app.get_student_by_name(student_name)
        course.add_student(student)
