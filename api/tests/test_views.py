import re
from tkinter.messagebox import NO
from urllib import response
import pytest
from django.test import TestCase
from mixer.backend.django import mixer
pytestmark=pytest.mark.django_db
from student_classroom.models import Student,Classroom
from django.urls import reverse
from rest_framework.test import APIClient # this for testing api
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
User=get_user_model()

class TestStudentAPIView(TestCase):

    def setUp(self):
        self.client=APIClient()
        #method 1 to get token
        # self.our_user=User.objects.create_user(username="testuser",password="shahid@grg")
        # self.token=Token.objects.create(user=self.our_user)
        # print(self.token.key,"token")
        # print("client",self.client)
        # self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)

        #method 2 to get token from url
        """This is second method to get token using url"""
        our_user=User.objects.create_user(username="testuser", password="shahid@grg")
        
        data={"username":"testuser","password":"shahid@grg"}
        self.url=reverse('api-auth-token')
        response=self.client.post(self.url,data=data)
        self.token = response.data['token']
        print(self.token)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token)
    
    def test_student_list_api(self):
        
        #create student
        student=mixer.blend(Student,first_name="shahid")
        #call url
        response=self.client.get(reverse('student-list-api'))
        # response=self.client.get("http://127.0.0.1:8000/api/student/list/api/")
        print("response",response.status_code)

        #assertion
        assert response.json != None
        assert len(response.json())==1
        assert response.json()[0]['first_name']=="shahid"
        assert response.status_code == 200
    
    def test_student_create(self):
        input_data={
            "first_name": "cristiano",
            "last_name": "footballer",
            "username": "",
            "admission_number": 12,
            "is_qualified": True,
            "average_score": 70
            }
        url=reverse('student-create-api')
        response=self.client.post(url,data=input_data)
        print(response.data)
        assert response.status_code==201
        assert response.json() != None
        assert Student.objects.count() == 1
    
    def test_student_detail(self):
        student=mixer.blend(Student,first_name="james",pk=1)
        student2=mixer.blend(Student,first_name="sames",pk=2)
        url=reverse('student-detail-delete-api',kwargs={"pk":1})
        url2=reverse('student-detail-delete-api',kwargs={"pk":2})
        response=self.client.get(url)
        response2=self.client.get(url2)
        assert response.status_code == 200
        assert response2.status_code == 200

    def test_student_delete(self):
        student=mixer.blend(Student,pk=1,first_name="james") #mixer also generate unique pk so specify pk also
        student2=mixer.blend(Student,first_name="sames",pk=2) #mixer also generate unique pk so specify pk to use further
        url=reverse('student-detail-delete-api',kwargs={"pk":1}) 
        url2=reverse('student-detail-delete-api',kwargs={"pk":2})
        response=self.client.delete(url)
        response2=self.client.delete(url2)
        assert Student.objects.count() == 0
        
class TestClassroomAPIView(TestCase):

    def setUp(self):
        self.our_user=User.objects.create_user(username="testuser",password="shahid@grg")
        self.token=Token.objects.create(user=self.our_user)
        print(self.token.key,"token")
        self.client=APIClient()
        print("client",self.client)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key) # appending authentication
    
    def test_classroom_get_api(self):
        classroom =mixer.blend(Classroom,student_capacity=20)
        classroom2 =mixer.blend(Classroom,student_capacity=25)
        url=reverse('classroom-get-api',kwargs={"student_capacity":25})
        response=self.client.get(url)
        print(response)
        assert response.status_code == 200
       
        assert response.data['classroom_data'] != []
        assert response.data['number_of_classes'] == 2