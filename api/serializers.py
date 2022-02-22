from rest_framework.serializers import ModelSerializer
from .models import Appointment, RescheduleRequest

class AppointmentSerializer(ModelSerializer):
	class Meta:
		model = Appointment
		fields = "__all__"


class RescheduleRequestSerializer(ModelSerializer):
	class Meta:
		model = RescheduleRequest
		fields = "__all__"