from django import urls
from django.urls import path
from genius.views import (home, Class_create, Class_Update, Class_Delete, Class_Detail, Classes, Add_name,
                          Student_Main, Student_Create, Student_Update, Student_Delete, Student_Detail, Search)

app_name = 'genius'

urlpatterns = [
    path('', home, name='home'),
    path('class/', Classes, name='class'),
    path('class/add-name', Add_name, name='add-name'),
    path('class/create', Class_create, name='create-class'),
    path('class/<int:id>', Class_Detail, name='detail'),
    path('class/<int:id>/edit/', Class_Update, name='update'),
    path('class/<int:id>/delete/', Class_Delete, name='delete'),
    path('stds/', Student_Main, name='stds'),
    path('stds/create', Student_Create, name='stds-new'),
    path('stds/<int:id>',Student_Detail , name='std-detail'),
    path('stds/search/',Search , name='std-search'),
    path('stds/<int:id>/edit/', Student_Update, name='std-update'),
    path('stds/<int:id>/delete/', Student_Delete, name='std-delete'),
]
