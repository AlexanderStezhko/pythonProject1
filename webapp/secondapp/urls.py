from django.urls import path

from .views import *

urlpatterns = [
   path('',index, name='home'),
   path('aboutblog/', about, name='about'),
   path('add_page/', add_page, name='add_page'),
   path('contact/', contact, name='contact'),
   path('login/', login, name='login'),
   path('post/<slug:post_slug>/', show_post, name='post'),
   path('category/<slug:cat_slug>/', show_category, name='category'),
]