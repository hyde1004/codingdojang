import unittest

def fibo_1(n):
	fibo = 0
	if n == 1:
		fibo = 0
	elif n == 2:
		fibo = 1
	else:
		fibo = fibo_1(n-1) + fibo_1(n-2)

	return fibo

def fibo_2(n):
	fibo = [0, 1]

	if n < 3:
		return fibo[n-1]

	for i in range(3, n+1):
		fibo.append(fibo[len(fibo)-1] + fibo[len(fibo)-2])

	return fibo[len(fibo)-1]

def fibo_3(n):
	fibo = [0, 1]

	if n < 3:
		return fibo[n-1]

	for i in range(3, n+1):
		fibo.append(fibo[len(fibo)-1] + fibo[len(fibo)-2])
		del(fibo[0])

	return fibo[len(fibo)-1]


class TestFibo(unittest.TestCase):
	def test_fibo(self):
		self.assertEqual(fibo_1(1), 0)
		self.assertEqual(fibo_1(2), 1)
		self.assertEqual(fibo_1(3), 1)
		self.assertEqual(fibo_1(4), 2)
		self.assertEqual(fibo_1(5), 3)
		self.assertEqual(fibo_1(6), 5)

	def test_fibo_2(self):
		self.assertEqual(fibo_2(1), 0)
		self.assertEqual(fibo_2(2), 1)
		self.assertEqual(fibo_2(3), 1)
		self.assertEqual(fibo_2(4), 2)
		self.assertEqual(fibo_2(5), 3)
		self.assertEqual(fibo_2(6), 5)

	def test_fibo_3(self):
		self.assertEqual(fibo_3(1), 0)
		self.assertEqual(fibo_3(2), 1)
		self.assertEqual(fibo_3(3), 1)
		self.assertEqual(fibo_3(4), 2)
		self.assertEqual(fibo_3(5), 3)
		self.assertEqual(fibo_3(6), 5)

if __name__ == '__main__':
	unittest.main()
	# input = 5
	# print('input : ' + str(input))
	# print('output : ' + str(fibo_3(input)))
