from django.contrib import admin
from .models import Barber, Service, Booking

# Register your models here.
@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ("name", "age")
    search_fields = ('name', )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "duration")
    filter_horizontal = ("barbers",)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("customer_name","service", "barber", "date", "time")
    list_filter = ("date", "barber")
    search_fields = ("customer_name", "costomer_email")


