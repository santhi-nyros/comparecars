from django.contrib import admin
from compare_cars.models import CarDetails,Car_Master_Data
# Register your models here.

class Car_Master_DataAdmin(admin.ModelAdmin):
	list_display = ('website_name', 'city_id','city_name','make_id' ,'make_name','model_id','model_name')

class CarDetailsAdmin(admin.ModelAdmin):
	list_display = ('website_name', 'city', 'car_make','car_model','price','model_year','car_title','car_href','car_image')

admin.site.register(CarDetails,CarDetailsAdmin)
admin.site.register(Car_Master_Data,Car_Master_DataAdmin)