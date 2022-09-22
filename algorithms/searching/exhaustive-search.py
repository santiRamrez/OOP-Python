my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def exhaustive(val, list):
  indx = 0
  found = False
  output = None
  for n in list: #it will search from the 0 index to the last index at the right
    if n == val:
      found = True
      output = indx
    indx += 1
  if found:
    print(f'The number {val} is at the index {output}')
  else:
    print(f'There is not {val} within the list')

# exhaustive(20, my_list)  ---> The number 20 is at the index 19




