from rest_framework.serializers import ModelSerializer
from student_classroom.models import *

#serializers
class StudentSerializer(ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class ClassroomSerializer(ModelSerializer):
    class Meta:
        model=Classroom
        fields='__all__'