from django.shortcuts import render

# Create your views here.

from .models import Article

def home(request):
    data = Article.objects.all()

    context ={
        'data':data,
    }
    return render(request,'index.html',context)
