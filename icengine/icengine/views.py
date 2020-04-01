from django.http import HttpResponse


def hello(request):
    print('\nREQUEST:\n', request, '\n')
    print('\nREQUEST DIR:\n', dir(request), '\n')
    return HttpResponse('<h1>Hello, empty world!</h1>')
