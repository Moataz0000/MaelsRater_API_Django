from django.shortcuts import render
from rest_framework import viewsets
from .models import Meal , Rating
from .serializers import MealSerializer , RatingSerializer






# GET , POST , PUT , DELETE ==> ModelViewSet

class MealViewSets(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    
    
    
class RatingViewSets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    