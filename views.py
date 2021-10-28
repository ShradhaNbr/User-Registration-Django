import jwt
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from .models import Notes
from .serializer import NotesSerializer
from rest_framework.views import APIView
import jwt
from user.views import RegisterLogin


# Create your views here.


class NoteList(APIView):

    def post(self, request):
        """
        This function creates a new note
        """
        decode_token = request.META.get('HTTP_AUTHORIZATION')
        decoded_token = jwt.decode(decode_token, 'secret', algorithms="HS256")
        notes_data = request.data
        notes_data["user_id"] = decoded_token["id"]
        try:
            serializer = NotesSerializer(data=notes_data)
            if serializer.is_valid():
                serializer.save()
                response = {"message": "Notes added successfully"}
                return Response(response)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                "message": "Invalid data"})

    def get(self, request):

        decode_token = request.META.get('HTTP_AUTHORIZATION')
        decoded_token = jwt.decode(decode_token, 'secret', algorithms="HS256")
        user_id = decoded_token["id"]
        try:
            serializer = NotesSerializer(Notes.objects.filter(user_id=user_id), many=True)
            notesdata = {
                "message": "Notes for user",
                "data": serializer.data
            }
            return Response(notesdata)
        except Exception:
            return Response({
                "message": "user not found"})

    def put(self, request):

        """
        This function updates particular note when id is passed
        """
        decode_token = request.META.get('HTTP_AUTHORIZATION')
        decoded_token = jwt.decode(decode_token, 'secret', algorithms="HS256")
        notes_data = request.data
        notes_data["user_id"] = decoded_token["id"]
        try:
            note = Notes.objects.get(id=request.data["id"])
            serializer = NotesSerializer(note, data=notes_data)
            if serializer.is_valid():
                serializer.save()
                response = {"message": "Notes added successfully"}
                return Response(response)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                "message": "id not found"})

    def delete(self, request):
        """
        This function deletes particular notes when id is passed
        """
        decode_token = request.META.get('HTTP_AUTHORIZATION')
        decoded_token = jwt.decode(decode_token, 'secret', algorithms="HS256")
        notes_data = request.data
        notes_data["user_id"] = decoded_token["id"]
        try:
            note = Notes.objects.get(id=request.data["id"])
            note.delete()
            return Response({"message": "Deleted successfully"})
        except Exception:
            return Response({
                "message": "id not found"})
