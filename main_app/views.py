from django.shortcuts import render
from django.views import View # class to handle requests
from django.http import HttpResponse # class to handle sending a type of response
#...
from django.views.generic.base import TemplateView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Plant:
    def __init__(self, kind, variety, germination):
        self.kind = kind
        self.variety = variety
        self.germination = germination

plants = [
    Plant('Carrot', 'Atomic Purple', '10 days'),
    Plant('Tomato', 'Cherry', '12 days'),
    Plant('Eggplant', 'Fairy Tale', '15 days'),
]

class Plant_List(TemplateView):
    template_name = "plant_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["plants"] = plants # this is where we add the key into our context object for the view to use
        return context









class Profile(TemplateView):
    template_name = "profile.html"

class Plant_Detail(TemplateView):
    template_name = "plant_detail.html"

class Note_Detail(TemplateView):
    template_name = "note_detail.html"

class Calendar(TemplateView): 
    template_name = "calendar.html"
    