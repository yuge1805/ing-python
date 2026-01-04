# 全局变量
num = 100

def add(a):
    # 实际定义了一个局部变量num
    num = 10000
    # print 10000
    print(f"num: {num}")
    return a + 100

# print 100
print(f"num: {num}")
add(1)
# print 100
print(f"num: {num}")


print("global num=================================================")

def add_global(a):
    # 访问全局变量num
    global num
    num = 10000
    # print 10000
    print(f"num: {num}")
    return a + 100

# print 100
print(f"num: {num}")
add_global(1)
# print 10000
print(f"num: {num}")


print("传参方式=============================================================")
def reg_stu(name, age, gender, city):
    print(f"name: {name}, age: {age}, gender: {gender}, city: {city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 位置传参（默认）
zhangsan = reg_stu("张三", 18, "男", "上海")
print(zhangsan)

# 关键字传参
lisi = reg_stu(gender="女", city="北京", name="lisi", age=19)
print(lisi)
# 如果位置参数与关键字参数混用，关键字参数必须放在最后
wangwu = reg_stu("王五", 20, city="上海", gender="男")
print(wangwu)

print("参数默认值=============================================================")
def reg_stu_default(name, age=18, gender="男", city="上海"):
    print(f"name: {name}, age: {age}, gender: {gender}, city: {city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

zhangsan = reg_stu_default("张三")
print(zhangsan)

lisi = reg_stu_default("lisi", gender="女")
print(lisi)

print("不定长参数=============================================================")
# 位置参数
def calc_data(*args):
    print(f"args: {args}")
    # args类型为tuple
    print(f"args type: {type(args)}")
    return sum(args)
print(calc_data(1, 2, 3))
print(calc_data(1, 2, 3, 4, 5))

# 关键字参数
def calc_data(*args, **kwargs):
    """
    求和
    :param args: 不定长参数
    :param kwargs: 不定长关键参数
        print: 是否打印输出
        round: 保留的小数位个数
    :return:
    """
    print(f"kwargs: {kwargs}")
    # kwargs类型为dict
    print(f"kwargs type: {type(kwargs)}")
    if kwargs.get("print"):
        print(f"sum: {sum(args)}")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    return round(sum(args), kwargs.get("round", 1))
calc_data_result = calc_data(1.11, 2.22, 3.33, print=True, round=2)
print(f"calc_data_result: {calc_data_result}")