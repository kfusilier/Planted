from django.contrib import admin
from .models import Plant, Note, Pest # import Plant model from models.py


# Register your models here.
admin.site.register(Plant) # <-this line adds model to admin panel
admin.site.register(Note)
admin.site.register(Pest)