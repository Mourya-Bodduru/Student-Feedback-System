from django.shortcuts import render,redirect
from . .models import Feedback,Student,Contact

def feedback_delete(request,id):
    user = Feedback.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        data1=Feedback.objects.all().values()
        data=Student.objects.all().values()
        data2=Contact.objects.all().values()
        return render(request,'pages/admin_dashboard.html',{'data1':data1,'data':data,'data2':data2})
    data1 = Feedback.objects.filter(id=id).values()
    return render(request,"pages/feedback_delete.html",{'data1':data1})

def contact_delete(request,id):
    user = Contact.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        data1=Feedback.objects.all().values()
        data=Student.objects.all().values()
        data2=Contact.objects.all().values()
        return render(request,'pages/admin_dashboard.html',{'data1':data1,'data':data,'data2':data2})
    data2 = Contact.objects.filter(id=id).values()
    return render(request,"pages/contact_delete.html",{'data2':data2})
