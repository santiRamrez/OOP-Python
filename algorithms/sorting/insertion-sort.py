theList = [3, 4, 6, 10, 43, 23, 22, 21, 99, 53, 35, 21, 1, 2, 9, 50]

def insertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i] #second index
    left = i - 1
    while left >= 0 and arr[left] > key:
      arr[left + 1] = arr[left]
      left -= 1
      print(f'Position: {i} -- Key{key} -- arr {arr}')
    arr[left + 1] = key
    
  
# test = insertionSort(theList)
# print(test)

insertionSort(theList)

