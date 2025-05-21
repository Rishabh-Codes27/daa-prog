def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False

arr = sorted(list(map(int, input("Enter sorted elements: ").split())))
key = int(input("Enter key to search: "))
print("Found" if binary_search(arr, key) else "Not Found")
