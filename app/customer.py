from typing import Any, Tuple


class Customer:
    def __init__(
        self, name: str,
        product_cart: dict,
        location: list[int],
        money: int,
        car: Any
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location
        self.money = money
        self.car = car

    def calculate_trip_price(
            self,
            shop: Any,
            mode: int = 1
    ) -> Tuple[float, list] | float:
        if not shop:
            return 0.0

        road_args = self.car.calculate_road_price(self.location, shop.location)

        road_price = road_args[0]
        new_location = road_args[1]

        products_price = shop.buy_products_cost(**self.product_cart)
        trip_price = road_price + products_price

        if mode == 0:
            return round(trip_price, 2)

        return round(trip_price, 2), new_location

    def find_cheapest_trip(
            self,
            shops: list[Any]
    ) -> list[Any]:
        shop_name = ""
        cheapest_trip = float("inf")
        cheapest_shop = None
        money_spend = float("inf")
        new_location = []

        for shop in shops:
            trip_price, new_location = self.calculate_trip_price(shop)
            if trip_price < cheapest_trip:
                cheapest_trip = trip_price
                shop_name = shop.name
                cheapest_shop = shop
                money_spend = trip_price
        self.location = new_location
        return [shop_name, cheapest_shop, money_spend]
