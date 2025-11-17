from math import sqrt


class Car:
    def __init__(
        self, brand: "str", fuel_consumption: float, fuel_price: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price

    def calculate_road_price(
            self,
            point_a: list[int],
            point_b: list[int]
    ) -> float:
        distance = sqrt(
            (point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2
        )

        total_distance = distance * 2
        distance_per_fuel = total_distance / 100
        fuel_cost = distance_per_fuel * self.fuel_consumption * self.fuel_price

        return fuel_cost
