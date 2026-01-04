# set
# 无序 不重复 可修改

# 定义
set1 = {"a", "b", "c", "d", "e"}
print(type(set1))
# print result: {'b', 'e', 'c', 'a', 'd'}
print(set1)

# 定义空集合set
# {} 代表的是字典，不能用来定义空set
set2 = set()
print(type(set2))
# print result: set()
print(set2)

dict3 = {}
# print result: <class 'dict'>
print(type(dict3))

print("set add remove clear---------------------------------------")
set_ddd = {"a", "b", "c"}
# add
set_ddd.add("d")
print(f"add d result: {set_ddd}")
# remove
set_ddd.remove("a")
print(f"remove a result: {set_ddd}")
# remove 不存在会报错
# set_ddd.remove("a")
# clear
set_ddd.clear()
print(f"clear result: {set_ddd}")


print("set operation ------------------------------------------")
set4 = {"1", "2", "3"}
set5 = {"3", "4", "5"}
print(f"set4: {set4}, set5: {set5}")
# 差集
# 方式一
diff_set = set4.difference(set5)
print(f"difference_set: {diff_set}")
# 方式二
diff_set2 = set4 - set5
print(f"difference_set2: {diff_set2}")

# 交集
# 方式一
intersect_set = set4.intersection(set5)
print(f"intersect_set: {intersect_set}")
# 方式二
intersect_set2 = set4 & set5
print(f"intersect_set2: {intersect_set2}")

# 并集
# 方式一
union_set = set4.union(set5)
print(f"union_set: {union_set}")
# 方式二
union_set2 = set4 | set5
print(f"union_set2: {union_set2}")

print("set 推导---------------------------------------------")
# 元素在set4中，但是不在set5中
set6 = {i for i in set4 if i not in set5}
print(f"set6: {set6}")


