def linear_search(arr, key):
    for item in arr:
        if item == key:
            return True
    return False

arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter key to search: "))
print("Found" if linear_search(arr, key) else "Not Found")
