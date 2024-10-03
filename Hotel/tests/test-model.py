

from django.test import TestCase
from Reservas.models import Rooms, Services, Booking, Booking_Marriage, Booking_Family 

class RoomsModelTest(TestCase):
    def setUp(self):
        Rooms.objects.create(room_type="Single Room", price=100.00)
        Rooms.objects.create(room_type="Marriage Room", price=200.00)

    def test_room_str(self):
        room = Rooms.objects.get(room_type="Single Room")
        self.assertEqual(str(room), "Single Room")

class ServicesModelTest(TestCase):
    def setUp(self):
        Services.objects.create(services_type="Breakfast", price=10.00)
        Services.objects.create(services_type="Lunch", price=15.00)

    def test_services_str(self):
        service = Services.objects.get(services_type="Breakfast")
        self.assertEqual(str(service), "Breakfast")

class BookingModelTest(TestCase):
    def setUp(self):
        room = Rooms.objects.create(room_type="Family Room", price=150.00)
        Services.objects.create(services_type="Dinner", price=20.00)
        Booking.objects.create(name="John", last_name="Doe", arrival_date="2024-10-01", exit_date="2024-10-05", type_of_room=room)

    def test_booking_str(self):
        booking = Booking.objects.get(name="John")
        self.assertEqual(booking.name, "John")
        self.assertEqual(booking.last_name, "Doe")

class BookingMarriageModelTest(TestCase):
    def setUp(self):
        room = Rooms.objects.create(room_type="Marriage Room", price=200.00)
        Booking_Marriage.objects.create(full_name_spouse1="Jane Doe", full_name_spouse2="John Smith", arrival_date="2024-10-01", exit_date="2024-10-05", type_of_room=room)

    def test_booking_marriage_str(self):
        booking_marriage = Booking_Marriage.objects.get(full_name_spouse1="Jane Doe")
        self.assertEqual(booking_marriage.full_name_spouse1, "Jane Doe")

class BookingFamilyModelTest(TestCase):
    def setUp(self):
        room = Rooms.objects.create(room_type="Family Room", price=150.00)
        Booking_Family.objects.create(full_name="The Smith Family", arrival_date="2024-10-01", exit_date="2024-10-05", type_of_room=room)

    def test_booking_family_str(self):
        booking_family = Booking_Family.objects.get(full_name="The Smith Family")
        self.assertEqual(booking_family.full_name, "The Smith Family")
