from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('register/',views.register,name='register'),
    path('login/',views.login1,name='login'),
    path('logout/',views.logout1,name='logout'),
    path('apply/<id>',views.apply,name='apply'),
    path('internship_applied/<id>',views.internship_applied,name='internship_applied'),
    path('add_internship',views.add_internship,name='add_internship'),
    path('view_responses/<id>',views.view_responses,name='view_responses'),
    path('download',views.download,name='download'),
    path('announcement',views.announcement,name='announcement'),
    path('all_announcements',views.all_announcements,name='all_announcement'),
    path('all_announcements_student',views.all_announcements_student,name='all_announcements_student'),
    path('edit_internship/<id>',views.edit_internship,name='edit_internship'),
    path('delete_internship<id>',views.delete_internship,name='delete_internship')
]