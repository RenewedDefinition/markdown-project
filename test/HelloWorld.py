# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# 输入uvicorn HelloWorld:app --reload 启动应用
# 访问 http://127.0.0.1:8000 （由默认配置和网络基础规则共同决定）
# 可以看到 {"Hello": "World"} 的输出


from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}