class Money:
  __value: int
  __currency: str
  def __init__(self, value: int, currency: str) -> None:
    self.__value = value
    self.__currency = currency
  
  @property
  def value(self):
    return self.__value
  
  @property
  def currency(self):
      return self.__currency
  
  def times(self, time: int):
    return Money(self.value * time, self.currency)

  def __eq__(self, other: object) -> bool:
    return self.__value == other.__value and self.currency == other.currency

  

  

  
