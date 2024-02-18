num = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(num)):
    for j in range(i+1, len(num)):
        if (num[i]>num[j]):
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
print(num)