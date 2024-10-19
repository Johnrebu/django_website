from django.db import models

# Create your models here.

class EmployeeDetails(models.Model):
    empid=models.IntegerField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    designation=models.CharField(max_length=50)

    def __str__(self):
        return self.username










