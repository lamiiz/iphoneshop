from django.db import models

# Create your models here.


class Contact(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=54)
    PhoneNumber=models.CharField(max_length=10)
    message=models.CharField(max_length=250)

    def __str__(self):
        return self.Name