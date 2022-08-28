# We try to find the closest number of a non exact square root

target = int(input('Type a number to find its sqr root: '))
epsilon = 0.01 # How close we want to arrive
step = epsilon**2
output = 0.0

while abs(output**2 - target) >= epsilon:
  output += step

if abs(output**2 - target) >= epsilon:
  print(f'there is not sqr root of {target}')
else:
  print(f'the sqr root of {target} is {output}') 