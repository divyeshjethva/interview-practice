
# print list without loop
# --------------------------
l = [1,2,4,8,4,5]
def f(n):
    if n>len(l)-1:
        return
    print(l[n])
    f(n+1)

f(0)