from abc import ABC, abstractmethod


class Parcel(ABC):
    """Abstract Parcel class to define interface"""

    @abstractmethod
    def calc_tariff(self) -> float:
        """Returns delivery tariff for this parcel type"""


class Envelope(Parcel):
    def calc_tariff(self) -> float:
        return 50


class Box(Parcel):
    def calc_tariff(self) -> float:
        return 250


class Tovarnyak(Parcel):
    def calc_tariff(self) -> float:
        return 100500
