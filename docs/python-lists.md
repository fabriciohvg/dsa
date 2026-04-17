# Python Lists

A list is a mutable, ordered collection that can hold items of any type.

## Creating Lists

```python
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]
from_range = list(range(5))  # [0, 1, 2, 3, 4]
```

## Accessing Elements

```python
fruits = ["apple", "banana", "cherry", "date"]

fruits[0]    # "apple"       — first element
fruits[-1]   # "date"        — last element
fruits[1:3]  # ["banana", "cherry"] — slicing
fruits[::2]  # ["apple", "cherry"]  — step
fruits[::-1] # reversed list
```

## Modifying Lists

```python
nums = [1, 2, 3]

# Add
nums.append(4)          # [1, 2, 3, 4]
nums.insert(0, 0)       # [0, 1, 2, 3, 4]
nums.extend([5, 6])     # [0, 1, 2, 3, 4, 5, 6]

# Remove
nums.pop()              # removes & returns last item
nums.pop(0)             # removes & returns item at index
nums.remove(3)          # removes first occurrence of 3
del nums[0]             # delete by index
nums.clear()            # remove all items
```

## Common Operations

```python
letters = ["b", "a", "d", "c"]

len(letters)            # 4
letters.sort()          # sorts in place → ["a", "b", "c", "d"]
letters.reverse()       # reverses in place
sorted(letters)         # returns new sorted list (original unchanged)
letters.index("c")      # index of first occurrence
letters.count("a")      # number of occurrences
"a" in letters          # True — membership check
```

## List Comprehensions

A concise way to create lists from existing iterables.

```python
squares = [x ** 2 for x in range(6)]
# [0, 1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

flat = [x for row in [[1, 2], [3, 4]] for x in row]
# [1, 2, 3, 4]
```

## Unpacking

```python
first, *rest = [1, 2, 3, 4]
# first = 1, rest = [2, 3, 4]

a, b, c = [10, 20, 30]
```

## Copying

```python
original = [1, [2, 3]]

shallow = original.copy()        # or original[:]
import copy
deep = copy.deepcopy(original)   # independent nested copy
```

## Useful Patterns

```python
# Iterate with index
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)

# Zip two lists together
names = ["Alice", "Bob"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(name, score)

# Filter + map
nums = [1, -2, 3, -4, 5]
positive_doubled = [x * 2 for x in nums if x > 0]
# [2, 6, 10]
```

## Time Complexity (Big O)

| Operation              | Complexity     |
| ---------------------- | -------------- |
| Access by index        | O(1)           |
| Append                 | O(1) amortized |
| Insert/Delete at index | O(n)           |
| Search (`in`)          | O(n)           |
| Sort                   | O(n log n)     |
| `len()`                | O(1)           |
