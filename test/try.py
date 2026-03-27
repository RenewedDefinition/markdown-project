# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# 输入uvicorn try:app --reload 启动应用

# from typing import Union

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# from pydantic import BaseModel
# from fastapi import FastAPI

# test = FastAPI()
# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float = None

# @test.post("/items/")
# def create_item(item: Item):
#     return item

# from fastapi import Header, Cookie
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/")
# def read_item(user_agent: str = Header(None), session_token: str = Cookie(None)):
#     return {"User-Agent": user_agent, "Session-Token": session_token}

# from fastapi import Header, Cookie
# from fastapi import FastAPI
# from fastapi.responses import RedirectResponse

# app = FastAPI()

# @app.get("/items/")
# def read_item(user_agent: str = Header(None), session_token: str = Cookie(None)):
#     return {"User-Agent": user_agent, "Session-Token": session_token}

# @app.get("/redirect")
# def redirect():
#     return RedirectResponse(url="/items/")

# from fastapi import FastAPI
# from fastapi import HTTPException

# app = FastAPI()

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     if item_id == 42:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item_id": item_id}

# from fastapi import FastAPI
# from fastapi.responses import JSONResponse

# app = FastAPI()

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     content = {"item_id": item_id}
#     headers = {"X-Custom-Header": "custom-header-value"}
#     return JSONResponse(content=content, headers=headers)

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float = None

# @app.post("/items/")
# def create_item(item: Item):
#     return item

# from fastapi import FastAPI, Query
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float = None

# @app.get("/items/")
# def read_item(item: Item, q: str = Query(..., max_length=10)):
#     return {"item": item, "q": q}

# from fastapi import Depends, FastAPI

# app = FastAPI()

# # 依赖项函数
# def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}

# @app.get("/items/")
# async def read_items(commons: dict = Depends(common_parameters)):
#     return commons

# from fastapi import Depends, FastAPI, HTTPException

# app = FastAPI()

# # 依赖项函数
# def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}

# # 路由操作函数
# @app.get("/items/")
# async def read_items(commons: dict = Depends(common_parameters)):
#     return commons

# # 后处理函数（好像不对呢）
# async def after_request():
#     # 这里可以执行一些后处理逻辑，比如记录日志
#     print("请求已处理，执行后处理逻辑")
#     pass

# # 后处理依赖项
# @app.get("/items/", response_model=dict)
# async def read_items_after(request: dict = Depends(after_request)):
#     return {"message": "Items returned successfully"}

# from fastapi import Depends, FastAPI, HTTPException

# app = FastAPI()

# # 依赖项函数1
# def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}

# # 依赖项函数2
# def verify_token(token: str = Depends(common_parameters)):
#     if token is None:
#         raise HTTPException(status_code=400, detail="Token required")
#     return token

# # 路由操作函数
# @app.get("/items/")
# async def read_items(token: dict = Depends(verify_token)):
#     return token

# from fastapi import Depends, FastAPI, HTTPException
# from typing import Optional
# import asyncio

# app = FastAPI()

# # 异步依赖项函数
# async def get_token():
#     # 模拟异步操作
#     await asyncio.sleep(2)
#     return "fake-token"

# # 异步路由操作函数
# @app.get("/items/")
# async def read_items(token: Optional[str] = Depends(get_token)):
#     return {"token": token}

# from fastapi import FastAPI, Form

# app = FastAPI()


# @app.post("/login/")
# async def login(username: str = Form(), password: str = Form()):
#     return {"username": username}

# from fastapi import FastAPI, Form

# app = FastAPI()

# # 路由操作函数
# @app.post("/items/")
# async def create_item(
#     name: str = Form(...),
#     description: str = Form(None),
#     price: float = Form(..., gt=0),
# ):
#     return {"name": name, "description": description, "price": price}

# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()

# # 路由操作函数
# @app.post("/files/")
# async def create_file(file: UploadFile = File(...)):
#     return {"filename": file.filename}

from fastapi import FastAPI, HTTPException, status, Depends, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import asyncio

# 综合示例：博客 API
app = FastAPI(
    title="博客 API",
    description="展示 FastAPI 核心概念的博客系统",
    version="1.0.0"
)

# 数据模型
class PostBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    published: bool = Field(True)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    author_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

# 模拟数据库
posts_db = []
next_id = 1

# 依赖：获取当前用户（简化版）
async def get_current_user() -> int:
    # 实际应用中会从 JWT token 解析
    return 1

# 异步路径操作
@app.get("/posts", response_model=List[PostResponse], tags=["文章"])
async def list_posts(
    skip: int = Query(0, ge=0, description="跳过的文章数"),
    limit: int = Query(10, ge=1, le=100, description="返回的文章数"),
    published_only: bool = Query(True, description="只返回已发布的文章")
):
    """
    获取文章列表
    
    支持分页和筛选功能
    """
    # 模拟异步数据库查询
    await asyncio.sleep(0.1)
    
    filtered_posts = posts_db
    if published_only:
        filtered_posts = [p for p in posts_db if p["published"]]
    
    return filtered_posts[skip:skip + limit]

@app.post("/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED, tags=["文章"])
async def create_post(
    post: PostCreate,
    current_user_id: int = Depends(get_current_user)
):
    """
    创建新文章
    
    需要用户认证
    """
    global next_id
    
    # 模拟异步数据库操作
    await asyncio.sleep(0.1)
    
    new_post = {
        "id": next_id,
        "title": post.title,
        "content": post.content,
        "published": post.published,
        "author_id": current_user_id,
        "created_at": datetime.now(),
        "updated_at": None
    }
    
    posts_db.append(new_post)
    next_id += 1
    
    return new_post

@app.get("/posts/{post_id}", response_model=PostResponse, tags=["文章"])
async def get_post(post_id: int):
    """
    获取特定文章
    
    根据文章 ID 返回文章详情
    """
    # 模拟异步数据库查询
    await asyncio.sleep(0.1)
    
    post = next((p for p in posts_db if p["id"] == post_id), None)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {post_id} not found"
        )
    
    return post

# 健康检查端点
@app.get("/health", tags=["系统"])
async def health_check():
    """系统健康检查"""
    return {
        "status": "healthy",
        "timestamp": datetime.now(),
        "posts_count": len(posts_db)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)