import numpy as np

A1 = np.array([11,33,22,44,66,55])
A2 = np.array([10,30,20,40,60,50])

# 1. Extract elements of array A1 from index 2 to 5
A1_extracted = A1[2:6]
print("Extracted elements from A1: ", A1_extracted)

# 2. Reshape array A1 into (3,2) size
A1_reshaped = A1.reshape(3,2)
print("A1 reshaped into (3,2): \n", A1_reshaped)

# 3. Join arrays A1 and A2
joined_array = np.concatenate((A1, A2))
print("Joined array of A1 and A2: ", joined_array)

# 4. Split array A1 into 3 arrays
A1_split = np.array_split(A1, 3)
print("A1 split into 3 arrays: ")
for i, arr in enumerate(A1_split):
    print(f"Array {i+1}: {arr}")

# 5. Search for number 44 in array A1
index_44 = np.where(A1 == 44)
if len(index_44[0]) > 0:
    print("Index of 44 in A1: ", index_44[0][0])
else:
    print("Number 44 not found in A1.")

# 6. Print all even numbers of array A1 using search option
even_numbers_A1 = A1[A1 % 2 == 0]
print("Even numbers in A1: ", even_numbers_A1)

# 7. Sort the numbers of array A2
A2_sorted = np.sort(A2)
print("A2 sorted: ", A2_sorted)

# 8. Filter odd numbers in array A1 using filter option
odd_numbers_A1 = list(filter(lambda x: x % 2 != 0, A1))
print("Odd numbers in A1: ", odd_numbers_A1)
