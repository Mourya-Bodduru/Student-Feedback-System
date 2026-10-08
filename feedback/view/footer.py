from django.http import HttpResponse
from django.template import loader

def footer(request):
  template = loader.get_template('components/footer.html')
  return HttpResponse(template.render())