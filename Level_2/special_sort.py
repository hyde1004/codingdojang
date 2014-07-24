import unittest

def method1(unsorted):
	minus_items = gather_minus(unsorted)
	plus_items = gather_plus(unsorted)

	sorted = minus_items + plus_items

	return sorted

def gather_plus(items):
	plus_items = [item for item in items if item > 0]
	return plus_items

def gather_minus(items):
	minus_items = [item for item in items if item < 0]
	return minus_items

class TestSpeicalSort(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(method1([-1, 1, 3, -2, 2]), [-1, -2, 1, 3, 2])

	def test_gather_plus(self):
		self.assertEqual(gather_plus([-1, 2, 3, 4, -2]), [2, 3, 4 ])

	def test_gather_minus(self):
		self.assertEqual(gather_minus([-1, 2, 3, 4, -2]), [-1, -2])

if __name__ == "__main__":
	unittest.main()

