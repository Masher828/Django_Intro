from django.db import models

# Create your models here.
class user_details(models.Model):
    first_name = models.CharField(max_length =70)
    last_name = models.CharField(max_length = 70)
    email = models.EmailField(max_length=120)

    def __str__(self):
        return str(self.email)
