from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from vertical.models import Boulder
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
import datetime

class HomePageView(TemplateView):
    template_name = "vertical/displayPage.html"

class DisplayPageView(TemplateView):
    template_name ="vertical/displayPage.html"
    model = Boulder

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['boulders'] = Boulder.objects.all()
        return context

class CreatePageView(TemplateView):
    template_name ="vertical/createPage.html"

@csrf_exempt
def boulder_post_method(request):
    print(request.POST.items())
    if request.method=='POST':
        boulder=Boulder()
        boulder.boulder_description = request.POST.get('boulder_description')
        boulder.boulder_difficulty = request.POST.get('boulder_difficulty')
        boulder.boulder_creator = request.POST.get('boulder_creator')
        boulder.boulder_name = request.POST.get('boulder_name')
        boulder.boulder_data = request.POST.get('boulder_data')
        boulder.save()
    template = loader.get_template('vertical/displayPage.html')
    book = Boulder.objects.all()
    context = {"boulders": book}


    return render(request,'vertical/displayPage.html',context)
@csrf_exempt
def boulder_edit_post_method(request):
    if request.method=='POST':
        c = Boulder.objects.get(pk = request.POST.get('boulder_id'))
        c.boulder_description = request.POST.get('boulder_description')
        c.boulder_difficulty = request.POST.get('boulder_difficulty')
        c.boulder_creator = request.POST.get('boulder_creator')
        c.boulder_name = request.POST.get('boulder_name')
        c.boulder_data = request.POST.get('boulder_data')
        c.save()

    template = loader.get_template('vertical/displayPage.html')
    boulder = Boulder.objects.all()
    context = {"boulders": boulder}


    return HttpResponse(template.render(context))

def request_method(request,boulder_id):
    c = Boulder.objects.get(pk = boulder_id)
    c.led_logic()
    template = loader.get_template('vertical/displayPage.html')
    boulder = Boulder.objects.all()
    context = {"boulders": boulder}


    return HttpResponse(template.render(context))
@csrf_exempt
def edit_method(request,boulder_id):
    c = Boulder.objects.get(pk = boulder_id)
    template = loader.get_template('vertical/editPage.html')
    context = {"boulders": c}

    return HttpResponse(template.render(context))
def delete_method(request,boulder_id):
    c = Boulder.objects.get(pk = boulder_id)
    c.delete()
    template = loader.get_template('vertical/displayPage.html')

    boulder = Boulder.objects.all()
    context = {"boulders": boulder}


    return HttpResponse(template.render(context))
def turn_off_led_view(request):
    id = 1
    c = Boulder.objects.get(pk = id)
    c.turn_off_led()
    template = loader.get_template('vertical/displayPage.html')

    book = Boulder.objects.all()
    context = {"boulders": book}


    return HttpResponse(template.render(context))
