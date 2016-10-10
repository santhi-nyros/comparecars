from rest_framework import serializers

from .models import Car_Master_Data,CarDetails




class CompareCarSerializer(serializers.ModelSerializer):
	# makes = GroupSerializer(many=True, read_only=True)
    
    class Meta:
        model = CarDetails
        fields = ('id', 'website_name', 'city', 'car_make', 'car_model','price','model_year','car_title','car_href','car_image','car_color','created')
        lookup_field = 'car_make'


class MaterCarSerializer(serializers.ModelSerializer):
	# makes = GroupSerializer(many=True, read_only=True)
    
    class Meta:
        model = Car_Master_Data
        fields = ('id','city_name','make_name','model_name')
        lookup_field = 'make_name'


