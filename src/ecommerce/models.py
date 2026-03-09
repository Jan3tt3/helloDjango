from django.db import models
from base.models import BasePublishModel
from django.contrib.auth.models import User

# Create your models here.
class ProductModel(BasePublishModel):
   
    title= models.TextField()
    price = models.FloatField()
    description= models.TextField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    color=models.TextField()
    dimensions= models.TextField()

    
    def save(self, *args, **kwargs):
        #validate_blocked_words(self_title)
        super().save(*args, **kwargs)
    
   
