import pytest

from app.calculator import Calculator


class TestCalculator:
    def setup(self):
        self.calculator = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calculator.multiply(self, 3, 2) == 6

    def test_division_calculate_correctly(self):
        assert self.calculator.division(self, 4, 2) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calculator.subtraction(self, 5, 2) == 3

    def test_adding_calculate_correctly(self):
        assert self.calculator.adding(self, 5, 2) == 7