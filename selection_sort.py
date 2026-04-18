array = [156, 141, 35, 94, 88, 35, 111]

def findSmallest(array):
  smallest_index = 0

  for i in range(1, len(array)):
    if array[i] < array[smallest_index]:
      smallest_index = i
  return smallest_index

def selectionSort(array):
  asc_sorted_array = []
  copy_array = list(array)    # copy array before mutating

  for i in range(len(copy_array)):
    smallest_index = findSmallest(copy_array)
    asc_sorted_array.append(copy_array.pop(smallest_index))   # .pop(i) removes and returns item at index
  return asc_sorted_array

print(selectionSort(array))
