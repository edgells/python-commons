def binary_search(list, item):
    low = 0
    high = len(list) -1
    while low <= high:
        mid = (high - low ) // 2 + low
        guess = list[mid]
        if guess > item:
            high = mid -1
        elif guess < item:
            low = mid + 1
        else:
            return mid
    return None


l1 = [1,3,5,7,9]


print(binary_search(l1, 7))
