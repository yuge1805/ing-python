# str
s = "abcde"
print(type(s))
print(s[0])
print(s[-1])

print("for ------------------------")
for i in s:
    print(i)

# str 子列表
ss = s[0:2]
print(f"sub: {ss}")

# reverse
# -1 代表从后往前截取
rs = s[::-1]
print(f"reverse: {rs}")

# find
print(f"c find: {s.find("c")}")
print(f"h find: {s.find("h")}")

# index
print(f"c index: {s.index("c")}")
# index找不到时会报错
# print(f"h index: {s.index("h")}")

# split
s_array = s.split("c")
print(type(s_array))
print(f"split: {s_array}")

s_replaced = s.replace("c", "x")
print(f"s: {s}")
print(f"replace: {s_replaced}")

s2 = "  aa   "
print(f"s2 strip: {s2.strip()}")


