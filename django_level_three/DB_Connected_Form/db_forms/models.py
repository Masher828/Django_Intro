from django.db import models

# Create your models here.
class users(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length =20)
    email = models.CharField(max_length = 40,unique =True)

    def __str__(self):
        return str(self.email)
