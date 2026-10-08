from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from . .models import Student,Feedback,Contact

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            data= Student.objects.all().values()
            data1=Feedback.objects.all().values()
            contacts = Contact.objects.all().values()
            content={
                'data':data,
                'data1':data1,
                'contacts':contacts,
            }
            return render(request,'pages/admin_dashboard.html',content)
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'pages/admin_login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'pages/admin_login.html')
