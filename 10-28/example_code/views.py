from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article, Category 

from django.http import HttpResponse
def home(request):
    s="Hello World!"
    return HttpResponse(s)               

def detail(request, pk):
    article=Article.objects.get(id=int(pk))
    s="""
    <html>
    <head></head>
    <body>
    <h1>{0}</h1>
    {1}
    </body>
    </html>
    """.format(article.title,article.content)
    return HttpResponse(s)

# Create your views here.
