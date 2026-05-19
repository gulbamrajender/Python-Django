from django.urls import path

from test_app import views



urlpatterns = [
    path('student', views.index, name='students'),
    path('student/<int:pk>/', views.get_student, name='student'),
    path('createStudent', views.createStudent, name='createStudent'),
]