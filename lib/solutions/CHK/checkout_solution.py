# noinspection PyUnusedLocal
# skus = unicode string
import json
from collections import OrderedDict

sku_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21
}

promotions = """
[
  {
        "sku": "V",
        "amount": 3,
        "discount": 20
},
  {
        "sku": "V",
        "amount": 2,
        "discount": 10
},
{
        "sku": "Q",
        "amount": 3,
        "discount": 10
},
{
        "sku": "P",
        "amount": 5,
        "discount": 50
},
{
        "sku": "K",
        "amount": 2,
        "discount": 20
    },
    {
        "sku": "H",
        "amount": 10,
        "discount": 20
    },
    {
        "sku": "H",
        "amount": 5,
        "discount": 5
    },
        {
        "sku": "B",
        "amount": 2,
        "discount": 15
    },
    {
        "sku": "A",
        "amount": 5,
        "discount": 50
    },
    {
        "sku": "A",
        "amount": 3,
        "discount": 20
    }
]
"""

free_products = """
[
{
        "sku": "U",
        "amount": 3,
        "free_product": "U"
    },
{
        "sku": "R",
        "amount": 3,
        "free_product": "Q"
    },
{
        "sku": "N",
        "amount": 3,
        "free_product": "M"
    },
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

group_discounts = """
[
    { 
        "list": ["S", "T", "X", "Y", "Z"], 
        "price": 45,
         "count": 3
    }
]
"""


def checkout(skus: str) -> int:
    products = list(skus)  # converting to the list to easier operate on it
    bill = check_group_discounts(skus)
    basket = {}
    for product in products:
        if product in basket.keys():
            basket[product] += 1  # product exists in dic, incrementing
        else:
            basket[product] = 1  # product does not exists, adding
    return count_basket(basket, bill)


def count_basket(basket: dict, bill) -> int:
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


def check_group_discounts(skus: str):
    group_discounts_load = json.loads(group_discounts)
    ordered_pricing = sorted(sku_prices.items(), key=lambda x: x[1], reverse=True)
    for group in group_discounts_load:
        count = group['count']
        for product in skus:
            basket_temp = skus
            if product in basket_temp:
                count -= 1
                basket_temp.

                return group['price']



if __name__ == '__main__':
    # print(checkout("AAAAA"))  # 200
    # print(checkout("AAAAAA"))  # 250
    # print(checkout("AAAAAAA"))  # 300
    # print(checkout("AAA"))  # 130
    # print(checkout("AAAA"))  # 180
    # print(checkout("AAAAAAAA"))  # 330
    # print(checkout("AAAABBEEE"))  # 330
    # print(checkout("AAAAAAAAAA"))  # 400
    # print(checkout("EEEEBB"))  # 160
    # print(checkout("BEBEEE"))  # 160
    # print(checkout("FF"))  # 20
    # print(checkout("FFF"))  # 20
    # print(checkout("FFFF"))  # 30
    print(checkout("XYZZZXY"))
