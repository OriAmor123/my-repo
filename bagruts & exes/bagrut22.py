arr1 = [2,5,6,6,-4,-3,8,3,3,3]
arr2 = [1,6,8,3,-7,-4,2, 4]
k = len(arr2)
m = len(arr1)

new_arr = []

for i1, i2 in zip(arr1,arr2):
    new_arr.append(i1*i2)

for li in arr1[k:]:
    new_arr.append(li)

print(new_arr)