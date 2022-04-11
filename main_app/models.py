from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import calendar 


class Pest(models.Model):
	name = models.CharField(max_length=100)
	img = models.CharField(max_length=500)
	method = models.CharField(max_length=300)
	treatment = models.CharField(max_length=300)
	
	def __str__(self):
		return self.name

SUCCESSION_CHOICES = (
	('Not Applicable', 'N/A' ),
	('Re-seed every 7 days', 'every 7 days'),
	('Re-seed every 14 days', 'every 14 days'),
	('Re-seed every 21 days', 'every 21 days'),
	('Re-seed every 30 days', 'every 30 days')
)

SUNLIGHT_CHOICES = (
	('Full Sun: minimum 6 hours direct sunlight', 'Full-Sun'),
	('Partial Sun: 3-6 hours direct sunlight', 'Part-Sun'),
	('Full Shade: less than 3 hours direct sunlight', 'Full-Shade'),
	('Partial Shade: 3-6 hours of sunlight, protect from mid-day sunlight', 'Part-Shade')
)

SEED_DEPTH_CHOICES = (
	('Surface, no cover', 'surface' ),
	('less-than 1/4 inch deep', 'less than 1/4 inch'),
	('1/4 inch deep', '1/4 inch'),
	('1/2 inch deep', '1/2 inch'),
	('2/3 inch deep', '2/3 inch'),
	('1 inch deep', '1 inch'),
	('more than 1 inch deep', 'more than 1 inch')
)

class Plant(models.Model):

	kind = models.CharField(max_length=30)
	variety = models.CharField(max_length=50)
	img = models.CharField(max_length=500)
	seed_depth = models.CharField(max_length=80, choices = SEED_DEPTH_CHOICES)
	seed_spacing = models.IntegerField()
	germination = models.IntegerField()
	plant_spacing = models.IntegerField()
	row_spacing = models.IntegerField()
	days_to_harvest = models.IntegerField()
	sunlight = models.CharField(max_length=80, choices = SUNLIGHT_CHOICES)
	indoor_start = models.DateField()
	indoor_stop = models.DateField()
	transplant_start = models.DateField()
	transplant_stop = models.DateField()
	outdoor_start = models.DateField()
	outdoor_stop = models.DateField()
	succession = models.CharField(max_length=50, choices = SUCCESSION_CHOICES)
	pests = models.ManyToManyField(Pest)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
	created_at = models.DateTimeField(auto_now_add=True)
	# updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.kind

	class Meta:
		ordering = ['kind']

class Note(models.Model):
	title = models.CharField(max_length=30)
	date = models.DateTimeField(default=timezone.now)
	body = models.CharField(max_length=250)
	plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
	def __str__(self):
		return self.title

		