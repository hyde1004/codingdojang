import unittest

def method1(str):
	return str.replace('\t', '    ')


class TestTab2Space(unittest.TestCase):
	def test_method1(self):
		str = "Hello\tMy Friend."
		self.assertEqual(method1(str), "Hello    My Friend.")

if __name__ == "__main__":
	unittest.main()