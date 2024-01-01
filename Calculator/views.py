from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    c = 0
    result = 0
    if request.method=="POST":
        n1 =float(request.POST.get('Num1'))
        n2 =float( request.POST.get('Num2'))
        n3 =float(request.POST.get('Num3'))
        n4 =float(request.POST.get('Num4'))
        a=(n1+n2)/2
        b=(n3+n4)/2
        d=a*b
        c=d/1089
        if c > 0:
            result = c
        else:  
            result = "Invalid Data"

    
    return render(request,'cal.html',{"c":result})


