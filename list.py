a=[10,20,30,40,50]
sum = 0
min_value = a[0]

for i in range(len(a)):
    print("a[",i,"]=",a[i])
    sum = sum+a[i]

    if(a[i]<min_value):
        min_value = a[i]
print("min value", min_value)
print("total = ",sum)
