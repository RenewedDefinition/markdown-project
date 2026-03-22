# 1.仓库介绍
这是一个AI协助下进行的项目，旨在完成~~AI出的~~Markdown实时预览服务，代码在虚拟机ubuntu20.04下编写，包含python后端服务和HTML/JS前端页面

# 2.安装conda/miniconda
你可以在 'https://www.anaconda.com/download' 中找到conda或miniconda下载linux下的安装包，点击下载
然后在终端输入（这里以miniconda为例）
```
$cd /home/xxx/下载
$bash Miniconda3-latest-Linux-x86_64.sh
```
然后一直按回车键，出现“Do you accept the license terms”和“Do you wish the installer to initialize Anaconda3 by running condo init?”输入“yes”就安装完成了

或者你可以在终端输入~~（宇宙免责声明：以下是ai写的，未经尝试，不过应该可以）~~
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
# 一路回车，最后 yes
source ~/.bashrc
```

# 3.创建环境
在终端输入（这里环境名为md）
```
conda create -n md python=3.10 -y
conda activate md
```
