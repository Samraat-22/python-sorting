def partition(num, low, high):
    pivot = num[low]
    i, j = low, high
    
    while i < j:
        while num[i] <= pivot and i <= high - 1:
            i = i + 1
        while num[j] > pivot and j >= low + 1:
            j = j - 1
        if i < j:
            num[i], num[j] = num[j], num[i]
            
    num[low], num[j] = num[j], num[low]
    return j

def quick_sort(num, low, high):
    if low < high:
        p_index = partition(num, low, high)
        quick_sort(num, low, p_index - 1)
        quick_sort(num, p_index + 1, high)

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    nums = [int(x) for x in user_input.split()]
    
    print("Original:", nums)
    quick_sort(nums, 0, len(nums) - 1)
    print("Sorted:  ", nums)