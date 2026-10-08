from django.shortcuts import render,redirect
from . .models import Student,Feedback,Contact

def delete(request,id):
    user = Student.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        data=Student.objects.all().values()
        data1=Feedback.objects.all().values()
        data2 = Contact.objects.all().values()
        return render(request,'pages/admin_dashboard.html',{'data':data , 'data1':data1 ,'data2':data2})
    data = Student.objects.filter(id=id).values()
    return render(request,"pages/delete.html",{'data':data})

