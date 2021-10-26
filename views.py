from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from .models import Notes
from .serializer import NotesSerializer
from rest_framework.views import APIView


# Create your views here.


class NoteList(APIView):

    def post(self, request):
        """
        This function creates a new note
        """
        try:
            serializer = NotesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = {"message": "Notes added successfully"}
                return Response(response)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response("Invalid data")

    def get(self, request):
        """
        This function gets particular note when id is passed
        """
        try:
            serializer = NotesSerializer(Notes.objects.filter(user_id=request.data["user_id"]), many=True)
            return Response(serializer.data)
        except Exception:
            return Response("User not found")

    def put(self, request):
        """
        This function updates particular note when id is passed
        """
        try:
            note = Notes.objects.get(id=request.data["id"])
            serializer = NotesSerializer(note, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "updated successfully",
                        "data": serializer.data
                    })
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response("id not found")

    def delete(self, request):
        """
        This function deletes particular notes when id is passed
        """
        try:
            note = Notes.objects.get(id=request.data["id"])
            note.delete()
            return Response({"message": "Deleted successfully"})
        except Exception:
            return Response("id not found")
