from django.urls import path
from . import views

urlpatterns = [
    path('generate', views.generate_qr_code, name='generate_qr_code'),
    path('validate/<str:exam_regis>/', views.validate_exam, name='validate_exam'),
]
