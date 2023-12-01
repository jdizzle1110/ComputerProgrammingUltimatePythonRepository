def calculator(equation): 
  n1, op, n2 = equation.split(" ")

  n1 = int(n1)
  n2 = int(n2)
  
  if op == "+":
    return n1 + n2
  elif op == "-":
    return n1 - n2
  elif op == "*":
    return n1 * n2 
  elif op == "/":
    return n1 / n2 



print("Enter math equation")
equation = input()
print(calculator(equation))

