theList = [3, 4, 6, 10, 43, 23, 22, 21, 99, 53, 35, 21, 1, 2, 9, 50]

def linearSearch(arr, val):
  for i in range(0, len(arr)):
    if arr[i] == val:
      return f'we found the value: {val} at the index: {i}'
    if i == len(arr) - 1:
      return 'not found'

test = linearSearch(theList, 100)
print(test)