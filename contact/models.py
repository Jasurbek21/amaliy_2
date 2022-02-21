from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.first_name
