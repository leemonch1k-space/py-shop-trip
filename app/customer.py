from typing import Any


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
        self.money = money
        self.car = car

    def calculate_trip_price(self, shop: Any) -> float:
        if not shop:
            return 0.0

        road_price = round(
            self.car.calculate_road_price(self.location, shop.location), 2
        )
        products_price = round(shop.buy_products_cost(**self.product_cart), 2)
        trip_price = road_price + products_price
        return round(trip_price, 2)

    def find_chippest_trip(
            self,
            shops: list[Any]
    ) -> tuple[str, Any]:
        shop_name = ""
        cheapest_trip = float("inf")
        cheapest_shop = None

        for shop in shops:
            trip_price = self.calculate_trip_price(shop)
            if trip_price < cheapest_trip:
                cheapest_trip = trip_price
                shop_name = shop.name
                cheapest_shop = shop
        return shop_name, cheapest_shop
