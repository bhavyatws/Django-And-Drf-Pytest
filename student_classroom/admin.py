from django.contrib import admin
from student_classroom.models import *
# Register your models here.
admin.site.register((Classroom,Student))