from django.shortcuts import render
from django.views.generic.list import ListView

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions

from .serializers import AppointmentSerializer, RescheduleRequestSerializer
from .models import Appointment, RescheduleRequest

from datetime import datetime


class AppointmentView(ModelViewSet):
    """
    API endpoint to handle appointments.
    """
    
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        filter =  self.kwargs.get('filter')
        if filter == "upcoming":
            return Appointment.objects.all().filter(date__gt=datetime.now()).order_by('date')
        elif filter == "past":
            return Appointment.objects.all().filter(date__lt=datetime.now()).order_by('date')
        else:
            return Appointment.objects.all().order_by('date')
            
    
class RescheduleRequestView(ModelViewSet):
    """
    API endpoint to handle reschedule requests.
    """
    queryset = RescheduleRequest.objects.all().order_by('to')
    serializer_class = RescheduleRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['put'], name="reschedule-approve")
    def approve(self, request, pk=None):
    	req = RescheduleRequest.objects.filter(pk=pk).update(approved=True, refused=False)
    	return Response(status=200)


    @action(detail=True, methods=['put'], name='reschedule-cancel')
    def cancel(self, request, pk=None):
    	req = RescheduleRequest.objects.filter(pk=pk).update(approved=False, refused=True)
    	return Response(status=200)


class Home(ListView):
	model = Appointment
	