import unittest

"""
MATH

"""

class MathLib(object):
	def __init__(self):
		pass

	def get_digits_as_list(self, number):
		# print list(str(number))
		# return list(str(number))
		res = []
		k = 0
		floor = divmod(number, 10**k)[0]
		while floor > 0:
			res.append(divmod(number, 10**k)[1])
			k += 1
			floor = divmod(number, 10**k)[0]
			number /= 10

		return res
		# return [pow(divmod(number, pow(10, i))[1], 2) for ]
		# return [ for digit in number]


class MathLibTest(unittest.TestCase):
	def setUp(self):
		self.ml = MathLib()		

	def tearDown(self):
		self.ml = None

	def test_get_digits_as_list(self):
		a= self.ml.get_digits_as_list(7625) 
		print a
		assert a == [7,6,2,5]


if __name__ == "__main__":
	unittest.main()

