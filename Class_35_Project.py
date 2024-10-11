class Vehicle:
   def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

def fare(self):
    return self.seating_capacity * 100

class Bus(Vehicle):

    def fare(self):
    base_fare = super().fare()
    maintenance_charge = 0.1 * base_fare
    total_fare = base_fare + maintenance_charge
    return total_fare

bus = Bus(seating_capacity=50)
print("Total fare for the bus:", bus.fare())