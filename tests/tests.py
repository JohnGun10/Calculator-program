# from calculator 
# import sys
# sys.path.append('/.../calculator/')
from calculator.calculator import Calculator
import pytest

def test_addition_when_memory_value_equal_to_zero():
	'test of add method to see how it handles when you pass range from -1 to 1 and class is initialized to zero'
	_calculator = Calculator()
	for a in range(-1, 1):
		if a == 1:
			assert _calculator.add(a) == 0
		elif a == 0:
			assert _calculator.add(a) == -1
		else:
			assert _calculator.add(a) == -1


def test_addition_when_memory_value_equal_to_one_positive_range():
	'test of add method to see how it handles when you pass range from 2 to 4 and class is initialized to one'
	_calculator = Calculator(1)
	for a in range(2, 4):
		if a == 2:
			assert _calculator.add(a) == 3
		elif a == 3:
			assert _calculator.add(a) == 6
		else:
			assert _calculator.add(a) == 10

def test_addition_when_memory_value_equal_to_one_negative_range():
	'test of add method to see how it handles when you pass range from -4 to -2 and class is initialized to one'
	_calculator = Calculator(1)
	for a in range(-4, -2):
		if a == -4:
			assert _calculator.add(a) == -3
		elif a == -3:
			assert _calculator.add(a) == -6
		else:
			assert _calculator.add(a) == -8

def test_addition_when_memory_value_equal_to_negative_one_positive_range():
	'test of add method to see how it handles when you pass range from 2 to 4 and class is initialized to negative one'
	_calculator = Calculator(-1)
	for a in range(2, 4):
		if a == 2:
			assert _calculator.add(a) == 1
		elif a == 3:
			assert _calculator.add(a) == 4
		else:
			assert _calculator.add(a) == 8

def test_addition_when_memory_value_equal_to_negative_one_negative_range():
	'test of add method to see how it handles when you pass range from -4 to -2 and class is initialized to negative one'
	_calculator = Calculator(-1)
	for a in range(-4, -2):
		if a == -4:
			assert _calculator.add(a) == -5
		elif a == -3:
			assert _calculator.add(a) == -8
		else:
			assert _calculator.add(a) == -10

def test_subtraction_when_memory_value_equal_to_zero():
	'test of subtract method to see how it handles when you pass range from -1 to 1 and class is initialized to zero'
	_calculator = Calculator()
	for a in range(-1, 1):
		if a == 1:
			assert _calculator.subtract(a) == 0
		elif a == 0:
			assert _calculator.subtract(a) == 1
		else:
			assert _calculator.subtract(a) == 1


def test_subtraction_when_memory_value_equal_to_negative_one_positive_range():
	'test of subtract method to see how it handles when you pass range from 2 to 4 and class is initialized to negative one'
	_calculator = Calculator(-1)
	for a in range(2, 4):
		if a == 2:
			assert _calculator.subtract(a) == -3
		elif a == 3:
			assert _calculator.subtract(a) == -6
		else:
			assert _calculator.subtract(a) == -10

def test_subtraction_when_memory_value_equal_to_negative_one_negative_range():
	'test of subtract method to see how it handles when you pass range from -4 to -2 and class is initialized to negative one'
	_calculator = Calculator(-1)
	for a in range(-4, -2):
		if a == -4:
			assert _calculator.subtract(a) == 3
		elif a == -3:
			assert _calculator.subtract(a) == 6
		else:
			assert _calculator.subtract(a) == 8

def test_subtraction_when_memory_value_equal_to_one_positive_range():
	'test of subtract method to see how it handles when you pass range from 2 to 4 and class is initialized to one'
	_calculator = Calculator(1)
	for a in range(2, 4):
		if a == 2:
			assert _calculator.subtract(a) == -1
		elif a == 3:
			assert _calculator.subtract(a) == -4
		else:
			assert _calculator.subtract(a) == 0

def test_subtraction_when_memory_value_equal_to_one_positive_range_negative_range():
	'test of subtract method to see how it handles when you pass range from -4 to -2 and class is initialized to one'
	_calculator = Calculator(1)
	for a in range(-4, -2):
		if a == -4:
			assert _calculator.subtract(a) == 5
		elif a == -2:
			assert _calculator.subtract(a) == 10
		else:
			assert _calculator.subtract(a) == 8

def test_multiplication_when_memory_value_equal_to_zero():
	'test of multiply method to see how it handles when you pass range from -1 to 1 and class is initialized to zero'
	_calculator = Calculator()
	for a in range(-1, 1):
		assert _calculator.multiply(a) == 0

# @pytest.mark.parametrize("test_input,expected", [(-4, 4), (-3, 3), (-2, 2)])
# def test_eval(test_input, expected):
# 	_calculator = Calculator(-1)
# 	test_input = _calculator.multiply()
# 	assert eval(test_input) == expected

def test_multiplication_when_memory_value_equal_to_negative_one_positive_range():
	'test of multiply method to see how it handles when you pass positive numbers and class is initialized to negative one'
	_calculator = Calculator(-1)
	for a in range(2, 4):
		if a == 2:
			assert _calculator.multiply(a) == -2
		elif a == 3:
			assert _calculator.multiply(a) == -6
		else:
			assert _calculator.multiply(a) == -24

def test_multiplication_when_memory_value_equal_to_negative_one_negative_range():
	'test of multiply method to see how it handles when you pass negative numbers and class is initialized to negative one'
	_calculator = Calculator(-1)
	for a in range(-4, -2):
		if a == -4:
			assert _calculator.multiply(a) == 4
		elif a == -3:
			assert _calculator.multiply(a) == -12
		else:
			assert _calculator.multiply(a) == 24

def test_multiplication_when_memory_value_equal_to_one_positive_range():
	'test of multiply method to see how it handles when you pass positive numbers and class is initialized to one'
	_calculator = Calculator(1)
	for a in range(2, 4):
		if a == 2:
			assert _calculator.multiply(a) == 2
		elif a == 3:
			assert _calculator.multiply(a) == 6
		else:
			assert _calculator.multiply(a) == 24

def test_multiplication_when_memory_value_equal_to_one_negative_range():
	'test of multiply method to see how it handles when you pass negative numbers and class is initialized to one'
	_calculator = Calculator(1)
	for a in range(-4, -2):
		if a == -4:
			assert _calculator.multiply(a) == -4
		elif a == -3:
			assert _calculator.multiply(a) == 12
		else:
			assert _calculator.multiply(a) == -24

def test_division_when_memory_value_equal_to_zero():
	'test of divide method to see how it handles when you pass near zero values and class is initialized to zero'
	_calculator = Calculator()
	for a in range(-1, 1):
		if a == 0:
			with pytest.raises(ZeroDivisionError):
				_calculator.divide(a)
		elif a == -1:
			assert _calculator.divide(a) == 0
		else:
			assert _calculator.divide(a) == 0			


def test_division_when_memory_value_equal_to_one_positive_range():
	'test of divide method to see how it handles when you pass positive numbers and class is initialized to one'
	_calculator = Calculator(1)
	for a in range(2, 4):
		if a == 2:
			assert _calculator.divide(a) == 0.5
		elif a == 3:
			assert _calculator.divide(a) == 0.16666666666666666
		else:
			assert _calculator.divide(a) == 0.041666666666666664

def test_division_when_memory_value_equal_to_one_negative_range():
	'test of divide method to see how it handles when you pass negative numbers and class is initialized to one'
	_calculator = Calculator(1)
	for a in range(-4, -2):
		if a == -4:
			assert _calculator.divide(a) == -0.25
		elif a == -2:
			assert _calculator.divide(a) == 0.125
		else:
			assert _calculator.divide(a) == 0.08333333333333333

def test_division_when_memory_value_equal_to_negative_one_positive_range():
	'test of divide method to see how it handles when you pass positive numbers and class is initialized to negative one'
	_calculator = Calculator(-1)
	for a in range(2, 4):
		if a == 2:
			assert _calculator.divide(a) == -0.5
		elif a == 4:
			assert _calculator.divide(a) == -0.041666666666666664
		else:
			assert _calculator.divide(a) == -0.16666666666666666

def test_division_when_memory_value_equal_to_negative_one_negative_range():
	'test of divide method to see how it handles when you pass negative numbers and class is initialized to negative one'
	_calculator = Calculator(-1)
	for a in range(-4, -2):
		if a == -4:
			assert _calculator.divide(a) == 0.25
		elif a == -3:
			assert _calculator.divide(a) == -0.08333333333333333
		else:
			assert _calculator.divide(a) == 0.041666666666666664		

def test_root_when_memory_value_equal_to_zero():
	'test of root method to see how it handles when you pass zero to negative one and class is intialized to zero. This checks for interesting cases'
	_calculator = Calculator(0)
	for a in range(-1, 1):
		if a == 0:
			assert _calculator.root(a) == 1
		elif a == -1:
			assert _calculator.root(a) == float("inf") or float("-inf")
		else:
			with pytest.raises(AssertionError):
				assert _calculator.root(a)

def test_root_when_memory_value_equal_to_one_positive_range():
	'test of root method to see how it handles when you pass positive numbers and class is initialized to one'
	_calculator = Calculator(1)
	for a in range(2, 4):
			assert _calculator.root(a) == 1

def test_root_when_memory_value_equal_to_one_negative_range():
	'test of root method to see how it handles when you pass negative numbers and class is initialized to one'
	_calculator = Calculator(1)
	for a in range(-4, -2):
			assert _calculator.root(a) == 1

def test_root_when_memory_value_equal_to_negative_one_positive_range():
	'test of root method to see how it handles complex numbers when you pass positive numbers and class is initialized to negative one'
	_calculator = Calculator(-1)
	for a in range(2, 4):
		if a == 2:
			assert _calculator.root(a) == (6.123233995736766e-17+1j)
		elif a == 3:
			assert  _calculator.root(a) == (0.8660254037844387+0.49999999999999994j)
		else:
			assert _calculator.root(a) == (0.9914448613738104+0.13052619222005157j)

def test_root_when_memory_value_equal_to_negative_one_negative_range():
	'test of root method to see how it handles complex numbers when you pass negative numbers and class is initialized to negative one'
	_calculator = Calculator(-1)
	for a in range(-4, -2):
		if a == -2:
			assert _calculator.root(a) == (6.123233995736766e-17-1j)
		elif a == -3:
			assert  _calculator.root(a) == (0.9659258262890683+0.2588190451025207j)
		else:
			assert _calculator.root(a) == (0.7071067811865476-0.7071067811865475j)