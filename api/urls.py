from django.urls import path
from .views import Home, AppointmentView, RescheduleRequestView

app_name = 'api'
urlpatterns = [
		path('', Home, name='home-page'),

		path('appointments/', AppointmentView.as_view({'get':'list'}), name='appointment'),
		path('appointments/upcoming/', AppointmentView.as_view({'get':'list'}), {"filter":"upcoming"}, name='appointment-upcoming'),
		path('appointments/past/', AppointmentView.as_view({'get':'list'}), {"filter":"past"}, name='appointment-past'),
		path('appointments/reserve/', AppointmentView.as_view({'post':'create'}), name='appointment-reserve'),
		path('appointments/new/', AppointmentView.as_view({'get':'list'}), {"filter":"new"}, name='appointment-new'),

		
		# client and admin can cancel the appointment
		path('appointments/<pk>/cancel/', AppointmentView.as_view({'put':'cancel'}), name='appointment-cancel'),
		
		# ONLY ADMIN
		path('appointments/<pk>/approve/', AppointmentView.as_view({'put':'approve'}), name='appointment-approve'),
		path('appointments/<pk>/mark-as-missed/', AppointmentView.as_view({'put':'missed'}), name='appointment-missed'),
		path('appointments/<pk>/mark-as-finished/', AppointmentView.as_view({'put':'finished'}), name='appointment-finished'),

		# reschedule appointment ( ONLY CLIENTS )
		path('reschedule-request/', RescheduleRequestView.as_view({'get':'list', 'post':'create'}), name='reschedule-request'),

		# reschedule appointment ( ONLY ADMINS )
		path('reschedule-request/<pk>/', RescheduleRequestView.as_view({'get':'retrieve'}), name='reschedule-request-details'),
		path('reschedule-request/<pk>/approve/', RescheduleRequestView.as_view({'put':'approve'}), name='reschedule-request-approve'),
		path('reschedule-request/<pk>/cancel/', RescheduleRequestView.as_view({'put':'cancel'}), name='reschedule-request-cancel'),
	]