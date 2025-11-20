from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('schedule/', views.schedule, name='schedule'),
]