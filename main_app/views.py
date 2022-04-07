from django.shortcuts import render
from django.views import View # class to handle requests
from django.http import HttpResponse # class to handle sending a type of response
from .models import Plant, Note
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

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

# PLANTS
class Plant_List(TemplateView):
	template_name = "plant_list.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# to get the query parameter we have to acccess it in the request.GET dictionary object        
		kind = self.request.GET.get("kind")
		# If a query exists we will filter by kind
		if kind != None:
			context["plants"] = Plant.objects.filter(kind__icontains=kind)
			# We add a header context that includes the search param
			context["header"] = f"Searching for {kind}"
		else:
			context["plants"] = Plant.objects.all()
			# default header for not searching 
			context["header"] = "Master Plant List"
		return context

class Plant_Create(CreateView):
	model = Plant
	fields = [
	'kind',
	'variety',
	'img',
	'seed_depth',
	'seed_spacing',
	'germination',
	'plant_spacing',
	'row_spacing',
	'days_to_harvest',
	'sunlight',
	'indoor_start',
	'indoor_stop',
	'transplant_start',
	'transplant_stop',
	'outdoor_start',
	'outdoor_stop',
	'succession',
	'notes',
	'pests',
	]
	template_name = "plant_create.html"
	success_url = "/plants/"

class Plant_Detail(DetailView):
	model = Plant
	template_name = "plant_detail.html"

class Plant_Update(UpdateView):
	model = Plant
	fields = [
	'kind',
	'variety',
	'img',
	'seed_depth',
	'seed_spacing',
	'germination',
	'plant_spacing',
	'row_spacing',
	'days_to_harvest',
	'sunlight',
	'indoor_start',
	'indoor_stop',
	'transplant_start',
	'transplant_stop',
	'outdoor_start',
	'outdoor_stop',
	'succession',
	'notes',
	'pests',
	]
	template_name = "plant_update.html"
	def get_success_url(self):
		return reverse('plant_detail', kwargs={'pk': self.object.pk})

class Plant_Delete(DeleteView):
    model = Plant
    template_name = "plant_delete.html"
    success_url = "/plants/"

# NOTES
class Note_List(TemplateView):
	template_name = "note_list.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# to get the query parameter we have to acccess it in the request.GET dictionary object        
		kind = self.request.GET.get("kind")
		# If a query exists we will filter by kind
		if kind != None:
			context["notess"] = Note.objects.filter(title__icontains=title)
			# We add a header context that includes the search param
			context["header"] = f"Searching for {title}"
		else:
			context["notes"] = Note.objects.all()
			# default header for not searching 
			context["header"] = "All Notes"
		return context

class Note_Create(CreateView):
	model = Note
	fields = [
	'plant',
	'title',
	'date',
	'body',
	]
	template_name = "note_create.html"
	success_url = "/notes/"

class Note_Detail(DetailView):
	model = Note
	template_name = "note_detail.html"

class Note_Update(UpdateView):
	model = Plant
	fields = [
	'plant',
	'title',
	'date',
	'body',

	]
	template_name = "note_update.html"
	def get_success_url(self):
		return reverse('note_detail', kwargs={'pk': self.object.pk})

class Note_Delete(DeleteView):
    model = Note
    template_name = "note_delete.html"
    success_url = "/notes/"

# Pests
# class Pest_List(TemplateView):
# 	template_name = "pest_list.html"

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		# to get the query parameter we have to acccess it in the request.GET dictionary object        
# 		name = self.request.GET.get("name")
# 		# If a query exists we will filter by kind
# 		if name != None:
# 			context["pests"] = Note.objects.filter(title__icontains=title)
# 			# We add a header context that includes the search param
# 			context["header"] = f"Searching for {title}"
# 		else:
# 			context["notes"] = Note.objects.all()
# 			# default header for not searching 
# 			context["header"] = "All Notes"
# 		return context