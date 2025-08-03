from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('applicant/<int:applicant_id>/', views.applicant_detail, name='applicant_detail'),
    path('update-status/<int:applicant_id>/', views.update_status, name='update_status'),
] 