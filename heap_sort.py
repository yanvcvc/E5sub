import random
import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# 生成随机数列表
random_nums = [random.randint(1, 10000) for _ in range(2000)]
print("随机数列表:", random_nums)

# 计时开始
start_time = time.time()

# 对随机数列表进行堆排序
heap_sort(random_nums)

# 计时结束
end_time = time.time()

# 计算所用时间（秒）
duration = end_time - start_time
print("排序后列表:", random_nums)
print("排序耗时（秒）:", duration)
