from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student-add/', views.add_student, name='add-student'),
    path('student-list/', views.student_list, name='student-list')
]
