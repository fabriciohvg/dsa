def binary_search(arr, item):
  low = 0               # lowest index
  high = len(arr) -1    # highest index
  
  while low <= high:          # loop at least on time until worst case or not found
    mid = (low + high) // 2   # mid value rounded down by `//` if not even
    guess = arr[mid]          # the value of the array at index = mid
    
    if guess == item:
      print(f">> found it! /o/ >> it is on index [{mid}]")
      return mid
    elif guess > item:
      high = mid - 1
      print(f"guess (({guess})) is higher than (({item}))... setting new 'high' >> {high}")
    else:
      low = mid + 1
      print(f"guess (({guess})) is lower than (({item}))... setting new 'low' >> {low}")
      
  return None                 # means `null` in Python; the item wasn´t found

my_list = [1, 3, 5, 9, 11, 14]

binary_search(my_list, 1)
# print(binary_search(my_list, -1))