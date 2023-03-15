import glob
import shutil
import os
import re


def culture_map_size():
    regex = re.compile(r'\d+,\d+,(up|right|down|left)')
    images = glob.glob("./*.jpg")
    max_x,max_y = 0,0
    for image in images:
        x, y, direction = regex.search(image).group().split(',')
        if int(x)>max_x:
            max_x=int(x)
        if int(y)>max_y:
            max_y=int(y)
    return max_x+1,max_y+1


def create_dir(X=0,Y=0):
    if X==0 or Y==0:
        X,Y  = culture_map_size()
    os.mkdir("points")
    for x in range(X):
        for y in range(Y):
            os.mkdir(os.path.join("points",f"{x},{y}"))
    return X,Y

def distribut():
    if not os.path.exists("points"):
        create_dir()
        regex = re.compile(r'\d+,\d+,(up|right|down|left)')
        images = glob.glob("./*.jpg")
        for image in images:
            x, y, direction = regex.search(image).group().split(',')
            target_path = os.path.join("points",f"{x},{y}",f"{direction}.jpg")
            shutil.move(image,target_path)


def create_test_images():
    images = glob.glob("./*.jpg")
    for x in range(12):
        for y in range(10):
            for name in ["up","down","left","right"]:
                os.rename(images.pop(0),f"{x},{y},{name}.jpg")



# # 获取所有图片的路径列表
# images = glob.glob("./*.jpg")

# # 获取图片数量和文件夹数量
# num_images = len(images)
# num_folders = 120

# # 计算每个文件夹应该分配多少张图片和剩余的图片数量
# images_per_folder = num_images // num_folders # 整除运算符，返回商的整数部分
# remainder = num_images % num_folders # 取余运算符，返回除法的余数

# for x in range(12):
#     for y in range(10):
#         folder_name = f"{x}.{y}"
#         target_path = "./"+folder_name+"/"
#         for j in ("up","down","left","right"):
#             image_path = images.pop(0)
#             image_name = os.path.basename(image_path)
#             shutil.move(image_path,target_path+image_name)