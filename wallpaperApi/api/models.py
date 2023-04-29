from django.db import models

# Create your models here.
class Image(models.Model):
    fname = models.CharField(max_length=100)
    image =models.ImageField(upload_to='images/')
    publish = models.BooleanField(default=True)
    def __str__(self):
        return self.fname
    
class CategoryList(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    iconName =models.CharField(max_length=100,default='godIcon')
    fname =models.CharField(max_length=100)

    def __str__(self):
        return self.fname
