from silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi('Hummer', 200, 2)
my_taxi.drive(18)
print(f"{my_taxi.get_fare():.2f}")
print(my_taxi)
