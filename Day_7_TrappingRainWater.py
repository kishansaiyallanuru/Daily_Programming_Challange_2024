def trap(height):
    n = len(height)
    if n == 0:
        return 0

    left, right = 0, n - 1
    left_max, right_max = height[left], height[right]
    trapped_water = 0

    while left < right:
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            trapped_water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            trapped_water += right_max - height[right]

    return trapped_water

height = list(map(int, input().split()))
output = trap(height)
print(output)
