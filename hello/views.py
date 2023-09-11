from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hell, so fast</h1>')
    return render(request, 'hello/index.html')

def greet(request, name):
    # return HttpResponse(f'<h1>Hell, {name.title()}!</h1>')
    hour = timezone.localtime().hour
    return render(request, 'hello/greet.html', {
        'name': name.title(),
        'time': hour
        })
