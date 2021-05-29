import math


class Calculator:

	""" Compute the values of the mathematical operations:

	Addition: a + b = c
	Subtraction: a - b = d
	Multiplication: a * b = e
	Division: a / b = f
	Root: sqrt(n) > 0

	Written in python through functions as:
	
	a + b | a - b | a * b | a / b | math.sqrt(n)

	For example:
	
	>>> calculator.add(3)
	3
	>>> calculator.subtract(1)
	2
	>>> calculator.multiply(10)
	20
	>>> calculator.divide(5)
	4.0
	>>> calculator.root(225)
	15.0
	>>> calculator.allocate()
	0

	"""
	
	def __init__(self, default=0):
		"Initializes default value to 0 if not set"
		self.default = default

	def add(self, b: int) -> int:
		'Method to add an integer to a default value, which is 0 if not set'
		addition = self.default + b
		self.default = addition
		return addition
	
	def subtract(self, b: int) -> int:
		'Method to subtract an integer from a default value, which is 0 if not set'
		subtraction = self.default - b
		self.default = subtraction
		return subtraction
	
	def multiply(self, b: int) -> int:
		'Method to multiply an integer with a default value, which is 0 if not set'
		multiplication = self.default * b
		self.default = multiplication
		return multiplication

	def divide(self, b: int) -> int:
		'Method to divide default value by an integer where default value is 0 if not set'
		division = self.default / b
		self.default = division
		return division

	def root(self, b: float) -> float:
		'Method to take the root of an integer'
		root_of_number = math.sqrt(b)
		self.default = root_of_number
		return root_of_number
	
	def allocate(self):
		'Method to reset default memory'
		self.default = 0
		print(self.default)
	

calculator = Calculator()

if __name__ == '__main__':

	import doctest

	print(doctest.testmod())
