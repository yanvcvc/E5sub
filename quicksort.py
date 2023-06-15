import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 选择基准点
    smaller = [x for x in arr if x < pivot]  # 所有比基准点小的元素
    equal = [x for x in arr if x == pivot]  # 所有与基准点相等的元素
    larger = [x for x in arr if x > pivot]  # 所有比基准点大的元素
    return quicksort(smaller) + equal + quicksort(larger)  # 递归排序子列表

# 生成随机数列表
random_nums = [random.randint(1, 10000) for _ in range(2000)]
print("随机数列表:", random_nums)

# 计时开始
start_time = time.time()

# 对随机数列表进行快速排序
sorted_nums = quicksort(random_nums)

# 计时结束
end_time = time.time()

# 计算所用时间（秒）
duration = end_time - start_time
print("排序后列表:", sorted_nums)
print("排序耗时（秒）:", duration)
