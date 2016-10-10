import datetime
from django.db import models
from django.utils import timezone
# Create your models here.



class Car_Master_Data(models.Model):
	website_name = models.CharField(max_length=100,blank=True)
	city_id = models.CharField(max_length=500,blank=True)
	city_name = models.CharField(max_length=500,blank=True)
	make_id = models.CharField(max_length=500,blank=True)
	make_name = models.CharField(max_length=500,blank=True)
	model_id = models.CharField(max_length=500,blank=True)
	model_name = models.CharField(max_length=500,blank=True)

	def __str__(self):
		return self.website_name


class CarDetails(models.Model):
	website_name = models.CharField(max_length=100,blank=True)
	city = models.CharField(max_length=100,blank=True)
	car_make = models.CharField(max_length=100,blank=True)
	car_model =models.CharField(max_length=100,blank=True)
	price = models.IntegerField(blank=True)
	model_year = models.IntegerField(blank=True)
	car_title = models.CharField(max_length=500,blank=True)
	car_href = models.URLField(unique=True)
	car_image = models.URLField(max_length=500,blank=True)
	car_color = models.CharField(max_length=50,blank=True)
	is_verified = models.BooleanField(default=False)
	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(auto_now=True)
	keywords = models.CharField(max_length=500, blank=True)

	def __str__(self):
		return self.website_name


