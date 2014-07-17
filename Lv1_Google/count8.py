import unittest

def method1():
	count = 0
	for i in range(1, 10001):
		if str(i).count("8") > 0:
			count += str(i).count("8")
	return count

def method2():
	count = 0
	for i in range(1, 10001):
		count += str(i).count("8")
	return count	

class TestCount8(unittest.TestCase):
	def test_methods(self):
		self.assertEqual(method1(), 4000)
		self.assertEqual(method2(), 4000)
		
if __name__ == "__main__":
	unittest.main()