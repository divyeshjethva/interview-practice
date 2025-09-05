# 100 to 1 print without loop

def fun(n):
    if n<1:
        return
    print(n)
    fun(n-1)

fun(100)