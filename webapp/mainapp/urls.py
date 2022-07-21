from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about,name='about'),
    path('create',views.create,name='create_contact'),
    path('<int:pk>',views.DetailViewTest.as_view(),name='details_contact'),
    path('<int:pk>/update',views.DetailUpdateViewTest.as_view(),name='details_updete_contact'),
    path('<int:pk>/delete',views.DetailDeleteViewTest.as_view(),name='details_delete_contact'),

]