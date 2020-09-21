from django.test import TestCase
from .models import Airplane

class AirplaneTestCase(TestCase):
    airplane_dict = {
        'id': 5,
        'passenger': 834,
        'fuel_capacity': 1000,
        'fuel_consumption': 1.3862943611198906,
        'additional_consumption': 1.668,
        'maximum_minutes_to_fly': 327,
    }

    def setUp(self):
        Airplane.objects.create(
            airplane_id=self.airplane_dict['id'],
            passenger_count=self.airplane_dict['passenger']
        )
    
    def get_airplane(self):
        return Airplane.objects.get(airplane_id=self.airplane_dict['id'])

    def test_fuel_tank_capacity_value(self):
        airplane = self.get_airplane()
        self.assertEqual(airplane.fuel_tank_capacity, self.airplane_dict['fuel_capacity'])
    
    def test_fuel_consumption_per_minute_value(self):
        airplane = self.get_airplane()
        self.assertEqual(airplane.fuel_consumption, self.airplane_dict['fuel_consumption'])

    def test_additional_consumption_per_minute(self):
        airplane = self.get_airplane()
        self.assertEqual(airplane.additional_fuel_consumption, self.airplane_dict['additional_consumption'])

    def test_total_consumption_per_minute_value(self):
        airplane = self.get_airplane()
        self.assertEqual(airplane.total_fuel_consumption, self.airplane_dict['fuel_consumption'] + self.airplane_dict['additional_consumption'])
        
    def test_maximum_minutes_to_fly_value(self):
        airplane = self.get_airplane()
        self.assertEqual(airplane.get_maximum_flight(), self.airplane_dict['maximum_minutes_to_fly'])
