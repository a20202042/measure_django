import statistics
import sys
import numpy as np
# data = [[10.2, 8.9, 9.9], [10.3, 11, 8.9]]
# all_data = []
# average_data = []
# for item in data:
#     average_data.append(statistics.mean(item))
# print(average_data)
#
# print(statistics.median(average_data)) #x
# # 計算總平均 = 中心線 = cl
# print(format(statistics.mean(average_data), '.3f')) #.3f小數點第三位
# x = statistics.mean(average_data)
# #計算全距 = R
# print(format(np.max(average_data) - np.min(average_data), '.3f'))
# r = np.max(average_data) - np.min(average_data)
# #UCL = x + A2*R
# A2 = float(0.483)
# x_ucl = x + r * A2
# x_lcl = x - r * A2
# print(x_ucl, x_lcl, x)
# x= [10.1, 10.3, 10.2]
# print(max(x) - min(x))
# print(np.min(x))
x = 0.1509090909090909
y = [10.5, 11]
print(np.linspace(9.77, 11.43, num=12))
data = np.linspace(9.77, 11.43, num=12)
data_range = []
old_data = []
new_data = []
for item in data:
    a = round(item, 2)
    old_data.append(a)
print(old_data)
for i in range(0, 11, 1):
    new_data.append([old_data[i],old_data[i+1]])
print(new_data)
Input = [12.8, .178, 1.8, 782.7, 99.8, 8.7]

# 用lambda进行排序
Output = sorted(Input, key=lambda x: float(x))

# 打印输出
print(Output)
x = [10.03, 10.44, 10.3, 9.92, 10.41, 10.49, 10.58, 10.81, 10.3, 10.72, 10.09, 10.12, 10.37, 10.48, 10.77, 10.78, 10.52, 10.84, 9.99, 10.12, 10.36, 10.86, 10.4, 9.77, 10.06, 10.16, 10.34, 10.53, 10.76, 10.93, 10.74, 10.57, 10.52, 10.67, 11.04, 11.43, 10.79, 10.64, 10.39, 10.56, 10.76, 11.03, 10.4, 9.85, 10.16, 10.43, 10.55, 10.36, 10.35, 10.86, 10.64, 10.95, 10.79, 10.74, 10.7, 10.57, 10.54, 10.54, 10.8, 10.65, 10.71, 10.59, 10.44, 10.43, 10.32, 10.17, 10.17, 10.14, 10.12, 10.23, 10.17, 10.21, 10.09, 10.48, 10.54, 10.65, 10.65, 10.9, 10.86, 10.79, 10.75, 10.65, 10.65, 10.58, 10.34, 10.34, 10.39, 10.48, 10.35, 10.99]
# x.pop()
z = [[9.77, 9.85, 9.92], [9.99, 10.03, 10.06], [10.09, 10.09, 10.12, 10.12, 10.12, 10.14, 10.16, 10.16, 10.17, 10.17, 10.17, 10.21], [10.23, 10.3, 10.3, 10.32, 10.34, 10.34, 10.34, 10.35, 10.35, 10.36, 10.36, 10.37], [10.39, 10.39, 10.4, 10.4, 10.41, 10.43, 10.43, 10.44, 10.44, 10.48, 10.48, 10.48, 10.49, 10.52, 10.52], [10.53, 10.54, 10.54, 10.54, 10.55, 10.56, 10.57, 10.57, 10.58, 10.58, 10.59, 10.64, 10.64, 10.65, 10.65, 10.65, 10.65, 10.65, 10.67], [10.7, 10.71, 10.72, 10.74, 10.74, 10.75, 10.76, 10.76, 10.77, 10.78, 10.79, 10.79, 10.79, 10.8, 10.81], [10.84, 10.86, 10.86, 10.86, 10.9, 10.93, 10.95], [10.99, 11.03, 11.04], [], [11.43]]
number = 0
for i in z:
    for i_2 in i:
        number = number + 1
print(number)
x = [1, 1,2,3]
for i in x:
    x.remove(i)
print(x)

ca = 0.11
cp = 0.22
cpk = 0.3
color = {
        'A+': "color: whitesmoke; background-color:pink",
        'A': "color: whitesmoke; background-color:orange",
        'B': "color: whitesmoke; background-color:dodgerblue",
        'C': "color: whitesmoke; background-color:seagreen",
        'D': "color: white; background-color:mediumseagreen;"
    }

if abs(ca) <= float(0.125):
    ca_color = color['A']
elif abs(ca) > float(0.125) and abs(ca) <= float(0.25):
    ca_color = color['B']
elif abs(ca) > float(0.25) and abs(ca) <= float(0.5):
    ca_color = color['C']
elif abs(ca) > float(0.5):
    ca_color = color['D']

if abs(cp) >= 1.67:
    cp_color = color['A+']
elif abs(cp) >= 1.33 and abs(cp) < 1.67:
    cp_color = color['A']
elif abs(cp) >= 1.0 and abs(cp) < 1.33:
    cp_color = color['B']
elif abs(cp) >= 0.67 and abs(cp) < 1.0:
    cp_color = color['C']
elif abs(cp) < 0.67:
    cp_color = color['D']

if abs(cpk) >= 1.67:
    cpk_color = color['A+']
elif abs(cpk) >= 1.33 and abs(cpk) < 1.67:
    cpk_color = color['A']
elif abs(cpk) >= 1.0 and abs(cpk) < 1.33:
    cpk_colork = color['B']
elif abs(cpk) >= 0.67 and abs(cpk) < 1.0:
    cpk_colork = color['C']
elif abs(cpk) < 0.67:
    cpk_colork = color['D']

print(ca_color)
print(cpk_color)
print(cp_color)