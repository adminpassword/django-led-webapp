from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from vertical.models import Boulder
from django.http import HttpResponse
from django.template import loader
import datetime

class HomePageView(TemplateView):
    template_name = "vertical/vert.html"

class DisplayPageView(TemplateView):
    template_name ="vertical/displayPage.html"
    model = Boulder

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['boulders'] = Boulder.objects.all()
        return context



def request_method(request,boulder_id):
    c = Boulder.objects.get(pk = boulder_id)
    print(boulder_id,c.boulder_data)
    c.led_logic()
    template = loader.get_template('vertical/vert.html')
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(template.render())
