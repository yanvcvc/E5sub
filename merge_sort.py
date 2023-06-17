import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# 生成2000个随机数（10000以内）
random_numbers = [random.randint(0, 10000) for _ in range(2000)]

# 记录开始时间
start_time = time.time()

# 对随机数列表进行排序
sorted_numbers = merge_sort(random_numbers)

# 记录结束时间
end_time = time.time()

# 计算排序所需的时间
duration = end_time - start_time
print("排序完成！用时：{:.6f}秒".format(duration))
