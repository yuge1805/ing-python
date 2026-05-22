import pytest

# pytest测试
# https://www.bilibili.com/video/BV1KZWKz3Ek5/?vd_source=70e88fee3f33e2f575db977061a065cf

# 测试方法： 以test_开头
# 测试类: 以Test开头
# 测试文件: 以test_开头，或_test结尾

def test_add():
    assert 1 + 1 == 2

# Fixture
# 定义测试用例的前置和后置
# 作用域： session、class、module、function
@pytest.fixture
def init_data():
    print("init_data前置操作")
    data = [1, 2, 3, 4, 5]
    # 返回数据给测试用例
    yield data
    print("init_data后置操作")

# 使用fixture （直接传函数名）
def test_use_data(init_data):
    assert len(init_data) == 3
    assert len(init_data) == 5


# 参数化
# 批量生产测试用例
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 2, 4),
    (3, 2, 5)
])
def test_add(a, b, expected):
    assert a + b == expected





