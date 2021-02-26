from django.db import models
from phone_field import PhoneField
from django.core.validators import RegexValidator
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10}$', message="Phone number must be 10 digits and  entered in the format: '98XXXXXXXX'.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=13)  # validators should be a list
    url_location = models.URLField(max_length=200, null=True)
    amount = models.PositiveIntegerField(null=True)
    length = models.PositiveIntegerField(null=True)
    breadth = models.PositiveIntegerField(null=True)
    image1 = models.ImageField(upload_to='images/', default=True)
    image2 = models.ImageField(upload_to='images/', default=True)
    image3 = models.ImageField(upload_to='images/', default=True)
    image4 = models.ImageField(upload_to='images/', default=True)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Name
