
# s = input("Enter name :")

# a = len(s) // 2

# if len(s)%2 == 0:
#     print("enter odd string")
# else:
#     print( s[a-1] + s[a] + s[a+1])

# ================================

# vowels = "aeiou"

# user = input("enter name :")
# total = 0

# for i in user:
#     if i in vowels:
#         total += 1
# print("total vowes is :", total)

# ================================

# user = input("Enter name :")

# reverse = user[::-1]

# if user==reverse:
#     print("pelidrom")
# else:
#     print("not")

# ================================

a = input("enter to check armstrong number :")
sum = 0
d = 1
for i in a:
    d = int(i) * int(i) * int(i)
    sum += d

if int(a)==sum:
    print("armstrong")
else:
    print("not")