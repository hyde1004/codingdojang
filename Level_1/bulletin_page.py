import unittest

def method1(m, n):
	page = m / n
	if m % n != 0:
		page += 1

	return page

def method2(m, n):
	page = math.ceil(m / n)

	return page

class TestBulletinPage(unittest.TestCase):
	def test_method1(self):
		self.assertEqual(method1(0, 1), 0)
		self.assertEqual(method1(1, 1), 1)
		self.assertEqual(method1(2, 1), 2)
		self.assertEqual(method1(1, 10), 1)
		self.assertEqual(method1(10, 10), 1)
		self.assertEqual(method1(11, 10), 2)

	def test_method2(self):
		self.assertEqual(method1(0, 1), 0)
		self.assertEqual(method1(1, 1), 1)
		self.assertEqual(method1(2, 1), 2)
		self.assertEqual(method1(1, 10), 1)
		self.assertEqual(method1(10, 10), 1)
		self.assertEqual(method1(11, 10), 2)
		
if __name__ == "__main__":
	unittest.main()