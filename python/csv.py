import csv
import unittest

class CsvHelper(object):
	def __init__(self):
		pass

	def read_lines(self, filepath):
		with open(filepath, 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				print row


class CsvHelperTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

if __name__ == "__main__":
	unittest.main()
