import random

def binary_search(data, target):
  low = 0
  high = len(data) - 1
  count = 0
  while low <= high:
    count = count + 1
    mid = (low + high) // 2
    if target == data[mid]:
      return mid, count
    elif target < data[mid]:
      high = mid - 1
    else:
      low = mid + 1

  # return the index as well as the count
  return -1, count

# initiate a array with random integers
data = [3, 28, 37, 44, 53, 62, 75, 86, 99, 100]
sorted_data = sorted(data)
target_num_1_index = random.randint(0, len(data) - 1)
target_num_2_index = random.randint(0, len(data) - 1)
target_num_1 = sorted_data[target_num_1_index]
target_num_2 = sorted_data[target_num_2_index] - 100 # Target number that is not in the array

searched_result_1 = binary_search(data, target_num_1)
searched_result_2 = binary_search(data, target_num_2)

print(f"Target number 1: {target_num_1}")
print(f"Target number 1 index: {searched_result_1[0]}")
print(f"Count of Target number 1: {searched_result_1[1]}")

print(f"Target number 2: {target_num_2}")
print(f"Target number 2 index: {searched_result_2[0]}")
print(f"Count of Target number 2: {searched_result_2[1]}")