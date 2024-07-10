# noinspection PyUnusedLocal
# skus = unicode string
import json

sku_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

promotions = """
[
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
"""


def checkout(skus: str) -> int:
    products = list(skus)  # converting to the list to easier operate on it
    basket = {}
    for product in products:
        if product in basket.keys():
            basket[product] += 1  # product exists in dic, incrementing
        else:
            basket[product] = 1  # product does not exists, adding
    return count_basket(basket)


def count_basket(basket: dict) -> int:
    bill = 0
    for item in basket:
        try:
            bill += sku_prices[item] * basket[item]  # increasing bill for product_price * ammount in baskter
        except:
            print(f"product that you added to the list: {item} is not for sale. Please put it away.")
    return apply_promotions(basket, bill)


def apply_promotions(basket: dict, bill: int) -> int:
    actual_promotions = json.loads(promotions)  # loading current promotions
    for item in basket:
        for promo in actual_promotions:
            if promo['sku'] == item:  # if current object is in promotion we need to apply the discount
                # if int is more than 0, it will apply promo to the basket
                bill -= int(basket[item] / promo['amount']) * promo['discount']
                break
    return bill



