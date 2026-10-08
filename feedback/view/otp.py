from django.shortcuts import render, redirect
from feedback.forms import OTPVerificationForm
from feedback.models import EmailOTP, Student

def otp(request):
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            otp_entered = form.cleaned_data['otp']
            email_otp = EmailOTP.objects.filter(otp=otp_entered).first()
            if email_otp:
                email_otp.delete()  
                return redirect('login') 
            else:
                messages.error(request, 'Invalid OTP. Please try again.')
                return redirect('verify_otp')
    else:
        form = OTPVerificationForm()
    return render(request, 'verify_otp.html', {'form': form})
