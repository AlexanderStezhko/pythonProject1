from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *
from django.http import HttpResponse, Http404


# Create your views here.
menu = [{'title':'About site','url_name':'about'},
        {'title':'Add post','url_name':'add_page'},
        {'title':'Feedback','url_name':'contact'},
        {'title':'Log in','url_name':'login'},]
def index(request):
    posts = Blog.objects.all()
    context = {'posts': posts,
               'menu':menu,
               'title':"Заглавие страницы"}
    return render(request,'secondapp/index.html', context=context)

def about(request):
    return render(request,'secondapp/about.html',{'menu':menu})

def add_page(request):
    if request.method=='POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Blog.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None,'Ошибка добавления статьи')
    else:
        form = AddPostForm()
    return render(request,'secondapp/addpage.html',{'form':form,' menu':menu,'title': "Добавление статьи"})

def contact(request):
    return HttpResponse('text')

def login(request):
    return HttpResponse('text')

def show_post(request,post_slug):
    post = get_object_or_404(Blog,slug=post_slug)

    context={
        'post':post,
        'menu':menu,
        'title':post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'secondapp/post.html', context=context)

def show_category(request, cat_slug):
    cat = Category.objects.filter(slug=cat_slug)
    posts = Blog.objects.filter(cat_id = cat[0].id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_slug,
    }

    return render(request, 'secondapp/index.html', context=context)