from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login1,name='login'),
    path('logout/',views.logout1,name='logout'),
    path('apply/',views.apply,name='apply'),
]