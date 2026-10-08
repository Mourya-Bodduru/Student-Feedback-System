from django.http import HttpResponse
from django.template import loader

def about(request):
  template = loader.get_template('pages/about.html')
  return HttpResponse(template.render())