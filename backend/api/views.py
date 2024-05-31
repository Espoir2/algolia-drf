import json
from django.http import JsonResponse
# Create your views here.

def object_viewer(theObject):
    requestParams = dir(theObject)
    print(requestParams)
    with open('request_view.txt', 'a') as f:
        for element in requestParams:
            value = getattr(theObject, element)
            print(element)
            print(value)
            print('*' * 30)
            f.write(element)
            f.write("\n")
            f.write(f"{value}\n")
            f.write("*****************\n\n")


def api_home(request, *args, **kwargs):
    # request --> HttpRequest --> Django
    # request.body
    body = request.body # byte string of JSON Data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
