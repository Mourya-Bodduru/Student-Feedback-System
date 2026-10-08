from django import forms

class EmailForm(forms.Form):
    to_address = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

class OTPForm(forms.Form):
    email = forms.EmailField()

class OTPValidationForm(forms.Form):
    otp = forms.CharField(max_length=6)