from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def index(request):
    blog_title = "Latest posts"
    # return HttpResponse("good")
    return render(request,'blog/index.html')
