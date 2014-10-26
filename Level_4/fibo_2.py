import unittest

def fibo2(n):
	fibo = 0
	if n == 1:
		fibo = 0
	elif n == 2:
		fibo = 1
	else:
		fibo = fibo2(n-1) + fibo2(n-2)

	return fibo % 4294967291

def fibo2_2(n):
	fibo = [0, 1]

	if n < 3:
		return fibo[n-1]

	for i in range(3, n+1):
		fibo.append(fibo[len(fibo)-1] + fibo[len(fibo)-2])

	return fibo[len(fibo)-1] % 4294967291

def fibo2_3(n):
	fibo = [0, 1]

	if n < 3:
		return fibo[n-1]

	for i in range(3, n+1):
		fibo.append(fibo[len(fibo)-1] + fibo[len(fibo)-2])
		del(fibo[0])

	return fibo[len(fibo)-1] % 4294967291


class TestFibo2(unittest.TestCase):
	def test_fibo2(self):
		self.assertEqual(fibo2(1), 0)
		self.assertEqual(fibo2(2), 1)
		self.assertEqual(fibo2(3), 1)
		self.assertEqual(fibo2(4), 2)
		self.assertEqual(fibo2(5), 3)
		self.assertEqual(fibo2(6), 5)

		# Error
		# self.assertEqual(fibo2(1000000000000000), 3010145777)

	def test_fibo2_2(self):
		self.assertEqual(fibo2_2(1), 0)
		self.assertEqual(fibo2_2(2), 1)
		self.assertEqual(fibo2_2(3), 1)
		self.assertEqual(fibo2_2(4), 2)
		self.assertEqual(fibo2_2(5), 3)
		self.assertEqual(fibo2_2(6), 5)
		# Memory Error
		# self.assertEqual(fibo2_2(1000000000000000), 3010145777) 

	def test_fibo2_3(self):
		self.assertEqual(fibo2_3(1), 0)
		self.assertEqual(fibo2_3(2), 1)
		self.assertEqual(fibo2_3(3), 1)
		self.assertEqual(fibo2_3(4), 2)
		self.assertEqual(fibo2_3(5), 3)
		self.assertEqual(fibo2_3(6), 5)

		# Memory Error
		self.assertEqual(fibo2_3(1000000000000000), 3010145777) 

if __name__ == '__main__':
	unittest.main()
	# input = 5
	# print('input : ' + str(input))
	# print('output : ' + str(fibo2_3(input)))
