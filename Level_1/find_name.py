#-*-coding:utf-8

import unittest
def search(name_list, family_name):
	return 1

class TestFindName(unittest.TestCase):
	def setUp(self):
		names = ["이유덕","이재영","권종표","이재영","박민호","강상희","이재영","김지완","최승혁","이성연","박영서","박민호","전경헌","송정환","김재성","이유덕","전경헌"]

	def test_search(self):
		self.assertEqual(search(names, "김"), 1)

if __name__ == "__main__":
	unittest.main()

