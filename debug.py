from models import NamedSingleton
import time


# Заметка, можно применить стратегию если добавить стратегию логирования
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
