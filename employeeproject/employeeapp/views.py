from django.shortcuts import render
from .models import employeedata
def employeeview(request):
    if request.method=="POST":
        name=request.POST.get('name')
        location=request.POST.get('location')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        username=request.POST.get('username')
        password=request.POST.get('password')
        a=employeedata(name1=name,
                       location1=location,
                       email1=email,
                       mobile1=mobile,
                       username1=username,
                       password1=password)
        a.save()
        return render(request,'employee.html')
    else:
        return render(request,'employee.html')


