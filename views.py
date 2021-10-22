import json

from django.contrib import auth

from django.contrib.auth.models import User
from django.http import JsonResponse

"""
    This function registers a new user
            :return: Response if registered or not
"""


def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        user = User.objects.create_user(username, email, password)
        user.save()
        response = {"message": "Registered successfully"}
        return JsonResponse(response)


"""
    This function lets the user to log in 
        :return: Login success or failed
"""


def login_user(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            login_name = data.get('username')
            login_password = data.get('password')
            user = auth.authenticate(username=login_name, password=login_password)
            if user is not None:
                auth.login(request, user)
                data = {'message': 'Logged in Successfully'}
                return JsonResponse(data)
            else:
                data = {"message": "Invalid Credentials!!!"}
                return JsonResponse(data)
    except Exception:
        raise ValueError
