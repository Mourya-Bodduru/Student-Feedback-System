from django.http import HttpResponse
from django.template import loader
from feedback.models import Student
from feedback.models import Feedback
from feedback.models import Contact


def admin_dashboard(request):
    template = loader.get_template('pages/admin_dashboard.html')
    data = Student.objects.all().values()
    data1 = Feedback.objects.all().values()
    contacts = Contact.objects.all().values()
    context = {
        'data': data,
        'data1':data1,
        'contacts':contacts,
    }
    
    return HttpResponse(template.render(context, request))
