
from lib.solutions.CHK.checkout_solution import count_basket, apply_promotions, apply_discounts


class TestChk():
    def test_chk(self):
        assert count_basket({'A': 4, 'B': 2, 'E': 3}) == 315

    def test_chk_apply_promotion(selfs):
        assert apply_promotions()

