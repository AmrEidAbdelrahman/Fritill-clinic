from rest_framework import serializers
from .models import Appointment, RescheduleRequest

class AppointmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		fields = "__all__"
		depth = 2

	def create(self, validated_data):
		print("#####SAVE APPOINTMENT####")
		user =  self.context['request'].user
		appointment = Appointment(client=user, **validated_data)
		appointment.save()
		return appointment


class RescheduleRequestSerializer(serializers.ModelSerializer):
	appointment_details = serializers.SerializerMethodField()

	class Meta:
		model = RescheduleRequest
		depth = 0
		fields = "__all__"

	def get_appointment_details(self, obj):
		serializer = AppointmentSerializer(obj.appointment)
		print(serializer.data)
		return serializer.data

	
