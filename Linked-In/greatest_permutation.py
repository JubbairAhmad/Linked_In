def next_nearest_greater_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    arr[i]
    if i >= 0:
        j = len(arr) - 1
        while arr[j] < arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    
arr = [1, 2, 3]
next_nearest_greater_permutation(arr)
print("Next Nearest Greater Permutation:", arr)
