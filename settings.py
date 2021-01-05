from middleware import demo
from views import create_course, create_category, category_list, course_list, StudentListView, StudentCreateView, \
    AddStudentByCourseCreateView

urls = {
    '/create_course/': create_course,
    '/create_category/': create_category,
    '/category_list/': category_list,
    '/course_list/': course_list,
    '/student_list/': StudentListView(),
    '/create_student/': StudentCreateView(),
    '/add_student/': AddStudentByCourseCreateView(),
}

middleware = [
    demo
]
