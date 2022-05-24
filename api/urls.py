from django.urls import path
from .views import StudentListAPI,StudentCreateAPI,StudentDetailDeleteAPI,ClassroomAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/auth/token/',obtain_auth_token,name='api-auth-token'),
    path('student/list/',StudentListAPI.as_view(),name='student-list-api'),
    path('student/create/',StudentCreateAPI.as_view(),name='student-create-api'),
    path('student/detail/delete/<int:pk>/',StudentDetailDeleteAPI.as_view(),name='student-detail-delete-api'),
    path('classroom/<int:student_capacity>/',ClassroomAPIView.as_view(),name='classroom-get-api'),
]