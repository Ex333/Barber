from django.db import models
from django.core.exceptions import ValidationError


class Barber(models.Model):
    name = models.CharField(max_length=64)
    bio = models.TextField(blank=True)
    age = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='barbers/')

    def __str__(self):
        return self.name


class Service(models.Model):  # ✔️ zmienione z Services
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.PositiveSmallIntegerField(help_text="Time in minutes")

    barbers = models.ManyToManyField(Barber, related_name="services")

    def __str__(self):
        return f"{self.name} - {self.price} zł"


class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE) 
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)

    customer_name = models.CharField(max_length=64)
    customer_email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.barber not in self.service.barbers.all():
            raise ValidationError("This barber does not provide this service")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['barber', 'date', 'time'],
                name='unique_booking'
            )
        ]

    def __str__(self):
        return f"{self.customer_name} - {self.service} - {self.date} {self.time}"