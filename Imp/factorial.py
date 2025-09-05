
# normal factorial
# ---------------------------
# n = 5
# fact = 1

# for i in range(1,6):
#     fact = fact * i
    
# print(fact)


# without loop factorial
# -----------------------------

def fun(n,f=1):
    if n == 0:
        print(f)
        return
    f=f * n
    fun(n-1,f)
    
fun(5)


