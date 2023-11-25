from .models import Meal , Rating
from rest_framework import serializers



# Return Json Format 


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id' , 'title' , 'descraption' , 'image' , 'price']
        
        
        
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id' , 'stars' , 'user' , 'meal']
        
                