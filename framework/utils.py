import json


def parse_query_string(request: dict, body=False) -> dict:
    args = request['ARGS']
    if body:
        args = request['BODY']
    param_dict = {}

    for x in args.split('&'):
        key, value = x.split('=')
        param_dict[key] = value

    return param_dict


def parse_body_json(request) -> dict:
    try:
        return json.loads(request['BODY'])
    except:
        return parse_query_string(request, body=True)


def url_check(url: str):
    return url if url[-1] == '/' else url + '/'
