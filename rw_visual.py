import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    #创建一个RandomWalk实例并绘制所有点
    rw = RandomWalk(50000)
    rw.fill_walk()
    points_number = list(range(rw.num_pointss))
    plt.scatter(rw.x_value, rw.y_value, s=1, c=points_number, cmap=plt.cm.Blues, edgecolor='none')
    #突出起点终点
    plt.scatter(0, 0, c='green', edgecolor='none', s=10)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red',edgecolor='none', s=10)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n)")
    if keep_running == "n":
        break