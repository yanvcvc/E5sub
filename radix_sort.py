import random
import time

def radix_sort(arr):
    # 获取最大值确定最大位数
    max_value = max(arr)
    max_digits = len(str(max_value))
    
    # 进行基数排序
    for i in range(max_digits):
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = (num // 10**i) % 10
            buckets[digit].append(num)
        arr = [num for bucket in buckets for num in bucket]
    
    return arr

# 生成2000个随机数（10000以内）
random_numbers = [random.randint(0, 10000) for _ in range(2000)]

# 记录开始时间
start_time = time.time()

# 对随机数列表进行排序
sorted_numbers = radix_sort(random_numbers)

# 记录结束时间
end_time = time.time()

# 计算排序所需的时间
duration = end_time - start_time
print("排序完成！用时：{:.6f}秒".format(duration))
