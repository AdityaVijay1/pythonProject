from CP1404_Practicals.prac_09.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(1, 100) < float(self.reliability):
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
