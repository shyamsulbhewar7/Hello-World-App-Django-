#i have created this file - shyam
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello World :)<h1>")
def about(request):
    return HttpResponse("Contact : @shyamsulbhewar")