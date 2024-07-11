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
    def test_checkout(self, input, expected, setup_checkout):
        assert checkout(input) == expected, f"Checkout total for {input} should be {expected}"

    def test_chk_apply_promotion(selfs):
        assert apply_promotions({'A': 4, 'B': 2, 'E': 3}, 365) == 315


