import unittest
import doctest

def isPrime(n):

    """
    Check if a number is prime.

    >>> isPrime(-1)
    False
    >>> isPrime(0)
    False
    >>> isPrime(5)
    True
    >>> isPrime(4)
    False

    """

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


class TestIsPrime(unittest.TestCase):
    def test_negative_number(self):
        self.assertEqual(isPrime(-1), False)

    def test_zero(self):
        self.assertEqual(isPrime(0), False)

    def test_prime_number(self):
        self.assertEqual(isPrime(5), True)

    def test_non_prime_number(self):
        self.assertEqual(isPrime(4), False)

    doctest.testmod()
    unittest.main()