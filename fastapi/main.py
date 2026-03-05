# 需要在terminal中执行命令安装fastapi
# 适用生产环境（精简）：pip install fastapi
# 适用开发环境（完整）：pip install "fastapi[standard]"
# 验证安装 pip list | findstr fastapi
import time

from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
def read_root():
    time.sleep(5)
    return {"message": "Hello FastAPI"}

@app.get("/async")
async def async_read_root():
    await time.sleep(5)
    return {"message": "Hello FastAPI"}