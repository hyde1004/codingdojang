import unittest

def method1():
	return 4000

class TestCount8(unittest.TestCase):
	def test_methods(self):
		self.assertEqual(method1(), 4000)

if __name__ == "__main__":
	unittest.main()