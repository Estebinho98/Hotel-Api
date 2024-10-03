from rest_framework import serializers
from .models import Booking, Booking_Family, Booking_Marriage, Services, Rooms
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'groups']


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'
        

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
        

class BookingSerializer(serializers.ModelSerializer):
    services_required = ServicesSerializer(many=True, read_only=True)
    services_required_ids = serializers.PrimaryKeyRelatedField(queryset=Services.objects.all(), many=True, write_only=True, source='services_required')

    class Meta:
        model = Booking
        fields = ['id', 'name','last_name', 'arrival_date', 'exit_date', 'type_of_room', 'services_required', 'services_required_ids']

class Booking_MarriageSerializer(serializers.ModelSerializer):
    services_required = ServicesSerializer(many=True, read_only=True)
    services_required_ids = serializers.PrimaryKeyRelatedField(queryset=Services.objects.all(), many=True, write_only=True, source='services_required')
    class Meta:
        model = Booking_Marriage
        fields = ['id', 'full_name_spouse1','full_name_spouse2' 'arrival_date', 'exit_date', 'type_of_room', 'services_required', 'services_required_ids']

class Booking_FamilySerializer(serializers.ModelSerializer):
    services_required = ServicesSerializer(many=True, read_only=True)
    services_required_ids = serializers.PrimaryKeyRelatedField(queryset=Services.objects.all(), many=True, write_only=True, source='services_required')
    class Meta:
        model = Booking_Family
        fields = ['id', 'full_name', 'arrival_date', 'exit_date', 'type_of_room', 'services_required', 'services_required_ids']