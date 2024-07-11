# noinspection PyUnusedLocal
# skus = unicode string
import json

sku_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10
}

promotions = """
[
    {
        "sku": "A",
        "amount": 5,
        "discount": 50
    },
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

free_products = """
[
    {
        "sku": "E",
        "amount": 2,
        "free_product": "B"
    },
    {
        "sku": "F",
        "amount": 2,
        "free_product": "F"
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
        except KeyError:
            return (-1)
    return apply_promotions(basket, bill)


def apply_promotions(basket: dict, bill: int) -> int:
    actual_promotions = json.loads(promotions)  # loading current promotions
    free_promo = json.loads(free_products)  # loading free products
    basket_for_discounts = basket
    for item in basket:
        bill = apply_free_products(free_promo, item, bill, basket)
    for item in basket:
        bill, basket_for_discounts = apply_discounts(actual_promotions, item, bill, basket_for_discounts)
    return bill


def apply_discounts(actual_promotions: json, item: object, bill: int, basket_for_discounts):
    for promo in actual_promotions:
        if promo['sku'] == item:  # if current object is in promotion we need to apply the discount
            # if int is more than 0, it will apply promo to the basket
            promo_counter = int(basket_for_discounts[item] / promo['amount'])
            if promo_counter > 0:
                basket_for_discounts[item] -= promo['amount'] * promo_counter
                bill -= promo_counter * promo['discount']

    return bill, basket_for_discounts


def apply_free_products(free_promo: json, item: object, bill: int, basket: dict) -> int:
    for promo in free_promo:
        if promo['sku'] == item:  # if current object is in promotion we need to apply the discount
            promo_counter = int(basket[item] / promo['amount'])  # number of promotion that needs to be applied
            try:
                products_to_discount = basket[promo['free_product']]  # number of products that can be free
                if promo['free_product'] == promo['sku']:
                    promo_counter = int(basket[item] / (promo['amount'] + 1))
                while promo_counter > 0:
                    if products_to_discount > 0:
                        bill -= sku_prices[promo['free_product']]
                        products_to_discount -= 1
                        basket[promo['free_product']] -= 1
                    promo_counter -= 1
            except KeyError:
                print("Client has no product for discount")
    return bill


if __name__ == '__main__':
    print(checkout("AAAAA"))  # 200
    print(checkout("AAAAAA"))  # 250
    print(checkout("AAAAAAA"))  # 300
    print(checkout("AAA"))  # 130
    print(checkout("AAAA"))  # 180
    print(checkout("AAAAAAAA"))  # 330
    print(checkout("AAAABBEEE"))  # 330
    print(checkout("AAAAAAAAAA"))  # 400
    print(checkout("EEEEBB"))  # 160
    print(checkout("BEBEEE"))  # 160
    print(checkout("FF"))  # 20
    print(checkout("FFF"))  # 20
    print(checkout("FFFF"))  # 30
