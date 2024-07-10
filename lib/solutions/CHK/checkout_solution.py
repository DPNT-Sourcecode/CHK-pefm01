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
    products = list(skus)  # converting to the list to easier operate on it
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
    return apply_promotions(basket, bill)


def apply_promotions(basket: dict, bill: int) -> int:
    actual_promotions = json.loads(promotions)  # loading current promotions
    for item in basket:
        for promo in actual_promotions:
            if promo['sku'] == item:  # if current object is in promotion we need to apply the discount
                bill -= (basket[item] % promo['amount']) * promo['discount']
                break
    return bill


if __name__ == '__main__':
    checkout("AABCD")

