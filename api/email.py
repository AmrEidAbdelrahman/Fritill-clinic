from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def send_reminder_email(name, email, appointment):
	context = {
		'name': name,
		'email': email,
		'appointment':appointment
	}
	email_subject = 'Appointment Reminder'
	email_body = render_to_string('email_body.txt', context)

	email = EmailMessage(
		email_subject, email_body,
		setting.DEFAULT_FROM_EMAIL, [email,]
	)

	return email.send(fail_silently=False)