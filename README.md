# map_generator
根据上传的图像生成可以行走的地图

## 使用说明
### 生成exe程序:
生成exe程序前，需要先安装程序所依赖的python包，命令为pip install -r requirements.txt
生成exe程序，需要使用pyinstaller包，安装pyinstaller包的命令为pip install pyinstaller
安装好后使用命令 pyinstaller ui.py生成exe程序，生成的程序存储在项目目录下的dist目录下，文件名为ui.exe
### 程序使用
在一个单独的文件夹中放置图片，图片命名的格式为 （x,y,up.jpg）   其中x和y是横坐标和纵坐标，是整数的，然后up是up,down,right,left其中一个，都好为英文逗号。一个坐标点的四张图片代表某一点的前后左右四个方向的看到的图像
命名图片完成后，将生成的ui.exe放入图片文件夹中，双击即可运行程序。

### 界面介绍
![image](https://user-images.content.com/9691657/225288900-7e91cec6-8ee1-4771-a45a-c25c18aed09b.png)
程序界面如图所示，右下角为生成的地图，红色代表当前位置，蓝色代表可以到达的位置，如果有绿色说明这一点没有上传图像，不可达。点击左转右转和后转会在原地旋转，看到相应方向的图像，点击向前将会走向前方对应的点。
