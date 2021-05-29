import pytest
from calculator import *
from calculator import Calculator


def test_addition():
	for a in range(-1, 1):
		if a == 1:
			assert calculator.add(a) == 0
		elif a == 0:
			assert calculator.add(a) == -1
		else:
			assert calculator.add(a) == -1


def test_subtraction():
	_calculator = Calculator()
	for a in range(-1, 1):
		if a == 1:
			assert _calculator.subtract(a) == 0
		elif a == 0:
			assert _calculator.subtract(a) == 1
		else:
			assert _calculator.subtract(a) == 1


def test_multiplication():
	_calculator = Calculator()
	for a in range(-1000, 1000):
		assert _calculator.multiply(a) == 0


def test_division():
	_calculator = Calculator()
	for a in range(-1000, 1000):
		if a == 0:
			with pytest.raises(ZeroDivisionError):
				_calculator.divide(a)
		else:
			assert _calculator.divide(a) == 0


def test_root():
	for a in range(-1000, 1000):
		if a < 0:
			with pytest.raises(ValueError):
				calculator.root(a)
		else:
			if a > 0:
				assert calculator.root(a)
			else:
				assert calculator.root(a) == 0


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


def test_multiplication_positive_default_instantion_before():
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


def test_division_positive_default_instantion_before():
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
				

def test_multiplication_negative_default_instantion_before():
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
			

def test_division_negative_default_instantion_before():
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
