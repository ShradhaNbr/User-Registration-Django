import json

from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer


class RegisterView(APIView):

    def post(self, request):
        """
        This function registers the user
        return: user registered or not
        """
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = {"message": "Registered successfully"}
                return Response(response)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({"message": "User name already exists"})
        except Exception as e:
            value = {'Exception', 'Value does not exists'}
            return Response(value)


class RegisterLogin(APIView):
    def post(self, request):
        """
               This function lets the user login
               return: user success or not
               """
        try :
            data = json.loads(request.body)
            user = authenticate(username=data.get('username'), password=data.get('password'))
            if user is not None:
                data = {'message': 'Logged in Successfully'}
                return Response(data)
            else:
                data = {"message": "Invalid Credentials!!!"}
                return Response(data)
        except Exception as e:
            value = {'Exception', 'Value does not exists'}
            return Response(value)


