# 函数需要先定义，后调用
# NameError: name 'add' is not defined
# print(f"1 + 2: {add(1, 2)}")

def add(a, b):
    """
    求和
    :param a: 参数a
    :param b: 参数b
    :return:  和
    """
    return a + b

print(f"1 + 2: {add(1, 2)}")
print(f"1.1 + 2.2: {add(1.1, 2.2)}")

# 函数多个返回值，会封装到元组中
def calculate(a, b):
    """
    计算
    :param a: 参数a
    :param b: 参数b
    :return: 和，差
    """
    return a + b, a - b

calculate_result = calculate(1, 2)
print(f"calculate_result: {calculate_result}")
print(f"calculate_result type: {type(calculate_result)}")

add_result, minus_result = calculate(1, 2)
print(f"add_result: {add_result}, minus_result: {minus_result}")


# 第一步：先定义所有函数（此时函数内部的代码不会执行）
def function_a():
    print("a ... before")
    function_b()  # 这里只是“声明要调用”，但定义阶段不会执行
    print("a ... after")

def function_b():
    print("b ... before")
    function_c()
    print("b ... after")

def function_c():
    print("c ...")

# 第二步：调用function_a，此时才会执行函数内部的代码
function_a()


