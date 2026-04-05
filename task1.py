from abc import abstractmethod, ABC
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class Vehicle(ABC):

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):

    def start_engine(self) -> None:
        logging.info("%s %s: Двигун запущено", self.make, self.model)


class Motorcycle(Vehicle):

    def start_engine(self) -> None:
        logging.info("%s %s: Мотор заведено", self.make, self.model)


class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} (US spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} (US spec)")


class EUVehicleFactory(VehicleFactory):

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} (EU Spec)")


# Використання


def client_code():
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    us_car = us_factory.create_car("Ford Mustang", "2021")
    us_car.start_engine()
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "2021")
    us_motorcycle.start_engine()

    eu_car = eu_factory.create_car("Volkswagen Golf", "2021")
    eu_car.start_engine()
    eu_motorcycle = eu_factory.create_motorcycle("BMW R1200", "2021")
    eu_motorcycle.start_engine()


if __name__ == "__main__":
    client_code()
