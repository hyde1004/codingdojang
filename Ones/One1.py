import unittest

def RepeatOne(x):
	"""RepeatOne(1) : 1, RepeatOne(2) : 11"""
	return "1" * x

def Solution(input):
	x = 1
	complete = False
	while(not complete):
		number = RepeatOne(x)
		if (int(number) % input == 0):
			return x
		else:
			x += 1

class OnesTest(unittest.TestCase):
	def test_result(self):
		self.assertEqual(Solution(3), 3)
		self.assertEqual(Solution(7), 6)
		self.assertEqual(Solution(9901), 12)

if __name__ == "__main__":
	unittest.main()

