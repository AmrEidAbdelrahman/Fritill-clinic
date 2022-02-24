from django import forms
from .models import Appointment

from datetime import datetime

class ReserveAppointmentForm(forms.Form):
	date = forms.DateTimeField(
			input_formats=['%d/%m/%Y %H:%M'],
	        widget=forms.DateTimeInput(attrs={
	            'class': 'form-control datetimepicker-input',
	            'data-target': '#datetimepicker1'
	        })
		)



class RescheduleRequestForm(forms.Form):
	to = forms.DateTimeField(
			input_formats=['%d/%m/%Y %H:%M'],
	        widget=forms.DateTimeInput(attrs={
	            'class': 'form-control datetimepicker-input',
	            'data-target': '#datetimepicker1'
	        })
		)
	