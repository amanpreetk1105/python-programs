num = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 123]
max = num[0]
for i in range(len(num)-1):
        if i!= len(num):            
            if (max>num[i+1]):
             continue #max = num[i]
            
            else:
                max = num[i+1]
print(f"{max} is greatest")