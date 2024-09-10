def find_missing():
    nums = input("Provide the numbers separated by spaces: ")
    nums_list = nums.split()
    arr = [int(i) for i in nums_list]
    total_count = len(arr) + 1

    expected_sum = total_count * (total_count + 1) // 2
    current_sum = sum(arr)
    missing_val = expected_sum - current_sum

    full_range = set(range(1, total_count + 1))
    provided_nums = set(arr)
    missing_elements = full_range - provided_nums

    if len(missing_elements) > 1:
        return "Error: More than one number is missing."
    elif len(missing_elements) == 0:
        return "Error: No number is missing."
    
    return missing_val

result = find_missing()
print(f"The missing number is: {result}")
