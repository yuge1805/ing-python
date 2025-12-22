print("hello world")
print("hello world2")
print("hello world3");print("hello world3")

# 数据类型
# 整数（int）
print(100)
# 浮点数/小数 （float）
print(3.14)
# 布尔值（bool）
print(True)
print(False)
# 字符串（str）
print("Hello")
# 空值（NoneType）
print(None)

# 变量
# Python是动态类型语音，在程序运行时才进行类型检查，变量的类型可以在程序运行过程中改变（一个变量可以接受不同类型的值）
# 不推荐
n = True
print(n)
n = 3.22
print(n)

# 常用函数
# type
print(type(n))
# isinstance
print(isinstance(n, float))
# str
print(str(n))


# 字符串
s1 = "Hello"
s2 = 'Hello'
s3 = """
    xxx
    xxxx
    xxxxx
    xxxxxx
"""

# 转义字符
s4 = 'It\'s very good'

# 拼接字符串
s5 = "Hello" "xxx"
print(s5)

s6 = "Hello" + "zzz"
print(s6)

# 拼接数值
name = "yyy"
age = 18
print(name + str(age))

# format
s1 = "uuu"
print("Hello %s" % s1)
s2 = "ddd"
print("Hello %s, %s" % (s1, s2))
print(f"Hello {s1}, {s2}")
