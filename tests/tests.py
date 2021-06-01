# from calculator 
# import sys
# sys.path.append('/.../calculator/')
import pytest
from calculator.calculator import Calculator


def test_addition_when_memory_value_equal_to_zero():
	"""test of add method to see how it handles when you pass range from -1 to 1 and class is initialized to zero"""
	_calculator = Calculator()

	additives = [2, 3, 4]
	products = [2, 5, 9]
	for index, additive in enumerate(additives):
		assert _calculator.add(additive) == products[index]


def test_addition_when_memory_value_equal_to_one_various_range():
	"""test of add method to see how it handles when you pass 0, 10, -13 and class is initialized to one"""
	_calculator = Calculator(1)

	additives = [0, 10, -13]
	products = [1, 11, -2]
	for index, additive in enumerate(additives):
		assert _calculator.add(additive) == products[index]


def test_addition_when_memory_value_equal_to_negative_one_various_range():
	"""test of add method to see how it handles when you pass -77, 0, 185 and class
		is initialized to -73"""
	_calculator = Calculator(-73)

	additives = [0, -77, 185]
	products = [-73, -150, 35]
	for index, additive in enumerate(additives):
		assert _calculator.add(additive) == products[index]


def test_subtraction_when_memory_value_equal_to_zero():
	"""test of subtract method to see how it handles when you pass range from -1 to 1 and class is initialized to zero"""
	_calculator = Calculator()
	for a in range(-1, 1):
		if a == 1:
			assert _calculator.subtract(a) == 0
		else:
			assert _calculator.subtract(a) == 1


def test_subtraction_when_memory_value_equal_to_negative_one_positive_range():
	"""test of subtract method to see how it handles when you pass -57, 0, 75 and class is initialized to negative one"""
	_calculator = Calculator(-1)
	
	subtractives = [-57, 0, 75]
	products = [56, 56, -19]
	for index, subtractive in enumerate(subtractives):
		assert _calculator.subtract(subtractive) == products[index]


def test_subtraction_when_memory_value_equal_to_one_positive_range():
	"""test of subtract method to see how it handles when you pass -17, 0, 41 and class is initialized to one"""
	_calculator = Calculator(1)
	
	subtractives = [-17, 0, 41]
	products = [18, 18, -23]
	for index, subtractive in enumerate(subtractives):
		assert _calculator.subtract(subtractive) == products[index]
	

def test_multiplication_when_memory_value_equal_to_zero():
	"""test of multiply method to see how it handles when you pass range from -1 to 1 and class is initialized to zero"""
	_calculator = Calculator()
	for a in range(-1, 1):
		assert _calculator.multiply(a) == 0


def test_multiplication_when_memory_value_equal_to_negative_one_positive_range():
    """test of multiply method to see how it handles when you pass positive numbers
        and class is initialized to negative one"""
    _calculator = Calculator(-1)

    multipliers = [2, 3.4, 4]
    products = [-2, -6.8, -27.2]
    for index, multiplier in enumerate(multipliers):
        assert _calculator.multiply(multiplier) == products[index]


def test_multiplication_when_memory_value_equal_to_negative_one_negative_range():
	"""test of multiply method to see how it handles when you pass 8, -10, 0
		and class is initialized to negative one"""
	_calculator = Calculator(-8)

	multipliers = [8.5, -10, 0]
	products = [-68.0, 680, 0]
	for index, multiplier in enumerate(multipliers):
		assert _calculator.multiply(multiplier) == products[index]


def test_multiplication_when_memory_value_equal_to_one_positive_range():
	"""test of multiply method to see how it handles when you pass positive numbers
		and class is initialized to one"""
	_calculator = Calculator(1)

	multipliers = [2, 3, 4]
	products = [2, 6, 24]
	for index, multiplier in enumerate(multipliers):
		assert _calculator.multiply(multiplier) == products[index]


def test_multiplication_when_memory_value_equal_to_one_negative_range():
	"""test of multiply method to see how it handles when you pass negative numbers
	and class is initialized to one"""
	_calculator = Calculator(1)
	
	multipliers = [-2, -3, -4]
	products = [-2, 6, -24]
	for index, multiplier in enumerate(multipliers):
		assert _calculator.multiply(multiplier) == products[index]


def test_division_when_memory_value_equal_to_zero():
	"""test of divide method to see how it handles when you pass near zero values
	and class is initialized to zero"""
	_calculator = Calculator()
	for a in range(-1, 1):
		if a == 0:
			with pytest.raises(ZeroDivisionError):
				_calculator.divide(a)
		else:
			assert _calculator.divide(a) == 0			


def test_division_when_memory_value_equal_to_one_positive_range():
	"""test of divide method to see how it handles when you pass -12, 2, 8 and class is initialized to 24"""
	_calculator = Calculator(24)
	
	divisors = [-12, 2, 8]
	products = [-2, -1, -0.125]
	for index, divisor in enumerate(divisors):
		assert _calculator.divide(divisor) == products[index]


def test_division_when_memory_value_equal_to_one_negative_range():
	"""test of divide method to see how it handles when you pass negative numbers and class is initialized to one"""
	_calculator = Calculator(1)

	divisors = [-2, -3, -4]
	products = [-0.5, 0.16666666666666666, -0.041666666666666664]
	for index, divisor in enumerate(divisors):
		assert _calculator.divide(divisor) == products[index]


def test_division_when_memory_value_equal_to_negative_one_positive_range():
	"""test of divide method to see how it handles when you pass -12, 0.5, -2 and class
	is initialized to negative 24"""
	_calculator = Calculator(-24)

	divisors = [-12, 0.5, -2]
	products = [2, 4, -2]
	for index, divisor in enumerate(divisors):
		assert _calculator.divide(divisor) == products[index]

def test_division_when_memory_value_equal_to_negative_one_negative_range():
	"""test of divide method to see how it handles when you pass 0.125, -2, 4 and class
	is initialized to negative one"""
	_calculator = Calculator(-1)

	divisors = [0.125, -2, 4]
	products = [-8, 4, 1]
	for index, divisor in enumerate(divisors):
		assert _calculator.divide(divisor) == products[index]		


def test_root_when_memory_value_equal_to_zero():
	"""test of root method to see how it handles when you pass zero to negative one and class is initialized to zero.
	This checks for interesting cases"""
	_calculator = Calculator(0)
	for a in range(-1, 1):
		if a == 0:
			assert _calculator.root(a) == 1
		elif a == -1:
			assert _calculator.root(a) == float("inf") or float("-inf")
		else:
			with pytest.raises(AssertionError):
				assert _calculator.root(a)


def test_root_when_memory_value_equal_to_eight():
	"""test of root method to see how it handles when the class is initialized to eight"""
	_calculator = Calculator(8)
	assert _calculator.root(3) == 2


def test_root_when_memory_value_equal_to_one_negative_range():
	"""test of root method to see how it handles when you pass negative numbers and class is initialized to one"""
	_calculator = Calculator(1)
	for a in range(-4, -2):
		assert _calculator.root(a) == 1


def test_root_when_memory_value_equal_to_negative_one_negative_range():
	"""test of root method to see how it handles complex numbers when you pass negative numbers
	and class is initialized to negative one"""
	_calculator = Calculator(-1)
	
	roots = [-2, -3, -4]
	products = [6.123233995736766e-17-1j, 0.8660254037844387+0.49999999999999994j, 0.9914448613738104-0.13052619222005157j]
	for index, root in enumerate(roots):
		assert _calculator.root(root) == products[index]
		

def test_root_when_memory_value_equal_to_negative_one_positive_range():
	"""test of root method to see how it handles complex numbers when you pass positive numbers and
	class is initialized to negative one"""
	_calculator = Calculator(-1)
	for a in range(2, 4):
		if a == 2:
			assert _calculator.root(a) == (6.123233995736766e-17+1j)
		elif a == 3:
			assert _calculator.root(a) == (0.8660254037844387+0.49999999999999994j)
		else:
			assert _calculator.root(a) == (0.9914448613738104+0.13052619222005157j)



