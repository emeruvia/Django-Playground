from django.shortcuts import render
from django.http import HttpResponse

# Views are request handlers. Request -> Response

def say_hello(request):
    return render(request, 'hello.html', { 'name': 'Duka'})
