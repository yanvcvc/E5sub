import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # 进行 n-1 轮遍历
        for j in range(n - 1 - i):  # 每轮遍历比较的次数逐渐减少
            if arr[j] > arr[j + 1]:  # 如果相邻元素逆序，则交换它们
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 生成随机数列表
random_nums = [random.randint(1, 100) for _ in range(10)]
print("随机数列表:", random_nums)

# 对随机数列表进行冒泡排序
bubble_sort(random_nums)
print("排序后列表:", random_nums)
