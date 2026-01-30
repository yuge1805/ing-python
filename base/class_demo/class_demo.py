# 定义类（不推荐）
class Car:
    pass

c1 = Car()
print(c1)
print(type(c1))
print(type(c1.__dict__))

# 动态定义属性
c1.color = "red"
c1.brand = "audi"
c1.name = "X5"
print(c1.name)
print(c1.color)
print(c1.__dict__)

# 定义类
class CarV1:
    # 类属性，所有实例对象共享
    # 轮胎数量
    wheel = 4
    # 购置税
    tax_rate = 0.1
    # 初始化方法
    # self: 当前对象
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print(f"init: {self.name}, {self.color}")

    def run(self):
        print(f"run: {self.name}, {self.color}")

    def stop(self):
        print(f"stop: {self.name}, {self.color}")

c1 = CarV1("audi", "red")
print(c1.name)
print(c1.color)
print(c1.__dict__)
c1.run()
c1.stop()
print(CarV1.wheel)
print(CarV1.tax_rate)