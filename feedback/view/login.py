from django.shortcuts import render, redirect
from django.contrib import messages
from . .models import *

def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        if Student.objects.filter(username=username).exists():
            data1=Student.objects.get(username=username)
            data2=Student.objects.filter(username=username).values()
            if data1.password1 == password:
                content={
                    'data2':data2,
                }
                return render(request,'pages/dashboard.html',content)
            else:
                messages.error(request,"You entered invalid password")
                return redirect('login')
        else:
            messages.error(request,"No such Student exists")
            return redirect('login')
    else:
        return render(request, 'pages/login.html')
