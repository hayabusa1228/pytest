from Money import Money

class MoneyFactory:
  @staticmethod
  def dollar(value: int):
    return Money(value,"USD")
  
  @staticmethod
  def franc(value: int):
    return Money(value,"CHF")