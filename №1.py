import numpy as np
import random
import time

start_random = 0
end_random = 10**3

array_py_1 = [random.randint(start_random, end_random) for i in range(10**6)]
array_py_2 = [random.randint(start_random, end_random) for j in range(10**6)]

array_np_1 = np.array(array_py_1)
array_np_2 = np.array(array_py_2)

start_time_py = time.time()
multiplication_py = [array_py_1[index] * array_py_2[index] for index in range(10**6)]
end_time_py = time.time()

start_time_np = time.time()
multiplication_np = np.multiply(array_np_1, array_np_2)
end_time_np = time.time()

time_py = end_time_py - start_time_py
time_np = end_time_np - start_time_np
difference_time = time_py - time_np

print(f'Время выполнения поэлементного умножения массивов без библиотеки NumPy: {time_py}')
print(f'Время выполнения поэлементного умножения массивов в библиотеке NumPy: {time_np}')
print(f'Данное действие выполняется в библиотеке NumPy на {difference_time} секунды быстрее')
