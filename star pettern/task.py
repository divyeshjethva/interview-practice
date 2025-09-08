
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

# for i in range(1,6):
#     for n in range(6-i):
#         print(" ",end='')
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# --------------------------
# n = 1
# for row in range(1, 6):
#     for col in range(row):
#         if n == 1:
#             print("d",end=' ')
#         elif n == 5:
#             print("i",end=' ')
#         elif n == 11:
#             print("v",end=' ')
#         elif n == 15:
#             print("y",end=' ')
#         else:
#             print("*", end=' ')
#         n += 1
#     print()

# --------------------------
n = 15
for i in range(1,6):
    for j in range(6-i):
        if n == 12:
            print("D",end=' ')
        elif n == 5:
            print("I",end=' ')
        else:
            print("*",end=' ')
        n -=1
    print()