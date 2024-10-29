from django.db import models

# Create your models here.

class Course(models.Model):
    number = models.CharField(max_length=50)
    

class Student(models.Model):
    name = models.CharField(max_length=255)
    course = models.ManyToManyField(Course)
    
    
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)