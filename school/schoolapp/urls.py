from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_content,name='index'),
    path('form/',views.form_content,name='index')
]