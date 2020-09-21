from rest_framework import serializers
from airlines.models import Airplane

class AirplaneSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='airplane_detail')
    maximum_flight = serializers.SerializerMethodField()

    class Meta:
        model = Airplane
        fields = [
            'url',
            'airplane_id',
            'passenger_count',
            'total_fuel_consumption',
            'maximum_flight'
        ]

    def get_maximum_flight(self, obj):
        return obj.get_maximum_flight()