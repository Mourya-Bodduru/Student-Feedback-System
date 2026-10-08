from django.http import HttpResponse
from django.template import loader

def thank_you(request):
  template = loader.get_template('pages/thank_you.html')
  return HttpResponse(template.render())