import random
import time

# 插入排序函数
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# 生成2000个随机数（10000以内）
arr = [random.randint(1, 10000) for _ in range(2000)]

# 记录开始时间
start = time.time()

# 调用插入排序函数
insertionSort(arr)

# 记录结束时间
end = time.time()

# 打印排序后的数组
print("排序后的数组:")
print(arr)

# 打印排序所用的时间，单位为秒
print("排序所用的时间:", end - start, "秒")
