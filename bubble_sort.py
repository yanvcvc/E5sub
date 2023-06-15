import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 生成随机数列表
random_nums = [random.randint(1, 10000) for _ in range(2000)]
print("随机数列表:", random_nums)

# 计时开始
start_time = time.time()

# 对随机数列表进行冒泡排序
bubble_sort(random_nums)

# 计时结束
end_time = time.time()

# 计算所用时间（秒）
duration = end_time - start_time
print("排序后列表:", random_nums)
print("排序耗时（秒）:", duration)
