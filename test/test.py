# import requests

# # 接口地址
# url = "http://127.0.0.1:8000/items/"

# # JSON 数据（对应 Item）
# json_data = {
#     "name": "test",
#     "description": "测试",
#     "price": 100.5,
#     "tax": 5.2
# }
# # 发送 POST 请求（同时传 json + params）
# response = requests.post(url, json=json_data)

# # 打印结果
# print("返回数据:\n", response.json())

import requests

# 接口地址
url = "http://127.0.0.1:8000/files/"

# 要上传的文件（改成你电脑上的文件）
files = {
    "file": open("t.html", "r")   # file 必须和接口参数名一样
}

# 发送请求
response = requests.post(url, files=files)

print(response.json())