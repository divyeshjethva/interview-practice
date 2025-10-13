# l = ['ajay','div']
# d = {}
# for i in l[0]:
#     # print(i)
#     if i in d:
#         d[i]+=1
#         # print(i,"=")
#     else:
#         d[i] = 1
#         # print(i,"=",1)

# print(d)

# for k,v in d.items():
#     print(k,'=',v)

# ------------------------------

# s = "this is pen pen is fine"
# l = s.split()
# print(l)

# d = {}
# for j in l:
#     if j in d:
#         d[j]+=1
#     else:
#         if j == 'this':
#             d[j] = 2
#         else:
#             d[j] = 1
            
# print(d)

# ---------------------------------

# l = [2,6,5,7,8,5]
# d = {}

# for i in range(0,len(l)-1,2):
#     d[l[i]] = l[i+1]
    
# print(d)

# ---------------------------------

# l = [2,5,6,4,5,8]
# s = []
# for i in range(0,len(l)-1):
#     a = l[i]
#     b = l[i+1]
#     sum = a+b
#     s.append(sum)
    
# print(s)
# ---------------------------------
         

# d1 = {'a':2,'b':6,'c':4}
# d2 = {'e':2,'f':6,'g':4}
# d = {}

# a = []
# a1 = []
# for k,v in d1.items():
#     a.append(k)
#     a1.append(v)

# b = []
# b1 = []
# for k1,v1 in d2.items():
#     b.append(k1)
#     b1.append(v1)
    
# for i in range(len(a)):
#     d[f'{a[i]}{b[i]}'] = a1[i] + b1[i]
    
# # print(a)
# # print(a1)
# # print(b)
# # print(b1)
# print(d)

# ---------------------------------
# s = "pythonMLV"
# o = 'MLVoyphtn'
# ---------------------------------
# s = "pythonMLV"

# # MLV + o + y + p + h + t + n

# o = s[6:9] + s[4] + s[1] + s[0] + s[3] + s[2] + s[5]

# print(o)  # Output: MLVoyphtn

# ---------------------------------

s = "pythonMLV"

indices = [6, 7, 8, 4, 1, 0, 3, 2, 5]

o = ""
for i in indices:
    o = o + s[i]

print(o)  # Output: MLVoyphtn
# ---------------------------------


# a = int(input("Enter first :"))
# b = int(input("Enter first :"))
# c = input("Enter perform task :")

# if c == "+":
#     v = a+b
#     print(v)
# elif c == "-":
#     v = a-b
#     print(v)


