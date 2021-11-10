from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def login(request):
    context = {
        'credits': 10
    }
    return render(request, 'signup.html',context=context)