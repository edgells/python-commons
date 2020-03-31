

str1 = ["hello", "world"]
str2 = ["hello", "world"]
str3 = ["hello", "world"]

#
print(id(str1))
print(id(str3))
if str1 is str3:        # equal mem addr
    print("true")

if str1 == str3:        # = 比较 内容
    print("== true")