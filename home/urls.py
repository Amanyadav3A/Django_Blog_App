from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('',home_view,name='home'),
    path('dashboard/',dashboard_view,name='dashboard'),
    path('create_post/',create_post,name='create_post'),
    path('update_post/<int:id>/',update_post,name='update_post'),
    path('delete_post/<int:id>/',delete_post,name='delete_post'),
    path('post_api/<str:id>/',post_api),
    path('comment_api/<str:id>/',comment_api),
]
