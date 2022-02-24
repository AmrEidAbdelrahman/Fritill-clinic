from django.shortcuts import render
from django.views.generic.list import ListView

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions

from .serializers import AppointmentSerializer, RescheduleRequestSerializer
from .models import Appointment, RescheduleRequest
from .forms import ReserveAppointmentForm, RescheduleRequestForm

from datetime import datetime


def Home(request):
    return render(request, 'api/home.html')


def reserve_appointment(request):
    if request.method == 'GET':
        form = ReserveAppointmentForm()
    return render(request, 'api/reserve_appointment.html', {'form': form})


class AppointmentView(ModelViewSet):
    """
    API endpoint to handle appointments.
    """
    
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        filter =  self.kwargs.get('filter')
        user = self.request.user
        queryset = Appointment.objects.all()
        if not user.is_staff:
            print('#$#$#$#$', user)
            queryset = queryset.filter(client=user)
            print(queryset)
        if filter == "upcoming":
            return queryset.filter(approved=True, date__gt=datetime.now()).order_by('date')
        elif filter == "past":
            return queryset.filter(date__lt=datetime.now()).order_by('date')
        elif filter == "new":
            print("#####$$##### ")
            return queryset.filter(approved=False, cancel=False, date__gt=datetime.now()).order_by('date')
        else:
            return queryset.order_by('date')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if self.kwargs.get('api') == True:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        print(queryset)
        context = {
            'response': queryset,
            'filter': self.kwargs.get('filter')
        }
        return render(request, 'api/appointment.html', context)

    # for clients and admins
    @action(detail=True, methods=['put'], name="appointment-cancel")
    def cancel(self, request, pk=None):
        print("####RR######")
        req = Appointment.objects.filter(pk=pk).update(cancel=True)
        return Response(status=200)


    @action(detail=True, methods=['put'], name="appointment-cancel")
    def approve(self, request, pk=None):
        print("####aprove######")
        req = Appointment.objects.filter(pk=pk).update(approved=True)
        return Response(status=200)

    @action(detail=True, methods=['put'], name="appointment-cancel")
    def missed(self, request, pk=None):
        print("####missed######")
        req = Appointment.objects.filter(pk=pk).update(missed=True)
        return Response(status=200)

    @action(detail=True, methods=['put'], name="appointment-cancel")
    def finished(self, request, pk=None):
        print("####finished######")
        req = Appointment.objects.filter(pk=pk).update(finished=True)
        return Response(status=200)
            
    
class RescheduleRequestView(ModelViewSet):
    """
    API endpoint to handle reschedule requests.
    """
    #queryset = RescheduleRequest.objects.all().order_by('to')
    serializer_class = RescheduleRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = RescheduleRequest.objects.all().order_by('to')
        if not user.is_staff:
            print('#$#$#$#$', user)
            queryset = queryset.filter(appointment__client=user)
            print(queryset)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if self.kwargs.get('api') == True:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        print(queryset)
        context = {
            'response': queryset,
            
        }
        return render(request, 'api/reschedule_requests.html', context)

    @action(detail=True, methods=['put'], name="reschedule-approve")
    def approve(self, request, pk=None):
        req = RescheduleRequest.objects.filter(pk=pk).update(approved=True, refused=False)
        # TODO: change the appointment date
        return Response(status=200)


    @action(detail=True, methods=['put'], name='reschedule-cancel')
    def cancel(self, request, pk=None):
        req = RescheduleRequest.objects.filter(pk=pk).update(approved=False, refused=True)
        return Response(status=200)


def reschedule_request(request, pk):
    if request.method == 'GET':
        form = RescheduleRequestForm()
        appointment = Appointment.objects.get(pk=pk)
        context = {
            'form':form,
            'appointment': appointment

        }
    return render(request, 'api/reschedule_requests.html', context)