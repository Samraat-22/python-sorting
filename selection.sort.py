class sorting:
    def sortarray(self,num):
        n=len(num)
        for i in range(n):
            min=num[i]
            index=i
            for j in range(i+1,n):
                if num[j]<min:
                    min=num[j]
                    index=j
                    temp=num[i]
                    num[i]=num[index]
                    num[index]=temp


        return num
num = list(map(int, input("Enter numbers separated by spaces: ").split()))

obj = sorting()

result = obj.sortarray(num)

print("Sorted array:", result)

        
