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
# class a:
#     def fun1(self):
#         print("method 1")
# class b:
#     def fun2(self):
#         print("method 2")
# class c(a,b):
#     def fun3(self):
#         print("method 3")
# obj = c()
# obj.fun1()
# obj.fun2()
# obj.fun3()
# -------------------------
# hirachical
# class a:
#     def fun1(self):
#         print("method 1")
# class b(a):
#     def fun2(self):
#         print("method 2")
# class c(a):
#     def fun3(self):
#         print("method 3")
# obj = b()
# obj.fun1()
# obj.fun2()
# obj = c()
# obj.fun1()
# obj.fun3()
# -------------------------

# hybrid

# class a:
#     def fun1(self):
#         print("method 1")
# class b(a):
#     def fun2(self):
#         print("method 2")
# class c:
#     def fun3(self):
#         print("method 3")
# class d(b,c):
#     def fun4(self):
#         print("method 4")
        
# obj = d()
# obj.fun1()
# obj.fun2()
# obj.fun3()
# obj.fun4()

# ====================================

# polymorphism

# class a:
#     def fun1(self):
#         super().fun1()
#         print("method 1")
# class b(a):
#     def fun1(self):
#         super().fun1()
#         print("method 2")
# class c:
#     def fun1(self):
#         print("method 3")
# class d(b,c):
#     def fun1(self):
#         super().fun1()
#         print("method 4")
        
# obj = d()
# obj.fun1()

# ===================================

# encapulation

# class a:
#     def fun1(self):
#         a = 10
#         self.a = a
        
# class b(a):
#     def fun2(self):
#         print(self.a)
        
# obj = b()
# obj.fun1()
# obj.fun2()
