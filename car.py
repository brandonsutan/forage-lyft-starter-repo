from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass

class Engine(Car):
    def __init__(self, last_service_date, engine_type, horsepower, displacement, fuel_type):
        super().__init__(last_service_date)
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.displacement = displacement
        self.fuel_type = fuel_type

    def needs_service(self):
        # Add your logic to determine if the engine needs service based on last_service_date and other factors.
        pass

class Transmission(Car):
    def __init__(self, last_service_date, transmission_type, gears):
        super().__init__(last_service_date)
        self.transmission_type = transmission_type
        self.gears = gears

    def needs_service(self):
        # Add your logic to determine if the transmission needs service based on last_service_date and other factors.
        pass

class Battery(Car):
    def __init__(self, last_service_date, brand, capacity):
        super().__init__(last_service_date)
        self.brand = brand
        self.capacity = capacity

    def needs_service(self):
        # Add your logic to determine if the battery needs service based on last_service_date and other factors.
        pass

class Tires(Car):
    def __init__(self, last_service_date, brand, size):
        super().__init__(last_service_date)
        self.brand = brand
        self.size = size

    def needs_service(self):
        # Add your logic to determine if the tires need service based on last_service_date and other factors.
        pass
