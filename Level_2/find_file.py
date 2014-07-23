import unittest
import pathlib

def has_string(in_file, find_string):
	f = open(in_file, "r")
	s = f.read()
	f.close()

	if s.find(find_string) >= 0:
		return True
	else:
		return False

def find_files(file_name):
	p = pathlib.Path('.')
	files = list(p.glob(file_name))
	return files

def method1(in_files, find_string):
	result = []

	for in_file in in_files:
		if has_string(in_file, find_string) == True:
			result.append(in_file)
	return result

class TestFindFile(unittest.TestCase):
	def test_has_string(self):
		self.assertEqual(has_string("test_file1.txt", "LIFE IS TOO SHORT"), True)
		self.assertEqual(has_string("test_file2.txt", "LIFE IS TOO SHORT"), False)

	# def test_find_files(self):
	# 	self.assertEqual(find_files('**/*.txt'), True)

	def test_solution(self):
		files = find_files('**/*.txt')
		self.assertEqual(method1(files, "LIFE IS TOO SHORT"), "test_file1.txt")

if __name__ == "__main__":
	unittest.main()