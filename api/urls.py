from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('maels' , views.MealViewSets),
router.register('ratings' , views.RatingViewSets)




urlpatterns = [
    path('' , include(router.urls)),
]

