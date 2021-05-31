import doctest

class Calculator:

	''' A Calculator class does mathematical operations like addition,
	subtraction, multiplication, division and taking nth root of a number.
	'''
	
	def __init__(self, memory: float = 0) -> None:
		"""Initializes default value to 0 if not set (1st example)
		>>> calculator.__init__()
		"""
		self.__memory = memory
	def get_memory(self) -> float:
		"""Gets the memory value 
		>>> calculator.get_memory()
		4.0
		"""
		try:
			self.__memory == float(self.__memory)
			return self.__memory
		except ValueError: 
			return "The value should be a float"

	def set_memory(self, new_memory: float) -> None:
		"""Sets the memory value 
		>>> calculator.get_memory()
		4.0
		"""
		try:
			self.__memory = new_memory
		except ValueError: 
			return "The value should be a float"

	def add(self, number: float) -> float:
		"""Method to add an integer (a) to a default value, which is 0 if not set.
		Addition: default + a = c
		>>> calculator.add(12.0)
		12.0
		"""
		try:
			number == float(number)
			addition = self.__memory + number
			self.__memory = addition
			return addition
		except ValueError: 
			return "The value should be a float"
		
	def divide(self, number: float) -> float:
		"""Method to divide default value by an integer (a) where default value is 0 if not set
		Division: default / a = c
		>>> calculator.divide(2)
		4.0
		"""
		try:
			number == float(number)
			division = self.__memory / number
			self.__memory = division
			return division
		except ValueError: 
			return "The value should be a float"
		
	def multiply(self, number: float) -> float:
		"""Method to multiply an integer (a) with a default value, which is 0 if not set
		Multiplication: default * a = c
		>>> calculator.multiply(4)
		16.0
		"""
		try:
			number == float(number)
			multiplication = self.__memory * number
			self.__memory = multiplication
			return multiplication
		except ValueError: 
			return "The value should be a float"
		
	def subtract(self, number: float) -> float:
		"""Method to subtract an integer (a) from a default value, which is 0 if not set
		Subtraction: default - a = c
		>>> calculator.subtract(2.0)
		2.0
		"""
		try:
			number == float(number)
			subtraction = self.__memory - number
			self.__memory = subtraction
			return subtraction
		except ValueError: 
			return "The value should be a float"
		
	def root(self, root_of_number: float) -> float:
		"""Method to take the root of an integer (n)
		Root: sqrt(n) > 0
		>>> calculator.root(2.0)
		4.0
		"""
		try:
			# if root_of_number == 0:
			# 	self.__memory = 0
			# 	return 0
			root_of_number = float(root_of_number)
			root_of_number = self.__memory**(1/float(root_of_number))
			self.__memory = root_of_number
			return root_of_number
		except ValueError: 
			return "The value should be a float"
		except ZeroDivisionError: 
			return "Division by zero not possible. Take a value that is non zero"
		
	def allocate(self, number: float) -> float:
		"""Select the default value by passing argument a (example a = 8)
		>>> calculator.allocate(8)
		8
		"""	
		try:
			number == float(number)
			self.__memory == float(self.__memory)
			self.__memory = number
			return number
		except ValueError:
			return "The value should be a float"

		
	def reset(self) -> None:
		"""Method to reset default memory
		>>> calculator.reset()
		0
		>>> calculator.allocate(16)
		16
		"""
		self.__memory = 0
		print(self.__memory)

calculator = Calculator()
doctest.testmod()
