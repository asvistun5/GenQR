from django.db import models
from django.core.exceptions import ValidationError
import re

#def validate_size(value):
#    if not re.match(r'^\d+x\d+$', value):
#        raise ValidationError('Size must be in format 400x400.')

# Create your models here.
class QR(models.Model):
    
    url = models.URLField(max_length=200)
    #size = models.CharField(max_length=10, validators=[validate_size])
    site = models.CharField(max_length=20, default="Youtube")
    color = models.CharField(max_length=20, default="black")
    #bg_color = models.CharField(max_length=20, default="#eceff7")
    shape = models.CharField(max_length=20, default="квадратний")
    img = models.ImageField(upload_to='qr/img')

    date = models.DateField(auto_now=True)


    def __str__(self):
        return f'{self.url}'