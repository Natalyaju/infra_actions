from django.http import HttpResponse


def index(request, exception=None):
    return HttpResponse('У меня получилось!', status=200)


def second_page(request, exception=None):
    return HttpResponse('А это вторая страница!', status=200)
