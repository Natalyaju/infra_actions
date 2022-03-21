from django.http import HttpResponse


def index(request, Exception=None):
    return HttpResponse('У меня получилось!', status=200)


def second_page(request, Exception=None):
    return HttpResponse('А это вторая страница', status=200)
