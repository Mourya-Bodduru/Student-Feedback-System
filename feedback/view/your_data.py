from django.http import HttpResponse
from django.template import loader

def your_data(request):
  template = loader.get_template('pages/your_data.html')
  return HttpResponse(template.render())