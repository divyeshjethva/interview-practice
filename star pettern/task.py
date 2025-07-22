
# s = "123456789"
# v = len(s)//2
# print(int(s[0]) + int(s[v]) + int(s[-1]))

# ------------------------------------------

# for i in range(1,6):
#     for j in range(i):
#         print("*",end='')
#     print()
# ------------------------------

# for i in range(1,6):
#     for j in range(6-i):
#         print(" ",end="")
#     for n in range(i):
#         print("*",end='')
#     print()

# --------------------------------

# for i in range(1,6):
#     for j in range(6-i):
#         print(" ",end='')
#     for n in range(i):
#         print("*",end=" ")
#     print()
    
# --------------------------------

# for i in range(1,6):
#     for j in range(6-i):
#         print("*", end="")
#     print()
    
# --------------------------------

# for i in range(1,6):
#     for j in range(i):
#         print(" ",end='')
#     for n in range(6-i):
#         print("*",end="")
#     print()

# --------------------------------

# for i in range(1,6):
#     for j in range(i):
#         print(" ",end='')
#     for n in range(6-i):
#         print("*",end=" ")
#     print()
        
# --------------------------------

for i in range(1,6):
    for n in range(6-i):
        print(" ",end='')
    for j in range(1,i+1):
        print(j,end=' ')
    print()