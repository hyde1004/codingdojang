import unittest

def distance(dots):
	return abs(dots[0] - dots[1])

def separate(array):
	a = []
	for i in range(len(array) - 1):
		a.append([array[i], array[i+1]])

	return a

def method1(array):
	a = separate(array)
	min = a[0]

	for i in a:
		if distance(i) < distance(min) :
			min = i
	return min

class TestDistance(unittest.TestCase):
	def test_distance(self):
		self.assertEqual(distance([0, 1]), 1)
		self.assertEqual(distance([2, 5]), 3)

	def test_separate(self):
		self.assertEqual(separate([1, 2, 3]), [[1, 2], [2, 3]])

	def test_solution(self):
		s = [1, 3, 4, 8, 13, 17, 20]
		self.assertEqual(method1(s), [3, 4])

if __name__ == "__main__":
	unittest.main()

