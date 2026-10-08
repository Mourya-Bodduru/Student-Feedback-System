from django.shortcuts import render,redirect
from . .models import Contact

def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

       


        if name and email and message: 
            data = Contact(name=name, email=email, message=message)
            data.save()
            return redirect('thank_you')  

    return render(request , 'pages/contact.html')