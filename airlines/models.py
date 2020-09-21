import math
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.validators import MinValueValidator 
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from . import constants


class Airplane(TimeStampedModel):
    airplane_id = models.PositiveIntegerField(
        verbose_name=_('ID'),
        validators=[MinValueValidator(1)],
        unique=True,
    )

    passenger_count = models.PositiveIntegerField(
        verbose_name=_('Passenger Count'),
        validators=[MinValueValidator(1)],
    )

    class Meta:
        ordering = ('airplane_id',)

    @property
    def fuel_tank_capacity(self):
        # Returns total fuel tank capacity in liters
        return constants.LITER_AMOUNT * self.airplane_id

    @property
    def fuel_consumption(self):
        # Returns fuel consumption per minute in liters
        return math.log(self.airplane_id * constants.CONSUMPTION_AMOUNT)

    @property
    def additional_fuel_consumption(self):
        # Returns additional fuel consumption per minute in liters
        return constants.FUEL_INCREASE * self.passenger_count
    
    @property
    def total_fuel_consumption(self):
        # Returns total fuel consumption per minute
        return self.fuel_consumption + self.additional_fuel_consumption
    
    def get_maximum_flight(self):
        #Returns maximum flight in minutes
        return round(self.fuel_tank_capacity / self.total_fuel_consumption)
