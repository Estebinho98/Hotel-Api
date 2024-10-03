from django.db import models

# Create your models here.


class Rooms(models.Model):
    room_type = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self) -> str:
        return self.room_type


class Services(models.Model):
    services_type = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self) -> str:
        return self.services_type

class Booking(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    arrival_date = models.DateField()
    exit_date = models.DateField()
    type_of_room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    services_required = models.ManyToManyField(Services)

class Booking_Marriage(models.Model):
    full_name_spouse1 = models.CharField(max_length=200)
    full_name_spouse2 = models.CharField(max_length=200)
    arrival_date = models.DateField()
    exit_date = models.DateField()
    type_of_room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    services_required = models.ManyToManyField(Services)

    

class Booking_Family(models.Model):
    full_name = models.CharField(max_length=200)
    arrival_date = models.DateField()
    exit_date = models.DateField()
    type_of_room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    services_required = models.ManyToManyField(Services)

    

