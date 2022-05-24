from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveDestroyAPIView
from rest_framework.views import APIView
from student_classroom.models import Classroom, Student
from .serializers import StudentSerializer,ClassroomSerializer
from mixer.backend.django import mixer

# Create your views here.
class StudentListAPI(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentCreateAPI(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentDetailDeleteAPI(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class ClassroomAPIView(APIView):
    queryset=Classroom.objects.all()
    serializer_class=ClassroomSerializer

    def get(self,*args, **kwargs):
        url_number=self.kwargs.get("student_capacity")
        print(url_number)
        # classroom =mixer.blend(Classroom,student_capacity=2)
        classroom_qs=Classroom.objects.filter(student_capacity__lte = url_number)
        number_of_classes=classroom_qs.count()
        serialized_data=ClassroomSerializer(classroom_qs,many=True)
        if serialized_data.is_valid: # on retrieving data .is_valid work
            return Response({
                "classroom_data":serialized_data.data,
                "number_of_classes":number_of_classes

            })
        return Response(serialized_data.errors)
      

