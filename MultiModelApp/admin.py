from django.contrib import admin
from .models import Department,Employee,Student,School

class OrderField(admin.ModelAdmin):
    fields = ["schoolname","studentname","studentId","studentsection","studentmark"]

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(School,OrderField)
admin.site.register(Student)

