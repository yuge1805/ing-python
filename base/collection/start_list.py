# list
# str
# tuple
# set
# dict

# list
print("list ---------------------------------------")
s = ["a", "b", "c", "d", "e"]
print(type(s))
print(s[0])
print(s[-1])

# list 修改
s[0] = "A"
print(s[0])

# list 删除
del s[0]
print(s)

# list 子列表
ss = s[0:2]
print(f"sub: {ss}")

# list尾部追加
s.append("f")
print(f"append result: {s}")

# list 插入
s.insert(0, "a")
print(f"insert result: {s}")

# list 删除元素
s.remove("a")
print(f"remove result: {s}")

# list 删除指定索引位置的元素
s.pop(1)
print(f"pop result: {s}")

# list sort
s.sort()
print(f"sort result: {s}")

# list reverse
s.reverse()
print(f"reverse result: {s}")

# len
print(f"len: {len(s)}")

# in 判断
if "f" in s:
    print("f in s")

if "a" not in s:
    print("a not in s")

# 解包\组包
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [*list1, *list2]
print(f"解包\组包：{list3}")

list4 = list1 + list2
print(f"list1 + list2: {list4}")

# 推导
num_list1 = [1, 2, 3]
# [待插入项 for i in 列表]
num_list2 = [i * 2 for i in num_list1]
print(f"num_list2: {num_list2}")
# [待插入项 for i in 列表 if 条件]
num_list3 = [i + 1 for i in num_list1 if i % 2 == 0]
print(f"num_list3: {num_list3}")

