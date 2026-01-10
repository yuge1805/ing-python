# 变量声明: 类型
a: int = 1
score: float = 0.0
name: str = "hello"
flag: bool = True
pic: None = None

names: list[str] = ["hello", "world"]
phones: set[str] = {"123", "456"}
scores: dict[str, float] = {"hello": 100.0, "world": 99.9}
goods: tuple[str, float, int] = ("hello", 100.0, 1)

# 函数参数声明: 类型
def add(x: int, y: int) -> int:
    return x + y
result = add(1, 2)
print(result)

def cal(*args: tuple[str, int], total=100.0):
    for item in args:
        total += item[1]
    return total
result = cal(("hello", 1), ("world", 2), total=99.9)
print(result)