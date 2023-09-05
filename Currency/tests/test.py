import pytest
import sys, os

test_files_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..', 'src')
sys.path.append(test_files_path)
from MoneyFactory import MoneyFactory
from Bank import Bank

def test_multiply():
  five = MoneyFactory.dollar(5)
  product = five.times(2)
  assert product == MoneyFactory.dollar(10)

def test_equal():
  assert MoneyFactory.dollar(5) != MoneyFactory.franc(5)
  assert MoneyFactory.dollar(5) != MoneyFactory.dollar(6)
  assert MoneyFactory.dollar(5) == MoneyFactory.dollar(5)

def test_currency():
  assert "USD" == MoneyFactory.dollar(1).currency
  assert "CHF" == MoneyFactory.franc(1).currency

def test_change():
   five_doll = MoneyFactory.dollar(5)
   Bank.add_rate("USD", "CHF", 1/2)
   ten_franc = Bank.exchange(five_doll, "CHF")
   assert MoneyFactory.franc(10) == ten_franc

def test_plus_same():
  Bank.add_rate("CHF", "USD", 2)
  sum = Bank.reduce(MoneyFactory.dollar(5),MoneyFactory.franc(10), "USD")
  assert MoneyFactory.dollar(10) == sum

def test_print():
  print("OK1")
