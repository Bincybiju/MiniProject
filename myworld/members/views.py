from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def form(request):
  template = loader.get_template('form.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  a = request.POST['first']
  b = request.POST['last']
  c = request.POST['se']
  d = request.POST['mail']
  e = request.POST['psw']

  member = Members(firstname=a, lastname=b,sex=c,email=d,password=e)
  member.save()
  return HttpResponseRedirect(reverse('index'))