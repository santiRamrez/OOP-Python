def factorial(n):
  #Calculate the factorial number of n

  """n int > 0
     return n! 
  """
  if n == 1:
    return 1
  else:
    return n * factorial(n - 1)


test = factorial(4)
print(test)