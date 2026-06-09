def binarysearch_iterative(num, target):
    n = len(num)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if num[mid] == target:
            return mid
        elif num[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binarysearch_recursive(num, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if num[mid] == target:
        return mid
    elif num[mid] < target:
        return binarysearch_recursive(num, mid + 1, high, target)
    else:
        return binarysearch_recursive(num, low, mid - 1, target)

# These lines now have explicit prompt messages
user_list = sorted([int(x) for x in input("Enter numbers separated by spaces: ").split()])
user_target = int(input("Enter the target number to search for: "))

iterative_result = binarysearch_iterative(user_list, user_target)
recursive_result = binarysearch_recursive(user_list, 0, len(user_list) - 1, user_target)

print("Iterative Search Index:", iterative_result)
print("Recursive Search Index:", recursive_result)