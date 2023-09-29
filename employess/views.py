from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from employess.models import Employee

# Create your views here.

def employee_detail(request,pk):
    employee = get_object_or_404(Employee,pk=pk)
    #print(employee)
    context = {
        'employee' : employee
    }
    return render(request,'employee_detail.html', context)
