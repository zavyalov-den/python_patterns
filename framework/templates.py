import os

from jinja2 import Template, Environment, FileSystemLoader


def render_from_file(filename, request={}, path='templates/', *args, **kwargs):
    full_path = os.path.join(path, filename)
    with open(full_path) as f:
        contents = f.read()

    # template = Template(contents)
    template = Environment(loader=FileSystemLoader('templates/')).from_string(contents)
    return template.render(request, **kwargs)
