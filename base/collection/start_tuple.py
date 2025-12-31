# tuple 元组
# 元组是不可变的序列，类似于列表，但创建后不能修改
# 重复 有序 不可修改

# 定义元组 （建议）
t1 = ("a", "b", "c", "d", "e")
print(type(t1))

t11 = "a", "b", "c", "d", "e"
print(type(t11))

# 定义空元组
t2 = ()
t3 = tuple()

print(t1[0])
print(t1[-1])

print(f"count: {t1.count("a")}")
print(f"a index: {t1.index("a")}")


invalid_tuple_t3 = ("aaa")
# str
print(type(invalid_tuple_t3))

# 单元素的元组
tuple_t3 = ("aaa",)
print(type(tuple_t3))


# 组包
nt1 = ("a", "b", "c", "d", "e")
# 解包
print("解包=========================================================")
print(f"nt1: {nt1}")
it1, it2, it3, it4, it5 = nt1
print(f"it1: {it1}")
print(f"it2: {it2}")
print(f"it3: {it3}")
print(f"it4: {it4}")
print(f"it5: {it5}")

# 扩展解包
# *表示收集剩余所有元素
x, *y, z = nt1
print(f"unpack x: {x}, y:{y}, z:{z}")
n, *m = nt1
print(f"unpack n: {n}, m:{m}")


# 通过元组的组包\解包交换a,b变量
a = 10
b = 20
print(f"a: {a}, b: {b}")
a, b = (b, a)
# 等价与 a, b = b, a
print(f"a: {a}, b: {b}")
