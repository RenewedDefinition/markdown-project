# 1. 从 fastapi 库中导入核心类：FastAPI(应用主体)、Request(接收请求数据)
from fastapi import FastAPI, Request

# 2. 导入静态文件服务：用于加载网页、CSS、JS等静态资源
from fastapi.staticfiles import StaticFiles

# 3. 导入响应类型：HTMLResponse(返回网页)、Response(基础响应)
from fastapi.responses import HTMLResponse, Response  

# 4. 导入 markdown 库：用于把 Markdown 文本转换成 HTML
import markdown

# 5. 创建 FastAPI 应用实例（整个服务的核心对象）
app = FastAPI()

# 6. 挂载静态文件目录：
#    访问路径：/static → 对应本地文件夹：static
#    作用：让服务器可以加载 index.html、css、js 等文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 7. 定义路由：处理浏览器自动请求的 /favicon.ico（网站图标）
#    include_in_schema=False：不在接口文档中显示这个接口
@app.get("/favicon.ico", include_in_schema=False)
# 8. 定义异步接口函数（async 是 FastAPI 推荐写法，支持高并发）
async def favicon():
    # 9. 返回状态码 204：表示无内容，避免浏览器报错找不到图标
    return Response(status_code=204)

# 10. 定义 POST 接口：路径 /api/convert，用于接收 Markdown 并转换
@app.post("/api/convert")
# 11. 接收 Request 对象：用来获取前端发送的 JSON 数据
async def convert(request: Request):
    # 12. 异步读取前端发送的 JSON 数据
    data = await request.json()
    # 13. 从 JSON 数据中取出 key 为 markdown 的值，没有则默认为空字符串
    md_text = data.get("markdown", "")
    # 14. 调用 markdown 库，把 Markdown 文本转换成 HTML
    #     extensions：开启扩展功能（代码块、代码高亮、表格、有序列表优化）
    html = markdown.markdown(
        md_text,
        extensions=["fenced_code", "codehilite", "tables", "sane_lists"]
    )
    # 15. 返回 JSON 格式数据：包含转换后的 HTML 字符串
    return {"html": html}

# 16. 定义根路由 GET /，返回类型强制为 HTML 网页
@app.get("/", response_class=HTMLResponse)
# 17. 首页接口：返回前端页面
async def index():
    # 18. 打开 static 文件夹下的 index.html 文件，读取内容
    with open("static/index.html", "r", encoding="utf-8") as f:
        # 19. 把 HTML 文件内容返回给浏览器渲染显示
        return f.read()

# 20. 主程序入口：只有直接运行这个文件时才执行
if __name__ == "__main__":
    # 21. 导入 uvicorn：FastAPI 官方推荐的运行服务器
    import uvicorn
    # 22. 启动服务：
    #    host=0.0.0.0：允许所有设备访问（局域网/本机）
    #    port=8000：服务端口号
    uvicorn.run(app, host="0.0.0.0", port=8000)