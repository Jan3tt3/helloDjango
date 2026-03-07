from django.db import models
from base.models import BasePublishModel

# Create your models here.
class ProductModel(BasePublishModel):
   
    title= models.TextField()
    price = models.FloatField()
    description= models.TextField()
    seller= models.TextField()
    color=models.TextField()
    dimensions= models.TextField()

    
    def save(self, *args, **kwargs):
        #validate_blocked_words(self_title)
        super().save(*args, **kwargs)
    
   
