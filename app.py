from framework.application import Application
from settings import urls, middleware

app = Application(urls, middleware)
