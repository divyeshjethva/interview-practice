
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

# a = input("enter to check armstrong number :")
# sum = 0
# d = 1
# for i in a:
#     d = int(i) * int(i) * int(i)
#     sum += d

# if int(a)==sum:
#     print("armstrong")
# else:
#     print("not")

# ================================

# a = 0
# b = 1
# user = int(input("Enter num :"))
# arr = []
# for i in range(user):
#     arr.append(a)
#     a,b = b, a+b
    
# print(arr)

# ================================
# n = 5
# for i in range(1,n+1):
#     print("*" * i)

# --------------------------

# n = 6
# for i in range(1,n):
#     print(" " * (n-i) ,"*" * i)
# --------------------------

# n = 6
# for i in range(1,n):
#     print(" " * (n-i) ," *" * i)
# --------------------------

# n = 6
# for i in range(1,n):
#     print("*" * (n-i))
# --------------------------

# n = 6
# for i in range(1,n):
#     print(" " * i ,"*" * (n-i))
# --------------------------


# n = 6
# for i in range(1,6):
#     print(" "*i, "* " * (n-i))

# ====================================

# l = [1,2,3,1,2]
# l1 = []
# l2 = []

# for i in l:
#     if i in l1:
#         l2.append(i)
#     else:
#         l1.append(i)

# print(l1)
# print(l2)

# ====================================

# d = {}
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]

# for i in range(len(l1)):
#     d[l1[i]] = l2[i]
    
# print(d)
# ====================================

# a = 10
# b = 20

# print("before",a)
# print("before",b)

# a,b = b,a

# print("after",a)
# print("After",b)
# -------------------------------

# a = 10
# b = 20

# print("before",a)
# print("before",b)

# temp = a
# a = b
# b = temp

# print("after",a)
# print("After",b)
# ----------------------

# a = 10
# b = 20

# print("before",a)
# print("before",b)

# a = a + b
# b = a - b
# a = a - b

# print("after",a)
# print("After",b)

# ================================

# name = "ajay"
# d = {}

# for i in name:
#     if i in d:
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
# print(d)

# =============================

# num1 = int(input("Enter number"))
# num2 = int(input("Enter number"))
# oparation = input("Enter perform")

# if oparation == "+":
#     print(num1+num2)
# elif oparation == "-":
#     print(num1-num2)
    
# =============================

# even = []
# odd = []

# for i in range(4):
#     num = int(input("Enter number :"))
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print(even)
# print(odd)

# ===========================

# n1 = int(input("Enter number1 :"))
# n2 = int(input("Enter number2 :"))
# n3 = int(input("Enter number3 :"))

# if n1>n2 and n1>n3:
#     print(n1,"is greater")
# elif n2>n3:
#     print(n2,"is greater")
# else:
#     print(n3,"is greater")

# =====================================

# d1={'a':1,'b':2}
# d2={'c':3,'d':4}

# d1.update(d2)

# print(d1)

# =====================================

# num = int(input("enter number :"))
# prime = 0

# for i in range(1,num+1):
#     if num%i == 0:
#         prime += 1

# if prime == 2:
#     print("prime num")
# else:
#     print("not prime")

# =====================================

# user = int(input("Enter num :"))
# fact = 1
# for i in range(1,user+1):
#     fact = fact * i

# print(fact)

# =====================================