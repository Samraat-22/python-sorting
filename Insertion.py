class sorting:
    def sortarray(self, num):
        n = len(num)

        for i in range(1, n):
            key = num[i]
            j = i - 1

            while j >= 0 and num[j] > key:
                num[j + 1] = num[j]
                j = j - 1

            num[j + 1] = key

        return num


num = list(map(int, input("Enter numbers separated by spaces: ").split()))

obj = sorting()

result = obj.sortarray(num)

print("Sorted array:", result)