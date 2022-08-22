from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # return HttpResponse("hello to world")
    return render(request, 'home.html')


def add(request):
    val1 = request.GET['num1']
    val2 = request.GET['num2']
    res = str(int(val1)+int(val2))

    return render(request, 'result.html', {'result': res})
