def binary_search(arr):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            first = mid + 1
        else:
            last = mid - 1
    return -1

# Example sorted array where element equals index at index 3
array = [-10, -5, 0, 3, 7]

print(binary_search(array))  # Should print 3 because arr[3] == 3
