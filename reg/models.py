from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, null=False)
    surname = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)

    is_auth = models.BooleanField(default=False)

    def __repr__(self):
        return f'{self.username}'