# noinspection PyUnusedLocal
# skus = unicode string
import json

sku_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

promotions = [
    {
        "sku": "A",
        "amount": 3,
        "discount": 20
    },
    {
        "sku": "B",
        "amount": 2,
        "discount": 15
    }
]


def checkout(skus: str) -> int:
    products = list(str)  # converting to the list to easier operate on it
    basket = {}
    for product in products:
        if product in basket.keys():
            basket[product] += 1
        else:
            basket[product] = 1


def count_basket(basket: dict) -> int:
    bill = 0
    for item in basket:
        bill += sku_prices[item] * basket[item]


def apply_promotions(basket: dict, bill: int) -> int:
    for item in basket:
        if pro
