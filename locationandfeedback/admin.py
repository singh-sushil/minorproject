from django.contrib import admin

# Register your models here.
from .models import Feedback, Rateapp
admin.site.register(Feedback)
admin.site.register(Rateapp)
