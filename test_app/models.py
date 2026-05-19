from django.db import models
from django.forms import ModelForm

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    branch = models.CharField(max_length=100)
    marks = models.IntegerField()
    college = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'branch', 'marks', 'college']