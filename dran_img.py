import matplotlib.pyplot as plt

# 创建一个4行5列的二维数组
data = [[10, 10, 10, 10, 10],
        [50, 50, 90, 50, 10],
        [10, 10, 10, 50, 10],
        [10, 10, 10 ,50 ,50]]

# 绘制网格图，使用jet颜色映射，并指定图像的范围
plt.imshow(data, cmap="jet", extent=[0,len(data[0]),0,len(data)])

# 反转y轴的方向
plt.gca().invert_yaxis()

# 设置x轴和y轴的刻度位置和标签为行数和列数
plt.xticks(range(len(data[0])))
plt.yticks(range(len(data)))

# 显示图像
plt.show()