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

print(Solution(3))
print(Solution(7))
print(Solution(9901))
