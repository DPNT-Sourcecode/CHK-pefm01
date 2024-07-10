
# noinspection PyUnusedLocal
# skus = unicode string

sku_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

promotions = {
    '3A': 20,
    '2B': 15
}

bill = 0


def checkout(skus: str) -> int:
    products = list(str)  # converting to the list to easier operate on it
    basket = {}
    for product in products:
        if product in basket.keys():
            basket[product] += 1
        else:
            basket[product] = 1

def count_basket(basket: dict) -> int:
    for item in basket:
        bill += sku_prices[item]*item
