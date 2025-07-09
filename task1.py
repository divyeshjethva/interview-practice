
s = input("Enter name :")

a = len(s) // 2

if len(s)%2 == 0:
    print("enter odd string")
else:
    print( s[a-1] + s[a] + s[a+1])