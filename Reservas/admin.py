from django.contrib import admin
from .models import Booking, Booking_Family, Booking_Marriage, Services, Rooms


# Register your models here.
admin.register(Rooms)
admin.register(Services)
admin.register(Booking)
admin.register(Booking_Marriage)
admin.register(Booking_Family)

