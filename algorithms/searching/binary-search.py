# We try to find the square root

target = int(input("Please type a number: "))
lowest = 0.0
epsilon = 0.01 #In case the choosen number does not have an exact square root, we want to get as closest as possible.
highest = max(1.0, target)
output = (highest + lowest) / 2 #the middle point

while abs(output**2 - target) >= epsilon:
  if output**2 < target:
    lowest = output
  else:
    highest = output

  output = (highest + lowest) / 2 #the middle point

  print(f'Lowest: {lowest} - Output: {output} - Highest: {highest}')

#This algorithm is faster for sqr roots that are not exact like 7
#end it is slower for sqr root that are axact, like 9.