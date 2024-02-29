import csv
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as scp

first_column = []
fourth_column = []
tenth_column = []

with open('data1.csv') as file:
    read_file = csv.reader(file, delimiter=';')
    for line in read_file:
        first_column.append(line[0])
        fourth_column.append(line[3])
        tenth_column.append(line[9])

first_column_float = list(map(float, first_column[1::50]))
fourth_column_float = list(map(float, fourth_column[1::50]))
tenth_column_float = list(map(float, tenth_column[1::50]))

first_column_np = np.array(first_column_float)
fourth_column_np = np.array(fourth_column_float)
tenth_column_np = np.array(tenth_column_float)

fig_graph_0, ax_graph_0 = plt.subplots()
ax_graph_0.set_title('График зависимости положения дроссельной заслонки(%) \n '
                     'и угла опережения зажигания от времени')
ax_graph_0.plot(first_column_np, fourth_column_np)
ax_graph_0.plot(first_column_np, tenth_column_np)
ax_graph_0.set_xlabel('Время, с')
ax_graph_0.set_ylabel('Пол. дрос. заслонки(%) '
                      'и угол опереж. зажиг. (°ПКВ)')
plt.show()

fig_graph_1, ax_graph_1 = plt.subplots()
(slope_graph_1, intercept_graph_1, rvalue_graph_1,
 pvalue_graph_1, stderr_graph_1) = (
    scp.linregress(first_column_np, tenth_column_np))
ax_graph_1.set_title('График кореляции для угла опереж. зажиг. (°ПКВ)')
ax_graph_1.plot(first_column_np, tenth_column_np,
                linewidth=0, marker='s')
ax_graph_1.plot(first_column_np,
                intercept_graph_1 + slope_graph_1 * first_column_np)
ax_graph_1.set_xlabel('Время, с')
ax_graph_1.set_ylabel('Угол опереж. зажиг. (°ПКВ)')
plt.show()

fig_graph_2, ax_graph_2 = plt.subplots()
ax_graph_2.set_title('График кореляции для пол. дрос. заслонки')
(slope_graph_2, intercept_graph_2, rvalue_graph_2,
 pvalue_graph_2, stderr_graph_2) = (
    scp.linregress(first_column_np, fourth_column_np))
ax_graph_2.plot(first_column_np, fourth_column_np,
                linewidth=0, marker='s')
ax_graph_2.plot(first_column_np,
                intercept_graph_2 + slope_graph_2 * first_column_np)
ax_graph_2.set_xlabel('Время, с')
ax_graph_2.set_ylabel('Пол. дрос. заслонки(%)')
plt.show()
