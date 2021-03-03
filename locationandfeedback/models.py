from django.db import models

# Create your models here.


class Feedback(models.Model):
    feedback_text = models.CharField(max_length=200)


class Rateapp(models.Model):
    rateapp = models.IntegerField()
