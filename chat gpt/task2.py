
# s = "divyesh"

# n = len(s)//2

# if n%2 == 0:
#     print("enter even string")
# else:
#     print(s[0], s[n], s[-1])

# print(n)
# ------------------------------
# s = "aaaaa"
# v = "aeiou"
# c = 0

# for i in s:
#     if i in v:
#         c+=1
# print(c)
# ---------------------------------

# n = "nayan"

# r = n[::-1]

# if n == r:
#     print("pelidrom")
# else:
#     print("Not")
# ----------------

# n = "wow"
# r = ""
# for i in range(len(n)-1,-1,-1):
#     r+=n[i]
    
# if n == r:
#     print("p")
# else:
#     print("n")

# ----------------

# s = "bob"
# g = ""
# def fun(n):
#     if n == -1:
#         return
#     global g
#     g+=s[n]
#     fun(n-1)    
# fun(len(s)-1)

# if g == s:
#     print("pelidrom")
# else:
#     print("Not")

# -------------------------------------------

# n = input("Enter numer :")
# s = 0
# for i in n:
#     s+=int(i)**3
    
# if s== int(n):
#     print("A")
# else:
#     print("N")

# -----------------------------------------------

# n = 10
# a = 0
# b = 1
# l = []
# for i in range(1,11):
#     l.append(a)
#     a,b = b,a+b
    
# print(l)
# -------------

# def fun(n,a,b):
#     if n == 0:
#         return
#     print(a)
#     a,b = b, a+b
#     fun(n-1,a,b)

# fun(10,0,1)
# ----------------------------------------

# for i in range(1,6):
#     print(" " * (i)," *"*(6-i))
    
    # ---------
    
# for i in range(1,6):
#     for n in range( i):
#         print(" ",end="")
        
#     for j in range(6-i):
#         print("*",end="")
#     print()
    
# ----------------------------------------

# l = [3,7,4,3,1,5,7,4]

# s = list(set(l))
# print(s)
# ----------
# l = [3,7,4,3,1,5,7,4]
# l1 = []
# l2 = []

# for i in l:
#     if i in l1:
#         l2.append(i)
#     else:
#         l1.append(i)

# print(l1)

# -----------
# a = ['a','b','c','d']
# b = [1,2,3,4]
# d = {}
# for i in range(len(a)):
#     d[a[i]] = b[i]
    
# print(d)
# -------------
# a = ['a','b','c','d']
# b = [1,2,3,4]

# s = dict(zip(a,b))

# print(s)

# -------------------------------------

# a = 10
# b = 20

# temp = a
# a = b
# b = temp
# print(a,b)
# ---------------

# a = 10
# b = 20

# a = a + b #a = 30
# b = a - b # 30-20-->10
# a = a - b # 30-10-->20
# print(a,b)
# -----------------------------------

# s = "ajay"
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
# ------------

# s = "ajay"
# d = {}
# for i in s:
#     d[i] = d.get(i, 0) + 1
# print(d)
# -----------------------------------

# a = 10
# def fun(a):
#     print(a)
# fun(20)
# ------------------------

# n = 16

# if n%2 == 0:
#     print("even")
# else:
#     print("ODD")

# --------------------------------------

# a = 3000
# b = 777
# c = 540

# if a>b and a>c:
#     print(a)
# elif b>c:
#     print(b)
# else:
#     print(c)

# -----------------------------------------

# d1={'a':1,'b':2}
# d2={'c':3,'d':4}

# d1.update(d2)

# print(d1)
# ---------------------------------------

# n = 5
# p = 0

# for i in range(1,n+1):
#     if n%i==0:
#         p+=1
# if p == 2:
#     print("prime")
# else:
#     print("Not")
# ---------------

# def fun(n,i,p):
#     if i == n:
#         if p == 1:
#             print("prime")
#             return
#         else:
#             print("Not prime")
#             return
#     if n%i==0:
#         p+=1
#     fun(n,i+1,p)
# fun(23,1,0)
# -------------------------------------
# fact = 1

# n = 5
# for i in range(1,n+1):
#     fact*=i
    
# print(fact)
# ----------

# def fun(n,i,fact):
#     if i==n+1:
#         print(fact)
#         return
#     fact*=i
#     fun(n,i+1,fact)
    
# fun(5,1,1)
# -----------------------------------------

# n = 5
# for i in range(1,11):
#     print(n ,"X",i,"=",n*i)
# ---------------

# def fun(n,i):
#     if i == 11:
#         return
#     print(n ,"X",i,"=",n*i)
#     fun(n,i+1)
    
# fun(5,1)
# -----------------------------------------

# f = open("demo.txt",'r')
# print(f.read())

# -------------------------------
# import random

# l = [3,67,8,323,85,3,2]
# otp = random.choice(l)
# print(otp)

