from middleware import demo
from views import index, contacts

urls = {
    '/': index,
    '/contacts/': contacts
}

middleware = [
    demo
]
