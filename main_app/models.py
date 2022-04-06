from django.db import models

SUCCESSION_CHOICES = (
	('N/A', 'not applicable'),
	('7', 're-seed every 7 days'),
	('14', 're-seed every 14 days'),
	('21', 're-seed every 21 days'),
	('30', 're-seed every 30 days')
)

class Plant(model.Model):

	kind = models.Charfield(max_length=30)
	variety = models.Charfield(max_length=50)
	seed_depth = models.Integerfield()
	seed_spacing = models.Integerfield()
	germination = models.Integerfield()
	plant_spacing = models.Integerfield()
	row_spacing = models.Integerfield()
	days_to_harvest = models.Integerfield()
	sunlight = models.Integerfield()
	indoor_start = models.Datefield()
	indoor_stop = models.Datefield()
	transplant_start = models.Datefield()
	transplant_stop = models.Datefield()
	outdoor_start = models.Datefield()
	outdoor_stop = models.Datefield()
	succession = models.CharField(max_length=50, choices = CATEGORY_CHOICES)
	notes = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.kind

	class Meta:
		ordering = ['kind']

	# user = models.ForeignKey(User, on_delete=models.CASCADE)
		
