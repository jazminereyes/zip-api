from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from airlines.models import Airplane
from . import serializers

class AirplaneListAPIView(generics.GenericAPIView):
    queryset = Airplane.objects.all()
    serializer_class = serializers.AirplaneSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """ POST method to allow input of more than 1 airplanes
            JSON Format should be:
            [
                {
                    "airplane_id": 1,
                    "passenger_count": 500
                }
            ]
        """

        serializer = serializers.AirplaneSerializer(
            data=request.data,
            many=True,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AirplaneDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = serializers.AirplaneSerializer
