from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from feedback.forms import OTPForm
from feedback.utils import generate_otp
from feedback.models import Student,Feedback

def register(request):
    if request.method == 'POST':
        reg_no = request.POST.get('reg_no')
        stu_name = request.POST.get('username')
        year = request.POST.get('year')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Password mismatched!')
            return redirect('register')

        if Student.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('register')

        if Student.objects.filter(username=stu_name).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        otp = generate_otp()
        request.session['otp'] = otp
        request.session['reg_no'] = reg_no
        request.session['username'] = stu_name
        request.session['year'] = year
        request.session['email'] = email
        request.session['password1'] = password1 

        send_mail(
            'Your OTP',
            f'Your OTP is : {otp}',
            'kusumakarthikeya0@gmail.com', 
            [email],
            fail_silently=False,
        )

        return redirect('verify_otp')

    return render(request, 'pages/register.html')


def verify_otp(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            stored_otp = request.session.get('otp')
            if stored_otp and entered_otp == stored_otp:
                reg_no = request.session.get('reg_no')
                stu_name = request.session.get('username')
                year = request.session.get('year')
                email = request.session.get('email')
                password = request.session.get('password1') 
                user = Student(username=stu_name, email=email, password1=password, reg_no=reg_no, year=year)
                user.save()

                messages.success(request, 'Registration successful! You can now login.')
                return redirect('login')  
            else:
                messages.error(request, 'Invalid OTP!')
                return redirect('verify_otp')
    else:
        form = OTPForm()

    return render(request, 'pages/verify_otp.html', {'form': form})
