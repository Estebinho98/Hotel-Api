

from django.test import TestCase
from django.urls import reverse
from Reservas.models import Rooms, Services, Booking

class BookingViewTest(TestCase):
    def setUp(self):
        self.room = Rooms.objects.create(room_type="Single Room", price=100.00)
        self.service = Services.objects.create(services_type="Breakfast", price=10.00)

    def test_booking_create_view(self):
        response = self.client.post(reverse('booking-create'), {
            'name': 'John',
            'last_name': 'Doe',
            'arrival_date': '2024-10-01',
            'exit_date': '2024-10-05',
            'type_of_room': self.room.id,
            'services_required': self.service.id,
        })
        self.assertEqual(response.status_code, 201)  # Cambia el código según el resultado esperado

    def test_booking_list_view(self):
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'your_template_name.html')  # Cambia el nombre de la plantilla
        self.assertContains(response, 'John')

    def test_booking_detail_view(self):
        booking = Booking.objects.create(
            name='John',
            last_name='Doe',
            arrival_date='2024-10-01',
            exit_date='2024-10-05',
            type_of_room=self.room,
            services_required=self.service
        )
        response = self.client.get(reverse('booking-detail', args=[booking.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')
