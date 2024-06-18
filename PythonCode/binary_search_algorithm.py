def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def main():
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = binary_search(arr, x)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")

if __name__ == "__main__":
    main()
