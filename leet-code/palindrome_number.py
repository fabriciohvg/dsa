x = 121

items = str(x)  # convert the integer to a string
counter = len(items) - 1

print(items[::-1]) # reversed list

# another approach: check last item item[-1] and item.pop() ... loop

for i in range(len(items)):
  if i < (counter):
    if items[i] == items[counter]:
      counter = counter - 1
    else:
      print(False)
      exit()
print(True)
