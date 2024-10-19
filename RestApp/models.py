from django.db import models

# Create your models here.
class Student(models.Model):
    studentname=models.CharField(max_length=16)
    phno=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.studentname