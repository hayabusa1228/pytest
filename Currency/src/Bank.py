from Money import Money

class Bank:
  __rate_table = []
  @classmethod
  def exchange(self,money: Money, to: str):
    for info in self.__rate_table:
      if info[0:2] == [money.currency, to]:
        return Money(money.value/info[2], to)
    
    raise ValueError(f'please add rate info in advance')

  @classmethod
  def add_rate(self,origin : str, to: str, rate: int):
    self.__rate_table.append([origin,to,rate])
  
  @classmethod
  def reduce(self,money1: Money, money2: Money, currency: str):
    #exchange
    if money1.currency != currency:
      money1 = self.exchange(money1, currency)
    if money2.currency != currency:
      money2 = self.exchange(money2, currency)
    return Money(money1.value+money2.value, currency)

