import random
import time

def counting_sort(arr):
    # 找出最大值和最小值
    min_value = min(arr)
    max_value = max(arr)
    
    # 统计每个元素出现的次数
    count = [0] * (max_value - min_value + 1)
    for num in arr:
        count[num - min_value] += 1
    
    # 根据统计结果进行排序
    sorted_arr = []
    for i in range(len(count)):
        while count[i] > 0:
            sorted_arr.append(i + min_value)
            count[i] -= 1
    
    return sorted_arr

# 生成2000个随机数（10000以内）
random_numbers = [random.randint(0, 10000) for _ in range(2000)]

# 记录开始时间
start_time = time.time()

# 对随机数列表进行排序
sorted_numbers = counting_sort(random_numbers)

# 记录结束时间
end_time = time.time()

# 计算排序所需的时间
duration = end_time - start_time
print("排序完成！用时：{:.6f}秒".format(duration))
