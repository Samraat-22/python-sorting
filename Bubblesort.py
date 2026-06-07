class Sorting:
    def sortarray(self, num):
        n = len(num)

        for i in range(n):
            for j in range(n - i - 1):
                if num[j] > num[j + 1]:
                    # swap
                    temp = num[j]
                    num[j] = num[j + 1]
                    num[j + 1] = temp

        return num



arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

# object creation
obj = Sorting()


result = obj.sortarray(arr)

print("Sorted array:", result)