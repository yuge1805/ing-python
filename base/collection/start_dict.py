# dict
# 存储键值对(key: value) key不可重复
# value可以是任意数据类型
# key不能为可变数据类型（不能为list set dict）(能为str int float tuple)

# 定义
dict1 = {"a": 1, "b": 2, "c": 3}
print(type(dict1))
print(dict1["a"])

# 定义空字典
dict2 = {}
print(type(dict2))
print(dict2)
dict3 = dict()
print(type(dict3))
print(dict3)

# 获取、修改
print(f"a value: {dict1["a"]}")
print(f"a value: {dict1.get("a")}")

# 修改
dict1["a"] = 10
print(f"a value: {dict1["a"]}")

# 删除
# 方式一
del dict1["a"]
print(f"delete a, dict: {dict1}")
# key不存在时，删除报错
# del dict1["a"]
# 方式二
bv = dict1.pop("b")
print(f"pop b value: {bv}")
print(f"pop b, dict: {dict1}")
# key不存在时，删除报错
# bv2 = dict1.pop("b")


dict2 = {"a": 1, "b": 2, "c": 3}
# keys
# print result: dict_keys(['a', 'b', 'c'])
print(f"keys: {dict2.keys()}")
# values
# print result: dict_values([1, 2, 3])
print(f"values: {dict2.values()}")
# items
# print result: dict_items([('a', 1), ('b', 2), ('c', 3)])
print(f"items: {dict2.items()}")

# 遍历
for item in dict2.items():
    print(f"key: {item[0]}, value: {item[1]}")

# 遍历
for k, v in dict2.items():
    print(f"key: {k}, value: {v}")