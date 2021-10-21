import json
from django.http import JsonResponse
from .models import UserRegistration

"""
    This function registers a new user
            :return: Response if registered or not
"""


def register_request(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')
        username = data.get('username')
        password = data.get('password')
        if UserRegistration.objects.filter(username=username).exists():
            response = {"message": "Username already exists"}
            return JsonResponse(response)
        else:
            user = UserRegistration(name=name, username=username, password=password)
            user.save()
            response = {"message": "Registered successfully"}
        return JsonResponse(response)


"""
    This function lets the user to log in 
        :return: Login success or failed
"""


def login(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            login_name = data.get('username')
            login_password = data.get('password')
            if UserRegistration.objects.filter(username=login_name, password=login_password).exists():
                data = {'message': 'Logged in Successfully'}
                return JsonResponse(data)
            else:
                data = {"message": "Invalid Credentials!!!"}
                return JsonResponse(data)
    except Exception as e:
        raise e
