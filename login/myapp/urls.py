
from django.urls import path
from .views import student_register, practitioner_register

urlpatterns = [
    path('student_register/', student_register, name='student_register'),
    path('practitioner_register/', practitioner_register, name='practitioner_register'),
]
