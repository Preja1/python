from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product (models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(null=True,blank=True,unique=True)#45 char
    market_price=models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    actual_price=models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    short_description=models.CharField(max_length=500)
    description=models.TextField()

    def save(self,*args,**kwargs):#reference self:afnai class refernce garxa self la 
        #variable haru lai declare garxa args la ,keyword args lai declare garxa kwags la
        if not self.slug:
            self.slug=slugify(self.name)[:45]
        super().save(*args,**kwargs)#parent class ko implementation garako ho 

    def __str__(self):
        return self.name
