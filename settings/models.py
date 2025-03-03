from django.db import models
from datetime import date

class Card(models.Model):
    num = models.IntegerField()
    end = models.DateField()
    cvv = models.CharField(max_length=4)

    def __repr__(self):
        return f'{self.num}'