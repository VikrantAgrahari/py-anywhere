from django import urls
from django.urls import path
from .views import ( login_user ,login_page, logout_user, Usercreation, UserProfile, EditProfile)


app_name = 'user'

urlpatterns = [
    path('login/',login_page,name='login_page'),
    path('login_user/',login_user, name='login_user'),
    path('logout/',logout_user, name='logout'),
    path('new_user/',Usercreation, name='new_user'),
    path('profile/',UserProfile, name='profile'),
    path('edit_profile/', EditProfile, name='edit_profile'),
]
