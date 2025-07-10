# class objeect

# class a:
#     def fun1(self):
#         print("method 1")

# obj = a()
# obj.fun1()

# =======================

# inheritance 
# ------------------------

# single
# class a:
#     def fun1(self):
#         print("method 1")
# class b(a):
#     def fun2(self):
#         print("method 2")
        
# obj = b()
# obj.fun1()
# obj.fun2()
# --------------------------

# multilevel
# class a:
#     def fun1(self):
#         print("method 1")
# class b(a):
#     def fun2(self):
#         print("method 2")
# class c(b):
#     def fun3(self):
#         print("method 3")
# obj = c()
# obj.fun1()
# obj.fun2()
# obj.fun3()
# ---------------------------
# multiple
class a:
    def fun1(self):
        print("method 1")
class b:
    def fun2(self):
        print("method 2")
class c(a,b):
    def fun3(self):
        print("method 3")
obj = c()
obj.fun1()
obj.fun2()
obj.fun3()
