import json
from django.test import Client, TestCase
from django.test.client import RequestFactory
from rest_framework import status
from rest_framework.reverse import reverse
from airlines.models import Airplane
from . import serializers

class AirlineTestCase(TestCase):
    client = Client()
    airplane_list = [
        {
            'id': 5,
            'passenger': 834,
        },
        {
            'id': 2,
            'passenger': 500,
        }
    ]

    def setUp(self):
        for airplane in self.airplane_list:
            Airplane.objects.create(
                airplane_id=airplane['id'],
                passenger_count=airplane['passenger']
            )
    
    def test_get_all_airplanes(self):
        # Get API Response
        response = self.client.get(reverse('airplane_list'))

        # Get list of airplanes from database
        airplanes = Airplane.objects.all()
        serializer = serializers.AirplaneSerializer(airplanes, many=True, context={'request': RequestFactory().get('/')})
        self.assertEqual(response.data, serializer.data)
    
    def test_create_valid_airplane(self):
        # Valid data (ID is unique and a postive integer, Passenger count is positive integer)
        airplane_dict = [
            {
                'airplane_id': 9,
                'passenger_count': 500,
            }
        ]

        response = self.client.post(
            reverse('airplane_list'),
            data=json.dumps(airplane_dict),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_airplane(self):
        # Invalid data (ID is existing, Passenger count is negative integer)
        airplane_dict = [
            {
                'airplane_id': 5,
                'passenger_count': -5,
            }
        ]

        response = self.client.post(
            reverse('airplane_list'),
            data=json.dumps(airplane_dict),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
