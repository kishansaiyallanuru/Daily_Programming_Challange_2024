def find_zero_sum_subarrays(arr):
    sum_map = {}
    result = []
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum == 0:
            result.append((0, i))
        
        if current_sum in sum_map:
            for start_index in sum_map[current_sum]:
                result.append((start_index + 1, i))
        
        if current_sum in sum_map:
            sum_map[current_sum].append(i)
        else:
            sum_map[current_sum] = [i]
    
    return result

arr = list(map(int, input("Enter the array elements separated by commas: ").split(',')))

subarrays = find_zero_sum_subarrays(arr)
print("Subarrays with zero sum:", subarrays)
