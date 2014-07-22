import unittest

def multiple1():
	sum = 0
	for i in range(1, 1000):
		if i % 3 == 0 or i % 5 == 0:
			sum += i

	return sum

def multiple2():
	a = [x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]
	return sum(a)

def multiple3():
	set3 = set(range(3, 1000, 3))
	set5 = set(range(5, 1000, 5))
	return sum( set3 | set5 )

class MultipliesTest(unittest.TestCase):
	def test_multiple(self):
		self.assertEqual(multiple1(), 233168)
		self.assertEqual(multiple2(), 233168)
		self.assertEqual(multiple3(), 233168)

if __name__ == "__main__":
	unittest.main()
