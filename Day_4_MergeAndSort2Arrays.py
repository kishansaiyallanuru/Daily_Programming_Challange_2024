def merge_and_split(arr1, arr2):
    merged_array = arr1 + arr2
    merged_array.sort()
    return merged_array[:len(arr1)], merged_array[len(arr1):]

arr1 = input("Enter elements of arr1: ").split()
arr1 = [int(num) for num in arr1]

arr2 = input("Enter elements of arr2: ").split()
arr2 = [int(num) for num in arr2]

first_half, second_half = merge_and_split(arr1, arr2)

print(first_half)
print(second_half)
