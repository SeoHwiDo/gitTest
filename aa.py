print("a (operator) b = result")
a = input("Type the value of a : ")
op = input("Type the operator : ")
b = input("Type the value of b : ")

a = float(a)
b = float(b)


if id("+") == id(op):
  def plus(a,b):
    return a + b
  
  result = plus(a,b)

  print("= ", result)

elif id("-") == id(op):
  def minus(a,b):
    return a - b

  result = minus(a,b)

  print("= ", result)

elif id("*") == id(op):
  def mul(a,b):
    return a * b

  result = mul(a,b)

  print("= ", result)

elif id("/") == id(op):
  def div(a,b):
    return a / b

  result = div(a,b)
  
  print("=", result)

elif id("%") == id(op):
  def rem(a,b):
    return a % b

  result = rem(a,b)

  print("= ", result)

elif id("^") == id(op):
    result = pow(a,b)

    print("= ",result)