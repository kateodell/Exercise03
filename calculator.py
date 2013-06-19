import arithmetic

while True:
  # read input
  problem = raw_input("enter your problem: ")
  # tokenize input
  tokens = problem.split(" ")
  if len(tokens) > 1:
    num1 = float(tokens[1])
  if len(tokens) > 2:
    num2 = float(tokens[2])

  # if the first token is 'q', quit
  if tokens[0] == "q":
    print "goodbye!"
    break
  # otherwise decide which math function to call based on the tokens we read
  if tokens[0] == '+':
    print arithmetic.add(num1, num2)
  elif tokens[0] == '-':
    print arithmetic.subtract(num1, num2)
  elif tokens[0] == '*':
    print arithmetic.multiply(num1, num2)
  elif tokens[0] == '/':
    print arithmetic.divide(num1, num2)
  elif tokens[0] == 'square':
    print arithmetic.square(num1)
  elif tokens[0] == 'cube':
    print arithmetic.cube(num1)
  elif tokens[0] == 'pow':
    print arithmetic.power(num1, num2)
  elif tokens[0] == 'mod':
    print arithmetic.mod(num1, num2)