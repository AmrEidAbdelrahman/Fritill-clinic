from django.shortcuts import render
from django.shortcuts import reverse
from django.views import View

import os
import requests
# Create your views here.


class Home(View):

	def get(self, request):
		url = "http://127.0.0.1:8000" + reverse('appointment')
		print(url)
		response = requests.get(url) 
		print(response)
		context = {
			response: response
		}
		return render(request, 'frontend/home.html', context)
