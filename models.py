from copy import deepcopy
from abc import ABC, abstractmethod


# prototype pattern
class ProtoMixin:
    def copy(self):
        return deepcopy(self)


# singleton
class NamedSingleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        name = args[0] if args else kwargs['name']

        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class AbstractUser(ABC):
    @staticmethod
    def login(username, password):
        pass

    @staticmethod
    def logout(username):
        pass


class Student(AbstractUser):
    pass


class Teacher(AbstractUser):
    pass


class UserFactory:
    _types = {
        'teacher': Teacher,
        'student': Student,
    }

    @classmethod
    def create(cls, type: str):
        return cls._types[type.lower()]()


class Course(ProtoMixin):
    def __init__(self, name, category):
        self.category = category
        self.name = name
        self.category.courses.append(self)


class Category(ProtoMixin):
    _last_id = 0

    def _generate_id(self):
        self._last_id += 1
        return self._last_id

    def __init__(self, name, category):
        self.id = self._generate_id()
        self.name = name
        self.category = category
        self.courses = []

    def count_courses(self):
        res = len(self.courses)
        return res + self.category.course_count() if self.category else res


class OnlineCourse(Course):
    pass


class VodCoursre(Course):
    pass


class InteractiveCourse(Course):
    pass


class CourseFactory:
    _types = {
        'online': OnlineCourse,
        'vod': VodCoursre,
        'interactive': InteractiveCourse,
    }

    @classmethod
    def create(cls, type: str, name, category):
        return cls._types[type.lower()](name, category)


class TrainingApp:
    teachers = []
    students = []
    courses = []
    categories = []

    def create_user(self, type):
        UserFactory.create(type)

    def create_category(self, name, category=None):
        cat = Category(name, category)
        self.categories.append(cat)
        return cat

    def get_category_by_id(self, id):
        for c in self.categories:
            if c.id == id:
                return c
        raise Exception('Category does not exist.')

    def create_course(self, type, name, category):
        # course = Course(name, category)
        course = CourseFactory.create(type, name, category)
        self.courses.append(course)
        return course

    def get_course_by_id(self, id):
        for c in self.courses:
            if c.id == id:
                return c
        raise Exception('Course does not exist.')

    def get_course_by_name(self, name):
        for c in self.courses:
            if c.name == name:
                return c
        raise Exception('Course does not exist.')
