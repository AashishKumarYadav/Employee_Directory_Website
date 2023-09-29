from django.http import HttpResponse
from django.shortcuts import render
from employess.models import Employee

def home(request):
    employess = Employee.objects.all()
    print(employess)
    context = {
        'employess': employess,
    }
    return render(request, 'task.html', context)
#,{'dynamic_data': 'Hello, dynamic data given By Aashish'})