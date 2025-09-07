s = "abcabcbb"
l = []
for i in s:
    if i in l:
        pass
    else:
        l.append(i)
print(l)