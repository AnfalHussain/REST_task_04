from rest_framework import serializers

from .models import Flight, Booking
from django.contrib.auth.models import User






class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = ['username', 'password', 'last_name', 'first_name']

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		lastname = validated_data['last_name']
		firstname = validated_data['first_name']


		new_user = User(username=username, last_name = lastname, first_name = firstname )
		new_user.set_password(password)
		new_user.save()
		return validated_data



class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']

