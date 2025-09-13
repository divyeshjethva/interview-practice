
# uniq list 
# ==========================

# l = [1,4,2,5,5,2,7]

# a = set(l)
# print(list(a))
# ----------------------------

# l = [1,4,2,5,5,2,7]
# l1 = []
# l2 = []
# for i in l:
#     if i in l1:
#         l2.append(i)
#     else:
#         l1.append(i)

# print(l1)

# ----------------------------

# l = [1, 2, 3, 2, 4, 1, 5]
# u = []

# for i in l:
#     if i not in u:
#         u.append(i)

# print(u)


# ----------------------------


# l = [1,4,2,5,5,2,7]
# u = []

# def f(i):
#     if i>len(l)-1:
#         return
#     if l[i]  not in u:
#         u.append(l[i])
#     f(i+1)

# f(0)
# print(u)

# -------------------------------

l = [1,'hello',6,8,'wow']

number = []
string = []

for i in l:
    try:
        if i:
            i+1
            number.append(i)
    except:
        string.append(i)
        
print(number)
print(string)