import unittest

def is_prime(n):
	for i in range(2, n - 1):
		if n % i == 0:
			return False
	else:
		return True

def method(n):
	primes = []
	for i in range(2, n - 1):
		if is_prime(i) == True:
			if n % i == 0:
				primes.append(i)

	return primes


class TestLargestPrimeFactor(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(1, 1)
		self.assertEqual(method(13195), [5, 7, 13, 29])
		self.assertEqual(method(600851475143), [0])

	def test_is_prime(self):
		self.assertEqual(is_prime(2), True)
		self.assertEqual(is_prime(3), True)
		self.assertEqual(is_prime(4), False)
		self.assertEqual(is_prime(5), True)
		self.assertEqual(is_prime(6), False)

if __name__ == "__main__":
	unittest.main()

