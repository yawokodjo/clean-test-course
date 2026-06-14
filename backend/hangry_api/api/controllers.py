from typing import Any

class Delivery():
  @staticmethod
  def calculate(order: list[Any], distance: float) -> float:
    items = 0
    for item in order:
      items += item.quantity
    if items > 10 and distance > 5:
      return 7.50
    elif items > 5 and distance > 3:
      return 5
    else:
      return 2.5

class Subtotal():
  @staticmethod
  def calculate(order: list[Any]) -> float:
    cost = 0
    for item in order:
      cost += item.quantity * item.item.price
    return cost

class Tax():
  @staticmethod
  def calculate(subTotal: float, deliveryFee: float) -> float:
    tax = (subTotal + deliveryFee) * 0.0825
    return (0,round(tax,2)) [ round(tax,2) > 0 ]

#Completed Total
class Total():
  @staticmethod
  def calculate(order: list[Any], deliveryFee: float) -> float:
    subTotal = Subtotal.calculate(order)
    total = (subTotal + deliveryFee) * 1.0825
    return (0,round(total,2)) [ round(total,2) > 0 ]
