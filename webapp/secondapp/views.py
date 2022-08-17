from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView, CreateView
from .forms import *
from .models import *
from django.http import HttpResponse, Http404
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

#def index(request):
#    posts = Blog.objects.all()
#    context = {'posts': posts,
#               'menu':menu,
#               'title':"Заглавие страницы"}
#    return render(request,'secondapp/index.html', context=context)

class BlogHome(DataMixin,ListView):
    model = Blog
    template_name = 'secondapp/index.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)

def about(request):
    return render(request,'secondapp/about.html',{'menu':menu})

# def add_page(request):
#     if request.method=='POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             try:
#                 #Blog.objects.create(**form.cleaned_data)
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None,'Ошибка добавления статьи')
#     else:
#         form = AddPostForm()
#     return render(request,'secondapp/addpage.html',{'form':form,' menu':menu,'title': "Добавление статьи"})

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'secondapp/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items())+list(c_def.items()))

def contact(request):
    return HttpResponse('text')



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'secondapp/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'secondapp/login.html'

    def get_context_data(self, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

class ShowPost(DataMixin,DeleteView):


    model = Blog
    template_name = 'secondapp/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items())+list(c_def.items()))


# def show_category(request, cat_slug):
#     cat = Category.objects.filter(slug=cat_slug)
#     posts = Blog.objects.filter(cat_id = cat[0].id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_slug,
#     }
#
#     return render(request, 'secondapp/index.html', context=context)

class BlogCategory(DataMixin,ListView):
    model = Category
    template_name = 'secondapp/index.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория '+ str(context['object_list'][0].cat),cat_selected = context['object_list'][0].cat_id)

        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'],is_published=True)
