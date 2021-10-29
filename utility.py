import jwt
from rest_framework.response import Response
from django.contrib.auth.models import models, User

def verify_token(function):
    """
    This function verifies the token to access the user id
    """
    def wrapper(self, request):
        try:
            if 'HTTP_AUTHORIZATION' not in request.META:
                response = Response({'message': 'Token not provided in the header'})
                response.status_code = 400
                return response
            decode_token = request.META.get('HTTP_AUTHORIZATION')
            decoded_token = jwt.decode(decode_token, 'secret', algorithms="HS256")
            request.data["user_id"] = decoded_token["id"]
            user = User.objects.get(id=request.data.get('user_id'))
            if user is None:
                return Response({'message': 'User not found'})
            return function(self, request)
        except Exception as e:
            return Response({'message': str(e)})
    return wrapper
