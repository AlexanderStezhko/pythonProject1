from django.urls import path

from .views import *

urlpatterns = [
   path('',BlogHome.as_view(), name='home'),
   path('aboutblog/', about, name='about'),
   path('add_page/', AddPage.as_view(), name='add_page'),
   path('contact/', contact, name='contact'),
   path('logout/', logout_user, name='logout'),
   path('login/', LoginUser.as_view(), name='login'),
   path('register/', RegisterUser.as_view(), name='register'),
   path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
   path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
]