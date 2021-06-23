from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def hello(request):
#     return HttpResponse("hello world")
# def hello1(request):
#     return render(request,'sample.html')    
def fun(request):
    return render(request,'v.html')