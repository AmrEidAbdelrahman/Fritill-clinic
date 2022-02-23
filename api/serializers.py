from rest_framework.serializers import ModelSerializer
from .models import Appointment, RescheduleRequest

class AppointmentSerializer(ModelSerializer):
	class Meta:
		model = Appointment
		fields = "__all__"
		depth = 2


class RescheduleRequestSerializer(ModelSerializer):
	class Meta:
		model = RescheduleRequest
		depth = 2
		fields = "__all__"