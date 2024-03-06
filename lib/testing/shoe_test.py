import pytest
from lib.shoe import Shoe

class TestShoe(object):
    def test_shoe_initialization(self):
        shoe = Shoe("Nike", "Leather", 10, "White")
        assert shoe.brand == "Nike"
        assert shoe.material == "Leather"
        assert shoe.size == 10
        assert shoe.color == "White"

    def test_change_color(self):
        shoe = Shoe("Nike", "Leather", 10, "White")
        shoe.change_color("Black")
        assert shoe.color == "Black"
