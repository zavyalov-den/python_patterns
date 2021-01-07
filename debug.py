from models import NamedSingleton
import time


class ConsoleWriter:
    def write(self, text):
        print(text)


class FileWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, text):
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(f'{text}\n')


class NamedLogger(metaclass=NamedSingleton):
    def __init__(self, name):
        self.name = name

    def log(self, text):
        print('log--->', text)


# debugging deco
def debug(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        finish = time.time()
        print('debug: ', func.__name__, finish - start, 'ms')
        return res

    return inner
