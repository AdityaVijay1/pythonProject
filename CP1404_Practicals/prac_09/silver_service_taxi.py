from taxi import Taxi


class SilverServiceTaxi(Taxi):
    price_per_km = Taxi.price_per_km
    flagfall = 4.50

    def __init__(self, fuel,name, fanciness):
        super().__init__(name,fuel)
        self.fanciness = fanciness
        self.current_fare_distance = 0
        self.price_per_km = self.price_per_km * self.fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        return super().get_fare() + self.flagfall
