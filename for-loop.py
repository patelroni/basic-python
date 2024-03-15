# pattern no 7
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()
# for p in range(5,1,-1):
#     for q in range(1,p):
#         print(q,end='')
#     print()

# pattern no 8
# for i in range(0,6):
#     for j in range(i+1,6):
#         print(j,end='')
#     print()
# for p in range(5,0,-1):
#     for q in range(5,p-1,-1):
#         print(q,end='')
#     print()

# pattern no 10 
# for i in range(1,6):
#     for j in range(i,i+1):
#         print(j,end=' ')
#     print(i+10, i+20)

# pattern no 9
# k=1
# for i in range(1,6):
#     for j in range(1,1+1 ):
#         print(k, end='')
#         k=k*11                                                                                     
#     print()


# pattern no 11 (diamond pattern)
# a=5
# for i in range(0,5):
#     for j in range(0,a):
#         print(end=' ')
#     a = a-1
#     for k in range(0,i+1):
#         print("*", end=' ')
#     print()
# for p in range(5,-1,-1):
#     for q in range(a,0,-1):
#         print(end=' ')
#     a = a+1
#     for r in range(0,p+1):
#         print("*", end=' ')
#     print()

# pattern no 1 with space
# a=5
# for i in range(0,6):
#     for p in range(0,a):
#         print(end=' ')
#     a=a-1
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

# pattern no 2 with space
# a=5
# for i in range(0,6):
#     for p in range(0,a):
#         print(end=' ')
#     a=a-1
#     for j in range(1,i+1):
#         print(j%2,end='')
#     print()

# pattern no 3 with space
# a=4
# for i in range(5,0,-1):
#     for p in range(0,a):
#         print(end=' ')
#     a=a-1
#     for j in range(5,i-1,-1):
#         print(j,end='')
#     print()

# pattern n0 4 with space
# a=0
# for i in range(5,0,-1):
#     for k in range(a,0,-1):
#         print(end=' ')
#     num = i
#     a=a+1
#     for j in range(0,i):
#         print(num, end='')
#     print()

# pattern no 5 with space
# a=0
# for i in range(0,6):
#     for k in range(a,0,-1):
#         print(end=' ')
#     a=a+1
#     for j in range(i+1,6):
#         print(j,end='')
#     print()

# pattern no 6 with space
# a=0
# for i in range(6,1,-1):
#     for k in range(a,0,-1):
#         print(end=' ')
#     a=a+1
#     for j in range(1,i):
#         print(j, end='')
#     print()

# pattern no 7 reverse space
# a=5
# for i in range(1,6):
#     for k in range(0,a):
#         print(end=' ')
#     a=a-1
#     for j in range(1,i+1):
#         print(j,end='')
#     print()
# a=1
# for p in range(6,1,-1):
#     for k in range(a,0,-1):
#         print(end=' ')
#     a=a+1
#     for q in range(1,p):
#         print(q,end='')
#     print()

# pattern no 8 reverse space
# a=0
# for i in range(0,6):
#     for k in range(0,a):
#         print(end=' ')
#     a=a+1
#     for j in range(i+1,6):
#         print(j,end='')
#     print()
# r=4
# for p in range(5,0,-1):
#     for k in range(r,0,-1):
#         print(end=' ')
#     r=r-1
#     for q in range(5,p-1,-1):
#         print(q,end='')
#     print()

# pattern no 9 reverse space
k=1
a=4
for i in range(1,6):
    for p in range(a,0,-1):
        print(end=' ')
    a=a-1
    for j in range(1,1+1 ):
        print(k, end='')
        k=k*11                                                                                     
    print()