def merge_sort(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left_array = arr[:mid]
    right_array = arr[mid:]
    
    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)
    
    return merge_array(left_array, right_array)

def merge_array(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)
    
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    while i < n:
        result.append(left[i])
        i += 1
        
    while j < m:
        result.append(right[j])
        j += 1
        
    return result

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    nums = [int(x) for x in user_input.split()]
    
    print("Original:", nums)
    sorted_nums = merge_sort(nums)
    print("Sorted:  ", sorted_nums)