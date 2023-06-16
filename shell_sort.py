import random
import time

# 希尔排序函数
def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# 生成2000个随机数（10000以内）
arr = [random.randint(1, 10000) for _ in range(2000)]

# 记录开始时间
start = time.time()

# 调用希尔排序函数
shellSort(arr)

# 记录结束时间
end = time.time()

# 打印排序后的数组
print("排序后的数组:")
print(arr)

# 打印排序所用的时间，单位为秒
print("排序所用的时间:", end - start, "秒")
