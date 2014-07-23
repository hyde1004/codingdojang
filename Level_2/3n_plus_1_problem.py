import unittest
def get_cycle(n):
	cycle = [n]
	while(not n == 1):
		if n % 2 == 0:
			n = n // 2
		else:
			n = n * 3 + 1
		cycle.append(n)
	return cycle

def get_cycles(n1, n2):
	cycles = []
	for i in range(n1, n2+1):
		cycles.append(get_cycle(i))

	return cycles

def method1(n1, n2):
	cycles = get_cycles(n1, n2)
	max_len_cycles = len(cycles[0])

	for cycle in cycles:
		if len(cycle) > max_len_cycles:
			max_len_cycles = len(cycle)

	return max_len_cycles

class TestThreeN(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(method1(22,22), 16)
		self.assertEqual(method1(1, 10), 20)
		self.assertEqual(method1(100, 200), 125)
		self.assertEqual(method1(201, 210), 89)
		self.assertEqual(method1(900, 1000), 174)

	def test_get_cycle(self):
		self.assertEqual(get_cycle(22), [22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

	def test_get_cycles(self):
		self.assertEqual(get_cycles(22, 22), [[22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]])


if __name__ == "__main__":
	unittest.main()

