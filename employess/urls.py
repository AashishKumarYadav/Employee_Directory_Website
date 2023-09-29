from django.urls import path
from .import views

urlpatterns = [
    #pk == emp id
    path('<int:pk>/',views.employee_detail, name='employee_detail')
]