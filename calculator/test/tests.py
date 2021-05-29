import pytest
from calculator import *
from calculator import Calculator


def test_addition_default():
	_calculator = Calculator()
	for a in range(-1, 1):
		if a == 1:
			assert _calculator.add(a) == 0
		elif a == 0:
			assert _calculator.add(a) == -1
		else:
			assert _calculator.add(a) == -1


def test_addition_positive():
	_calculator = Calculator()
	for a in range(2, 4):
		if a == 2:
			assert _calculator.add(a) == 2
		elif a == 3:
			assert _calculator.add(a) == 5
		else:
			assert _calculator.add(a) == 8


def test_addition_negative():
	_calculator = Calculator()
	for a in range(-4, -2):
		if a == -4:
			assert _calculator.add(a) == -4
		elif a == -3:
			assert _calculator.add(a) == -7
		else:
			assert _calculator.add(a) == -9


def test_subtraction_default():
	_calculator = Calculator()
	for a in range(-1, 1):
		if a == 1:
			assert _calculator.subtract(a) == 0
		elif a == 0:
			assert _calculator.subtract(a) == 1
		else:
			assert _calculator.subtract(a) == 1


def test_subtraction_negative():
	_calculator = Calculator()
	for a in range(-4, -2):
		if a == -4:
			assert _calculator.subtract(a) == 4
		elif a == -3:
			assert _calculator.subtract(a) == 7
		else:
			assert _calculator.subtract(a) == 9


def test_subtraction_positive():
	_calculator = Calculator()
	for a in range(2, 4):
		if a == 2:
			assert _calculator.subtract(a) == -2
		elif a == 0:
			assert _calculator.subtract(a) == -1
		else:
			assert _calculator.subtract(a) == -5


def test_multiplication_default():
	_calculator = Calculator()
	for a in range(-1000, 1000):
		assert _calculator.multiply(a) == 0


def test_multiplication_negative():
	_calculator = Calculator(-1)
	for a in range(-4, -2):
		if a == -4:
			assert _calculator.multiply(a) == 4
		elif a == -3:
			assert _calculator.multiply(a) == -12
		else:
			assert _calculator.multiply(a) == 24


def test_multiplication_positive():
	_calculator = Calculator(1)
	for a in range(2, 4):
		if a == 2:
			assert _calculator.multiply(a) == 2
		elif a == 3:
			assert _calculator.multiply(a) == 6
		else:
			assert _calculator.multiply(a) == 24


def test_division():
	_calculator = Calculator()
	for a in range(-1000, 1000):
		if a == 0:
			with pytest.raises(ZeroDivisionError):
				_calculator.divide(a)
		else:
			assert _calculator.divide(a) == 0


def test_division_default():
	_calculator = Calculator()
	for a in range(-1, 1):
		if a == 0:
			with pytest.raises(ZeroDivisionError):
				_calculator.divide(a)
		elif a == -1:
			assert _calculator.divide(a) == 0
		else:
			assert _calculator.divide(a) == 1			


def test_division_positive():
	_calculator = Calculator(1)
	for a in range(2, 4):
		if a == 2:
			assert _calculator.divide(a) == 0.5
		elif a == 3:
			assert _calculator.divide(a) == 0.16666666666666666
		else:
			assert _calculator.divide(a) == 0.041666666666666664


def test_division_negative():
	_calculator = Calculator(-1)
	for a in range(-4, -2):
		if a == -4:
			assert _calculator.divide(a) == 0.25
		elif a == -3:
			assert _calculator.divide(a) == -0.08333333333333333
		else:
			assert _calculator.divide(a) == 0.041666666666666664


def test_division_default():
	_calculator = Calculator()
	for a in range(-1, 1):
		if a == 0:
			with pytest.raises(ZeroDivisionError):
				_calculator.divide(a)
		elif a == -1:
			assert _calculator.divide(a) == 0
		else:
			assert _calculator.divide(a) == 1			


def test_division_positive():
	_calculator = Calculator(1)
	for a in range(2, 4):
		if a == 2:
			assert _calculator.divide(a) == 0.5
		elif a == 3:
			assert _calculator.divide(a) == 0.16666666666666666
		else:
			assert _calculator.divide(a) == 0.041666666666666664


def test_division_negative():
	_calculator = Calculator(-1)
	for a in range(-4, -2):
		if a == -4:
			assert _calculator.divide(a) == 0.25
		elif a == -3:
			assert _calculator.divide(a) == -0.08333333333333333
		else:
			assert _calculator.divide(a) == 0.041666666666666664


def test_root_negative_numbers():
	for a in range(-1000, 0):
		if a < 0:
			with pytest.raises(ValueError):
				calculator.root(a)
		else:
			assert calculator.root(a) == 0


def test_root_positive_numbers():
	for a in range(0, 1000):
		if a == 0:
			assert calculator.root(a) == 0
		else:
			assert calculator.root(a) > 0


def test_root_default():
	_calculator = Calculator()
	for a in range(-1, 1):
		if a == 0:
			assert _calculator.root(a) == 0
		elif a == -1:
			with pytest.raises(ValueError):
				_calculator.root(a)
		else:
			assert _calculator.root(a) == 1			


def test_root_positive():
	_calculator = Calculator()
	for a in range(2, 4):
		if a == 2:
			assert _calculator.root(a) == 1.4142135623730951
		elif a == 3:
			assert _calculator.root(a) == 1.7320508075688772
		else:
			assert _calculator.root(a) == 2


def test_add_positive_default():
	_calculator = Calculator(1000)
	for a in range(-1000, 1000):
		if a < 0:
			_value = _calculator.add(a)
			if _value < 0:
				assert _value < 0 
			elif _value > 0:		
				assert _value > 0 
			else:
				assert _value == 0
		elif a > 0:
			_value = _calculator.add(a)
			if _value > 0:
				assert _value > 0 
			elif _value < 0:
				assert _value < 0
			else:
				assert _value == 0
		else:
			_value = _calculator.add(a)
			if _value > 0:
				assert _value > 0 
			elif _value < 0:
				assert _value < 0
			else:
				assert _value == 0


def test_subtraction_positive_default():
	_calculator = Calculator(1000)
	for a in range(-1000, 1000):
		if a < 0:
			_value = _calculator.subtract(a)
			if _value < 0:
				assert _value < 0 
			else:
				assert _value > 0 
		elif a > 0:
			_value = _calculator.subtract(a)
			if _value > 0:
				assert _value > 0 
			elif _value < 0:
				assert _value < 0
		else:
			_value = _calculator.subtract(a)
			if _value < 0:
				assert _value < 0 
			else:
				assert _value > 0


def test_multiplication_positive_default():
	for a in range(-1000, 1000):
		_calculator = Calculator(1000)
		if a < 0:
			assert _calculator.multiply(a) < 0
		elif a > 0:
			assert _calculator.multiply(a) > 0
		else:
			assert _calculator.multiply(a) == 0


def test_division_positive_default():
	for a in range(-1000, 1000):
		_calculator = Calculator(1000)
		if a == 0:
			with pytest.raises(ZeroDivisionError):
				_calculator.divide(a)
		elif a > 0:
			assert _calculator.divide(a) > 0
		else:
			assert _calculator.divide(a) < 0


def test_add_negative_default():
	_calculator = Calculator(-1000)
	for a in range(-1000, 1000):
		if a < 0:
			_value = _calculator.add(a)
			if _value < 0:
				assert _value < 0 
			elif _value < 0:		
				assert _value > 0 
			else:
				assert _value == 0
		elif a > 0:
			_value = _calculator.add(a)
			if _value > 0:
				assert _value > 0 
			elif _value < 0:
				assert _value < 0
			else:
				assert _value == 0
		else:
			_value = _calculator.add(a)
			if _value > 0:
				assert _value > 0 
			elif _value < 0:
				assert _value < 0
			else:
				assert _value == 0


def test_subtraction_negative_default():
	_calculator = Calculator(-1000)
	for a in range(-1000, 1000):
		if a < 0:
			_value = _calculator.subtract(a)
			if _value < 0:
				assert _value < 0 
			elif _value > 0:		
				assert _value > 0 
			else:
				assert _value == 0
		elif a > 0:
			_value = _calculator.subtract(a)
			if _value > 0:
				assert _value > 0 
			elif _value < 0:
				assert _value < 0
			else:
				assert _value == 0
		else:
			_value = _calculator.subtract(a)
			if _value > 0:
				assert _value > 0 
			elif _value <= 0:
				assert _value <= 0


def test_multiplication_negative_default():
	for a in range(-1000, 1000):
		_calculator = Calculator(-1000)
		if a < 0:
			assert _calculator.multiply(a) > 0
		elif a > 0:
			assert _calculator.multiply(a) < 0
		else:
			assert _calculator.multiply(a) == 0


def test_division_negative_default():
	for a in range(-1000, 1000):
		_calculator = Calculator(-1000)
		if a == 0:
			with pytest.raises(ZeroDivisionError):
				_calculator.divide(a)
		elif a > 0:
			assert _calculator.divide(a) < 0
		else:
			assert _calculator.divide(a) > 0


def test_multiplication_positive_default_instantiation_before():
	_calculator = Calculator(1000)
	for a in range(-1000, 1000):
		if a < 0:
			_value = _calculator.multiply(a)
			if _value < 0:
				assert _value < 0 
			else:
				assert _value > 0 
		elif a > 0:
			_value = _calculator.multiply(a)
			if _value > 0:
				assert _value > 0 
			elif _value < 0:
				assert _value < 0
		else:
			assert _calculator.multiply(a) == 0


def test_division_positive_default_instantiation_before():
	_calculator = Calculator(1000)
	for a in range(-1000, 1000):
		if a == 0:
			with pytest.raises(ZeroDivisionError):
				_calculator.divide(a)
		elif a > 0:
			_value = _calculator.multiply(a)
			if _value < 0:
				assert _value < 0 
			else:
				assert _value > 0 
		else:
			_value = _calculator.multiply(a)
			if _value < 0:
				assert _value < 0 
			else:
				assert _value > 0 
				

def test_multiplication_negative_default_instantiation_before():
	_calculator = Calculator(-1000)
	for a in range(-1000, 1000):
		if a < 0:
			_value = _calculator.multiply(a)
			if _value < 0:
				assert _value < 0 
			else:
				assert _value > 0 
		elif a > 0:
			_value = _calculator.multiply(a)
			if _value > 0:
				assert _value > 0 
			elif _value < 0:
				assert _value < 0
		else:
			assert _calculator.multiply(a) == 0
			

def test_division_negative_default_instantiation_before():
	_calculator = Calculator(-1000)
	for a in range(-1000, 1000):
		if a == 0:
			with pytest.raises(ZeroDivisionError):
				_calculator.divide(a)
		elif a > 0:
			_value = _calculator.multiply(a)
			if _value < 0:
				assert _value < 0 
			else:
				assert _value > 0 
		else:
			_value = _calculator.multiply(a)
			if _value < 0:
				assert _value < 0 
			else:
				assert _value > 0
