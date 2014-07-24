import unittest

def merge_lists(a, b):
	c = []
	for i in range(len(a)):
		c.append(a[i])
		c.append(b[i])
	return c

class TestMergeList(unittest.TestCase):
	def test_merge_lists(self):
		self.assertEqual(merge_lists([1], [2]), [1, 2])
		self.assertEqual(merge_lists([1, 2, 3], [4, 5, 6]), [1, 4, 2, 5, 3, 6])

if __name__ == "__main__":
	unittest.main()

