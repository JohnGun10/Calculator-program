""" Importing this module cause in methods I have two different return values, hence to solve some mypy errors
	I am using Union for returning floats or None and if it breaks str"""
from typing import Union
# import doctest
import math


class Calculator:

	""" A Calculator class does mathematical operations like addition,
	subtraction, multiplication, division and taking nth root of a number.
	"""
	
	def __init__(self, memory: float = 0) -> None:
		"""Initializes default value to 0 if not set (1st example)
		"""
		self.__memory = memory

	def get_memory(self) -> Union[float, str]:
		"""Gets the memory value 
		>>> calculator = Calculator(4.0)
		>>> calculator.get_memory()
		4.0
		"""
		return self.__memory

	def set_memory(self, new_memory: float) -> Union[float, str]:
		"""Sets the memory value 
		>>> calculator = Calculator(4.0)
		>>> calculator.get_memory()
		4.0
		"""
		try: 
			new_memory == float(new_memory)
			self.__memory = new_memory
			return self.__memory
		except ValueError:
			return "The value should be a float"
		except TypeError:
			return "The value should be a float"

	def add(self, number: float) -> Union[float, str]:
		"""Method to add an integer (a) to a default value, which is 0 if not set.
		Addition: default + a = c
		>>> calculator = Calculator()
		>>> calculator.add(12.0)
		12.0
		"""
		try:
			"Rounding to two decimals and assignment"
			addition = self.__memory + number
			addition = round(addition, 4)
			self.__memory = addition
			return self.__memory
		except ValueError: 
			return "The value should be a float"
		except TypeError:
			return "The value should be a float"
		
	def divide(self, number: float) -> Union[float, str]:
		"""Method to divide default value by an integer (a) where default value is 0 if not set
		Division: default / a = c
		>>> calculator = Calculator(8)
		>>> calculator.divide(2)
		4.0
		"""
		try:
			"Rounding to two decimals and assignment"
			division = self.__memory / number
			division = round(division, 4)
			self.__memory = division
			return self.__memory
		except ValueError: 
			return "The value should be a float"
		except TypeError:
			return "The value should be a float"
		except ZeroDivisionError:
			print("You cannot divide by zero. Choose another number!\nError: \n")
			raise 
		
	def multiply(self, number: float) -> Union[float, str]:
		"""Method to multiply an integer (a) with a default value, which is 0 if not set
		Multiplication: default * a = c
		>>> calculator = Calculator(4.0)
		>>> calculator.multiply(4)
		16.0
		"""
		try:
			"Rounding to two decimals and assignment"
			multiplication = self.__memory * number
			multiplication = round(multiplication, 4)
			self.__memory = multiplication
			return self.__memory
		except ValueError: 
			return "The value should be a float"
		except TypeError:
			return "The value should be a float"
		
	def subtract(self, number: float) -> Union[float, str]:
		"""Method to subtract an integer (a) from a default value, which is 0 if not set
		Subtraction: default - a = c
		>>> calculator = Calculator(4)
		>>> calculator.subtract(2.0)
		2.0
		"""
		try:
			"Rounding to two decimals and assignment"
			subtraction = self.__memory - number
			subtraction = round(subtraction, 4)
			self.__memory = subtraction
			return self.__memory
		except ValueError: 
			return "The value should be a float"
		except TypeError:
			return "The value should be a float"

		
	def root(self, root_of_number: float) -> Union[float, str]:
		"""Method to take the root (n) of an integer. This method prints only real roots.
		Imaginary roots are not printed.
		Root: sqrt(n) > 0
		>>> calculator = Calculator(16)
		>>> calculator.root(2.0)
		4.0
		"""
		try:
			if root_of_number == 0:
				raise ValueError("Oth root is undefined. Please choose a root (n) to be n < 0 or n > 0")
			else:
				pass
			if self.__memory > 0:
				number_after_root = self.__memory**(1.0/root_of_number)
				self.__memory = number_after_root
			elif self.__memory < 0:
				"Because roots of a negative numbers give real and imaginary parts, this part " \
				"gives only real root of a negative number"
				number_after_root = -abs(self.__memory)**(1.0/root_of_number)
				self.__memory = number_after_root
			else:
				if root_of_number > 0:
					self.__memory = 0
				else:
					self.__memory = math.inf
			return self.__memory
		except ValueError as err: 
			return 'The error is: {}'.format(err)
		except ZeroDivisionError: 
			return "Take a value that is non zero"
		except TypeError:
			return "The value should be a float"
		
	def allocate(self, number: float) -> Union[float, str]:
		"""Select the mmory value by passing argument a (example a = 8)
		>>> calculator = Calculator()
		>>> calculator.allocate(8)
		8
		"""	
		try:
			"Assignments"
			self.__memory = number
			return self.__memory
		except ValueError:
			return "The value should be a float"
		except TypeError:
			return "The value should be a float"


	def reset(self) -> None:
		"""Method to reset memory value
		>>> calculator = Calculator()
		>>> calculator.reset()
		0
		>>> calculator.allocate(16)
		16
		"""
		self.__memory = 0
		print(self.__memory)
