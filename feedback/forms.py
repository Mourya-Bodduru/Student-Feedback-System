from django import forms
from feedback.models import Student,Feedback
from django.forms import ModelForm

class MemberForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        fields = '__all__'



class OTPForm(forms.Form):
    otp = forms.CharField(label='Enter OTP', max_length=6, widget=forms.TextInput(attrs={'autocomplete': 'off'}))


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label='Current Password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['tname', 'sname', 'dept','feedback_text', 'rating']