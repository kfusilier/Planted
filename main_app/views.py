from django.shortcuts import render
from django.views import View # class to handle requests
from django.http import HttpResponse # class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Plant

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
	template_name = "home.html"

class About(TemplateView):
	template_name = "about.html"

class Profile(TemplateView):
	template_name = "profile.html"

class Plant_Detail(TemplateView):
	template_name = "plant_detail.html"

class Note_Detail(TemplateView):
	template_name = "note_detail.html"

class Calendar(TemplateView): 
	template_name = "calendar.html"

class Plant_List(TemplateView):
	template_name = "plant_list.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# to get the query parameter we have to acccess it in the request.GET dictionary object        
		kind = self.request.GET.get("kind")
		# If a query exists we will filter by kind
		if kind != None:
		# .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
			context["plants"] = Plant.objects.filter(kind__icontains=kind)
		else:
			context["plants"] = Plant.objects.all()
		return context
