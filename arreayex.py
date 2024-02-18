num = ['1', '5', '7', '3']
for x in num:
    print (x)
new = []
a=0
b=1
while range(len(num)):
    while range(len(num)):
        if num[a]>num[b]:
            max=num[a]
            

        else:
            d=num[a]
            e=num[b]
            i=d
            d=e
            e=i
            new.append(e)
        b+=1
    new.append(max)
    a+=1
print(new)