from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def homepage(request):#名稱自己定義(homepage)
    posts = Post.objects.all() #select * from post
    now = datetime.now()
    return render (request, 'index.html',locals())

def showpost(request,slug):
    post = Post.objects.get(slug=slug)
    #select*from post where slug=%slug
    return render (request, 'post.html',locals())
    

'''
def homepage(request):#名稱自己定義(homepage)
    posts = Post.objects.all() #select * from post
    post_list = list()
    for counter, post in enumerate(posts):
        post_list.append(f'No.{counter}-{post} <br>') #br為網頁換行
    return HttpResponse(post_list)
'''