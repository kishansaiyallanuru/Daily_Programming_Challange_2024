def find_duplicate(numbers):
    slow = numbers[0]
    fast = numbers[0]
    
    while True:
        slow = numbers[slow]
        fast = numbers[numbers[fast]]
        if slow == fast:
            break
    
    slow = numbers[0]
    while slow != fast:
        slow = numbers[slow]
        fast = numbers[fast]
    
    return fast

input_data = input("Enter the numbers separated by spaces: ")
array = input_data.split()
array = [int(num) for num in array]

n = len(array)
unique_numbers = set(array)

if len(unique_numbers) != len(array):
    print("The duplicate number is:", find_duplicate(array))
else:
    print("Invalid input! Please ensure there is at least one duplicate.")
