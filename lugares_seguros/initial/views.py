from django.http import HttpResponse

def index(request):
    return HttpResponse('Lo estoy logrando jiji')