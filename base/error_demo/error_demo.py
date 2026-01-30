def fun_error():
    try:
        print("before=======================")
        print(1/0)
        print("after=======================")
    except Exception as e:
        print("运行错误：", e)
    finally:
        print("finally")

fun_error()