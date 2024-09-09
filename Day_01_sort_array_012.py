def sortarray(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 1:
            mid += 1

        elif arr[mid] == 0:
            temp = arr[low]
            arr[low] = arr[mid]
            arr[mid] = temp
            low += 1
            mid += 1

        else:
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
            high -= 1

def check_array(arr):
    for x in arr:
        if x not in (0, 1, 2):
            return False
    return True



input_str = input("Enter the array elements separated by spaces: ")
arr = []
for x in input_str.split():
    arr.append(int(x))
if not check_array(arr):
    print("Error only 0 1 2 are allowed")
else:
    sortarray(arr)
    print(arr)
