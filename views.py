import json

from django.contrib import auth

from django.http import JsonResponse, HttpResponse
from django.db import IntegrityError

from .models import UserRegistration

"""
    This function registers a new user
    return: Response if registered or not
"""


def register(request):
    if request.method == "POST":

        data = json.loads(request.body)
        # username = data.get('username')

        # email = data.get('email')
        # password = data.get('password')
        # name = data.get('name')
        # address = data.get('address')
        # state = data.get('state')
        try:
            UserRegistration.objects.create_user(data.get('username'), data.get('email'), data.get('password'), name=data.get('name'), address=data.get('address'), state=data.get('state'))
            response = {"message": "Registered successfully"}
            return JsonResponse(response)
        except IntegrityError:
            return HttpResponse("User name already exists")


"""
    This function lets the user to log in 
    return: Login success or failed
"""


def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        login_name = data.get('username')
        login_password = data.get('password')
        user = auth.authenticate(username=login_name, password=login_password)
        if user is not None:
            data = {'message': 'Logged in Successfully'}
            return JsonResponse(data)
        else:
            data = {"message": "Invalid Credentials!!!"}
            return JsonResponse(data)

