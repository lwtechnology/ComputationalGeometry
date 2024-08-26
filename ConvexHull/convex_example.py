import random
import matplotlib.pyplot as plt
import math
from extreme_point import *

# 生成包含100个随机点的二维坐标列表
random_points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(100)]
extreme_index = [True for _ in range(100)]

points_len = len(random_points)
for p in range(points_len):
    for q in range(p + 1, points_len):
        for r in range(q + 1, points_len):
            for s in range(points_len):
                if s == p or s == q or s == r or extreme_index[s] == False:
                    continue
                if in_triangle_test(random_points[p], random_points[q], random_points[r], random_points[s]):
                    extreme_index[s] = False

# 将随机点拆分为 x 和 y 坐标
x_values = [point[0] for point in random_points]
y_values = [point[1] for point in random_points]

# 创建散点图
plt.figure(figsize=(8, 6))
plt.scatter(x_values, y_values, color='b', marker='o')
plt.title('Random Scatter Plot of 100 Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

extreme_points = []
for i in range(points_len):
    if extreme_index[i]:
        extreme_points.append(random_points[i])


reference_point = extreme_points[0]
def polar_angle(point):
    x_diff = point[0] - reference_point[0]
    y_diff = point[1] - reference_point[1]
    return math.atan2(y_diff, x_diff)

# 按照极角对点进行排序
sorted_extreme_points = sorted(extreme_points, key=polar_angle, reverse=True)

# 将点的坐标拆分为 x 和 y 坐标
x_extreme = [point[0] for point in sorted_extreme_points]
y_extreme = [point[1] for point in sorted_extreme_points]
x_extreme.append(sorted_extreme_points[0][0])
y_extreme.append(sorted_extreme_points[0][1])

plt.plot(x_extreme, y_extreme, 'r')

plt.show()
