from django.db import models

class Barber(models.Model):
    name = models.CharField(max_length=64)
    bio = models.TextField(blank=True)
    age = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='barbers/')

    def __str__(self):
        return self.name
    
class Services(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places= 2 )
    duration = models.PositiveSmallIntegerField(help_text="Time in minutes")

    barbers = models.ManyToManyField(Barber, related_name="services")

    def __str__(self):
        return f"{self.name} - {self.price} zł"
