from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def index(request):
    return HttpResponse("University")


def add_student(request):
    student = Student()
    student.name = "fdfsfs"
    student.group = "316-17"
    student.age = 23
    student.save()
    return HttpResponse("Student Added")


def student_list(request):
    students = Student.objects.all()
    for student in students:
        print(student)
    return HttpResponse("Student List")
