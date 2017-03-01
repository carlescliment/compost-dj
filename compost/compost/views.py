from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    return HttpResponse('<h1>Compost</h1><p> It is %s' % now)
