nums = [3,2,3]
target = 6

def twoSum(nums, target):
  for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[y] == target - nums[x]:
                  print(f"input: nums = {nums}, target = {target}")
                  print(f"output: [{x},{y}]")
                  print(f"explanation: sum of {nums[x]} (nums[{x}]) + {nums[y]} (nums[{y}]) = {target}")
                  return [x,y]
  # an empty list if no solution is found
  print(">> There is no two sum in this array.")
  return []

twoSum(nums, target)
