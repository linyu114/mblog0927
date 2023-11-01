from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
    
def showpost(request, slug):
<<<<<<< HEAD
    post = Post.objects.get(slug=slug)
    return render(request, 'post.html', locals())
=======
    try:
        post = Post.objects.get(slug=slug) 
        if post != None:
            return render(request, 'post.html', locals())
        else:
            return redirect("/")    
    except:
        return redirect("/")
>>>>>>> df6a38d506e3fc075fea8eef96cc21209d0e407b
    #select * from post where slug=%slug
    

'''
def homepage(request):#名稱自己定義(homepage)
    posts = Post.objects.all() #select * from post
    post_list = list()
    for counter, post in enumerate(posts):
        post_list.append(f'No.{counter}-{post} <br>') #br為網頁換行
    return HttpResponse(post_list)
'''