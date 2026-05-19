from django.http import HttpResponse
from django.shortcuts import render
from .models import Student, StudentForm


def index(request):
    std=Student.objects.all()
    return render(request, 'index.html', {'students': std, "form": StudentForm()})

def get_student(request,pk):
    std=Student.objects.get(id=pk)
    return render(request,'Student.html',{'student':std})

def createStudent(request):
    if request.method=="POST":
        student=StudentForm(request.POST)
        if student.is_valid():
            student.save()
    return render(request,'index.html',{'students':Student.objects.all()})