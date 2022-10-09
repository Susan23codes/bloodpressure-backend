from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsOwner
from rest_framework import generics
from api.models import Reading
from .serializers import ReadingSerializer

# C# View Readings GET/ Add Reading POST ListCreate handles GET and POST
class ReadingAddListView(generics.ListCreateAPIView):
    serializer_class = ReadingSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Reading.objects.all().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    



