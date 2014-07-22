import unittest

def method1(org):
	result = ""
	for pos in range(len(org)):
		if pos % 2 == 1 and org[pos].isdigit():
			result += '*'
		else:
			result += org[pos]
	return result

class TestEveryOtherDigit(unittest.TestCase):
	def test_solution(self):
		i = "a1b2cde3~g45hi6"
		self.assertEqual(method1(i), "a*b*cde*~g4*hi6")

if __name__ == "__main__":
	unittest.main()

