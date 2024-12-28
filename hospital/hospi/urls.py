from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.list_doctors, name='list_doctors'),
    path('', views.list_doctors, name='home'), 
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/<int:doctor_id>/add_patient/', views.add_patient, name='add_patient'),
]
