"""Tests for prime.py — the suite we grew one case at a time in class."""

import unittest

from prime import is_prime, print_next_prime


class PrimesTestCase(unittest.TestCase):
    """Known cases."""

    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_four_prime(self):
        self.assertFalse(is_prime(4))

    def test_larger_prime(self):
        self.assertTrue(is_prime(97))

    def test_larger_composite(self):
        self.assertFalse(is_prime(91))  # 7 * 13


class PrimesEdgeCaseTestCase(unittest.TestCase):
    """The cases that broke us."""

    def test_is_zero_not_prime(self):
        self.assertFalse(is_prime(0))

    def test_is_one_not_prime(self):
        self.assertFalse(is_prime(1))

    def test_is_two_prime(self):
        self.assertTrue(is_prime(2))

    def test_negative_numbers(self):
        for number in range(-9, 0):
            with self.subTest(number=number):
                self.assertFalse(is_prime(number))


class NextPrimeTestCase(unittest.TestCase):
    """The function that uses the unit we tested."""

    def test_next_prime_after_ten(self):
        self.assertEqual(print_next_prime(10), 11)

    def test_next_prime_after_prime(self):
        self.assertEqual(print_next_prime(7), 11)


if __name__ == "__main__":
    unittest.main()
