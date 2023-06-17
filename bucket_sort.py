import random
import time

def bucket_sort(arr):
    # 确定桶的数量
    bucket_count = len(arr)
    
    # 创建桶
    buckets = [[] for _ in range(bucket_count)]
    
    # 将元素分配到对应的桶中
    for num in arr:
        index = num // (10000 // bucket_count)
        buckets[index].append(num)
    
    # 对每个桶内部进行排序
    for i in range(bucket_count):
        buckets[i].sort()
    
    # 合并所有桶中的元素
    sorted_arr = [num for bucket in buckets for num in bucket]
    
    return sorted_arr

# 生成2000个随机数（10000以内）
random_numbers = [random.randint(0, 10000) for _ in range(2000)]

# 记录开始时间
start_time = time.time()

# 对随机数列表进行排序
sorted_numbers = bucket_sort(random_numbers)

# 记录结束时间
end_time = time.time()

# 计算排序所需的时间
duration = end_time - start_time
print("排序完成！用时：{:.6f}秒".format(duration))
