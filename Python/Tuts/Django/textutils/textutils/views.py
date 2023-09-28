# this pythone file is created by arya
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Arya')
def about(request):
    return HttpResponse('About Arya')