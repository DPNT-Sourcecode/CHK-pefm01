
from lib.solutions.CHK.checkout_solution import count_basket, apply_promotions, checkout


class TestChk():
    def test_chk(self):
        assert count_basket({'A': 4, 'B': 2, 'E': 3}) == 315


    def check_full_solution(self):
        assert checkout("AAAAA") == 200
        # assert checkout("AAAAAA") == 250
        # assert checkout("AAAAAAA") == 300
        # assert checkout("AAA") == 130
        # assert checkout("AAAA") == 180
        # assert checkout("AAAAAAAA") == 330
        # assert checkout("AAAABBEEE") == 330
        # assert checkout("AAAAAAAAAA") == 400
        # assert checkout("EEEEBB") == 160
        # assert checkout("BEBEEE") == 160
        # assert checkout("FF") == 20
        # assert checkout("FFF") == 20
        # assert checkout("FFFF") == 30

    # def test_chk_apply_promotion(selfs):
    #     assert apply_promotions({'A': 4, 'B': 2, 'E': 3}) == 315


