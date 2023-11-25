from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator , MaxValueValidator # Return Msg


# uuid 


# Meal Model 
class Meal(models.Model):
    title = models.CharField(max_length=50)
    descraption = models.TextField(max_length=250)
    image = models.ImageField(upload_to='photos/meal/')
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    
    # Return Object Title 
    def __str__(self):
        return self.title
    
    
    
    
    
    
# Rating Model     
class Rating(models.Model):
    meal = models.ForeignKey(Meal , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    
    
    # Function Is Retutn meal object 
    # def __str__(self):
    #     return self.meal
    
    
    # This class to don't user to give rate on meal two rete 
    class Meta:
        unique_together = (('user' , 'meal'),)
        index_together = (('user' , 'meal'),)
    
    
    
    
    
    
    
    
    