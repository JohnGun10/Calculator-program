import math


class Calculator:

	''' Compute the values of the mathematical operations:

	Addition: a + b = c
	Subtraction: a - b = d
	Multiplication: a * b = e
	Division: a / b = f
	Root: sqrt(n) > 0

	Written in python through functions as:
	
	a + b | a - b | a * b | a / b | math.sqrt(n)

	'''
	
	def __init__(self, default=0):
		"""Initializes default value to 0 if not set (1st example, 2nd example - default=8)
		>>> calculator.__init__()
		"""
		self.default = default

	def add(self, b: float) -> float:
		"""Method to add an integer (a) to a default value, which is 0 if not set.
		Addition: default + a = c
		>>> calculator.add(4)
		4
		"""
		addition = self.default + b
		self.default = addition
		return int(addition)

	def divide(self, b: float) -> float:
		"""Method to divide default value by an integer (a) where default value is 0 if not set
		Division: default / a = c
		>>> calculator.divide(2)
		4.0
		"""
		division = self.default / b
		self.default = division
		return division

	def multiply(self, b: float) -> float:
		"""Method to multiply an integer (a) with a default value, which is 0 if not set
		Multiplication: default * a = c
		>>> calculator.multiply(4)
		16.0
		"""
		multiplication = self.default * b
		self.default = multiplication
		return multiplication

	def subtract(self, b: float) -> float:
		"""Method to subtract an integer (a) from a default value, which is 0 if not set
		Subtraction: default - a = c
		>>> calculator.subtract(2)
		-2
		"""
		subtraction = self.default - b
		self.default = subtraction
		return subtraction

	def root(self, b: float) -> float:
		"""Method to take the root of an integer (n)
		Root: sqrt(n) > 0
		>>> calculator.root(64)
		8.0
		>>> calculator.reset()
		0
		"""
		root_of_number = math.sqrt(b)
		self.default = root_of_number
		return root_of_number

	def allocate(self, a):
		"""Select the default value by passing argument a (example a = 8)
		>>> calculator.allocate(8)
		8
		"""
		self.default = a
		return a
		
	def reset(self):
		"""Method to reset default memory
		>>> calculator.reset()
		0
		"""
		self.default = 0
		print(self.default)


calculator = Calculator()

if __name__ == '__main__':

	import doctest

	print(doctest.testmod())
