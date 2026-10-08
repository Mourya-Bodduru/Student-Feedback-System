from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import *
from .utils import *

# Create your views here.

# def send_email(request):
#     send_mail(
#         'This is testing',
#         'Hello Good Morning',
#         'veerapraveena12@gmail.com',
#         ['satishchikoti6012sky@gmail.com'],
#         fail_silently=False
#     )
#     return HttpResponse("Email send succesfully")

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            to_address = form.cleaned_data['to_address']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                subject,
                message,
                'from@example.com',
                [to_address],
                fail_silently=False,
            )
            return HttpResponse("Email send succesfully")
    else:
        form = EmailForm()
    return render(request, 'email_form.html', {'form':form})

def send_otp(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            otp = generate_otp()
            request.session['otp'] = otp
            send_mail(
                'Your OTP',
                f'Your OTP is : {otp}',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return redirect('validate_otp')
        
    else:
        form = OTPForm()

    return render(request,'otp_form.html',{'form':form})

def validate_otp(request):
    if request.method == 'POST':
       form = OTPValidationForm(request.POST)
       if form.is_valid():
           entered_otp = form.cleaned_data['otp']
           stored_otp = request.session.get('otp')

           if stored_otp and entered_otp == stored_otp:
               return HttpResponse('otp match')
           else:
               return HttpResponse('not match')
    else:
        form = OTPValidationForm()
    return render(request,'otp_validation.html',{'form':form})
