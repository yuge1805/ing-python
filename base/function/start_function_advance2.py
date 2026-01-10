def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# 函数作为参数
def calculate(x, y, func):
    return func(x, y)

result = calculate(1, 2, add)
print(result)
result = calculate(1, 2, subtract)
print(result)

# 匿名函数
# lambda 参数列表: 函数体（只能是单行表达式）
# 不需要return，默认返回表达式结果
add_func = lambda x, y: x + y
result = calculate(1, 2, add_func)
print(result)
result = calculate(1, 2, lambda x, y: x + y)
print(result)

# 根据字符串长度排序
data_list = ["hello", "world", "python", "java"]
print(data_list)
data_list.sort(key=lambda x: len(x))
print(data_list)
data_list.sort(key=lambda x: len(x), reverse=True)
print(data_list)