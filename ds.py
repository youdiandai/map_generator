import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
import random
from distribut_images import distribut


class Point:
    def __init__(self, origin_site, up="", down="", left="", right="") -> None:
        self.origin_site = origin_site
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def turn_left(self):
        self.up, self.down, self.left, self.right = self.left, self.right, self.down, self.up

    def turn_right(self):
        self.up, self.down, self.left, self.right = self.right, self.left, self.up, self.down

    def turn_back(self):
        self.up, self.down, self.left, self.right = self.down, self.up, self.right, self.left

    def __str__(self) -> str:
        return f"X:{self.origin_site[0]},Y:{self.origin_site[1]} UP:{self.up} DOWN:{self.down} LEFT:{self.left} RIGHT:{self.right}"

    @property
    def can_reach(self) -> str:
        return True if self.up or self.down or self.left or self.right else False

    def __repr__(self) -> str:
        return f"X:{self.origin_site[0]},Y:{self.origin_site[1]} UP:{self.up} DOWN:{self.down} LEFT:{self.left} RIGHT:{self.right}"


class Img_map:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
        self.img_map = np.array([[Point(origin_site=(x, y)) for y in range(width)] for x in range(height)])
        self.current_x = 0
        self.current_y = 0

    def forward(self) -> bool:
        if self.current_x + 1 < self.img_map.shape[0]:
            if self.img_map[self.current_x + 1][self.current_y].can_reach:
                self.current_x = self.current_x + 1
                return True
            else:
                print("Point is None")
                return False
        else:
            print("can't reach ,beyond the boundary")
            return False

    @property
    def current_path(self) -> str:
        return self.img_map[self.current_x][self.current_y].up

    def print_current(self):
        print(self.img_map[self.current_x][self.current_y])
        return str(self.img_map[self.current_x][self.current_y])

    def turn_right(self):
        self.turn_left()
        self.turn_left()
        self.turn_left()

    def turn_left(self):
        for x in range(self.height):
            for y in range(self.width):
                self.img_map[x][y].turn_left()
        self.img_map = np.rot90(self.img_map, 3)
        self.height, self.width = self.width, self.height
        past_x = self.current_x
        self.current_x = self.current_y
        self.current_y = self.width - past_x - 1

    def turn_back(self):
        self.turn_right()
        self.turn_right()

    def __repr__(self) -> str:
        return self.img_map.__repr__()

    def set_current_value(self, up="", down="", left="", right=""):
        self.img_map[self.current_x][self.current_y].up = up
        self.img_map[self.current_x][self.current_y].down = down
        self.img_map[self.current_x][self.current_y].left = left
        self.img_map[self.current_x][self.current_y].right = right

    def draw_map(self):
        f = lambda x: 50 if x.can_reach else 0
        data = [[f(y) for y in x] for x in self.img_map]
        data[self.current_x][self.current_y] = 99
        plt.imshow(data, cmap="jet", extent=[0, len(data[0]), 0, len(data)])
        # 翻转y轴方向
        plt.gca().invert_yaxis()
        # 设置x轴和y轴的刻度位置和标签为行数和列数
        plt.xticks(range(len(data[0])))
        plt.yticks(range(len(data)))
        plt.axis("off")
        # 显示图像
        plt.savefig("map.jpg")


def get_test_map():
    m = Img_map(width=4, height=3)
    m.img_map[0][0].up = "↑"
    m.img_map[0][0].down = "↓"
    m.img_map[0][0].left = "←"
    m.img_map[0][0].right = "→"
    return m


def get_test_map2():
    distribut()
    m = Img_map(width=10, height=12)
    folders = os.listdir("./points")
    random_blank_points = [(random.randint(0, 12), random.randint(0, 12)) for x in range(50)]
    if (0, 0) in random_blank_points:
        random_blank_points.pop(random_blank_points.index((0, 0)))

    for folder in folders:
        site = [int(x) for x in folder.split(",")]
        if (site[0], site[1]) in random_blank_points:
            continue
        m.img_map[site[0]][site[1]].up = os.path.join("./points", folder, "up.jpg")
        m.img_map[site[0]][site[1]].down = os.path.join("./points", folder, "down.jpg")
        m.img_map[site[0]][site[1]].left = os.path.join("./points", folder, "left.jpg")
        m.img_map[site[0]][site[1]].right = os.path.join("./points", folder, "right.jpg")
    return m


def create_map():
    distribut()
    folders = os.listdir("points")
    max_x, max_y = 0, 0
    for folder in folders:
        x, y = folder.split(",")
        if int(x) > max_x:
            max_x = int(x)
        if int(y) > max_y:
            max_y = int(y)
    m = Img_map(width=max_y+1, height=max_x+1)
    for folder in folders:
        x, y = [int(x) for x in folder.split(",")]
        m.img_map[x][y].up = os.path.join("./points", folder, "up.jpg") if os.path.exists(
            os.path.join("./points", folder, "up.jpg")) else ""
        m.img_map[x][y].down = os.path.join("./points", folder, "down.jpg") if os.path.exists(
            os.path.join("./points", folder, "down.jpg")) else ""
        m.img_map[x][y].left = os.path.join("./points", folder, "left.jpg") if os.path.exists(
            os.path.join("./points", folder, "left.jpg")) else ""
        m.img_map[x][y].right = os.path.join("./points", folder, "right.jpg") if os.path.exists(
            os.path.join("./points", folder, "right.jpg")) else ""
    return m


if __name__ == "__main__":
    m = get_test_map2()
    # m.print_current()
    # m.turn_left()
    # m.print_current()
    # m.turn_left()
    # m.print_current()
    # m.turn_right()
    # m.print_current()
    # m.turn_right()
    # m.print_current()
    # m.turn_back()
    # m.print_current()
    # m.turn_back()
    # m.print_current()
    # m.current_x
    # m.current_y
    # m.draw_map()

    # 循环输入上下左右，根据上下左右移动初始位置，并打开对应位置的文件
    while True:
        print(f"输入下一步(left right back forward，输入exit退出)，当前位置{m.print_current()}")
        n = input()
        if n == "exit":
            break
        elif n == "left":
            m.turn_left()
        elif n == "right":
            m.turn_right()
        elif n == "back":
            m.turn_back()
        elif n == "forward":
            m.forward()
        else:
            print("无效输入")
        # m.draw_map()
        img = Image.open(m.current_path)  # 打开图片文件，并返回一个Image对象
        img.show()  # 显示图片
