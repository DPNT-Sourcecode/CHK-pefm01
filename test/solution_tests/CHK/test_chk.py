import pytest
from lib.solutions.CHK.checkout_solution import count_basket, apply_promotions, checkout


class TestChk():

    @pytest.fixture
    def setup_checkout(self):
        pass

    # Using parametrize to simplify tests
    @pytest.mark.parametrize("input,expected", [
        ("AAAAA", 200),
        ("AAAAAA", 250),
        ("AAAAAAA", 300),
        ("AAA", 130),
        ("AAAA", 180),
        ("AAAAAAAA", 330),
        ("AAAABBEEE", 330),
        ("AAAAAAAAAA", 400),
        ("EEEEBB", 160),
        ("BEBEEE", 160),
        ("FF", 20),
        ("FFF", 20),
        ("FFFF", 30),
    ])
    def test_checkout(input, expected, setup_checkout):
        assert checkout(input) == expected, f"Checkout total for {input} should be {expected}"

    # def test_chk(self):
    #     assert count_basket({'A': 4, 'B': 2, 'E': 3}) == 330
    #
    # def check_full_solution1(self):
    #     assert checkout("AAAAA") == 200
    #
    # def check_full_solution2(self):
    #     assert checkout("AAAAAA") == 250
    #
    # def check_full_solution3(self):
    #     assert checkout("AAAAAAA") == 300
    #
    # def check_full_solution4(self):
    #     assert checkout("AAA") == 130
    #
    # def check_full_solution5(self):
    #     assert checkout("AAAA") == 180
    #
    # def check_full_solution6(self):
    #     assert checkout("AAAAAAAA") == 330
    #
    # def check_full_solution7(self):
    #     assert checkout("AAAABBEEE") == 330
    #
    # def check_full_solution8(self):
    #     assert checkout("AAAAAAAAAA") == 400
    #
    # def check_full_solution9(self):
    #     assert checkout("EEEEBB") == 160
    #
    # def check_full_solution10(self):
    #     assert checkout("BEBEEE") == 160
    #
    # def check_full_solution11(self):
    #     assert checkout("FF") == 20
    #
    # def check_full_solution12(self):
    #     assert checkout("FFF") == 20
    #
    # def check_full_solution13(self):
    #     assert checkout("FFFF") == 30

    def test_chk_apply_promotion(selfs):
        assert apply_promotions({'A': 4, 'B': 2, 'E': 3}, 365) == 315

