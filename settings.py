from middleware import demo
from views import create_course, create_category, category_list, course_list

urls = {
    '/create_course/': create_course,
    '/create_category/': create_category,
    '/category_list/': category_list,
    '/course_list/': course_list,
}

middleware = [
    demo
]
