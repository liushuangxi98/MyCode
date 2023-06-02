import bisect


# 二分法求法：# 先取出列表第一个元素放在待定的最长递增子序列列表里，再循环其他元素，如果i大于最长递增子序列就添加到其最后，如果i小于就把i替换掉最长递增子序列比它大的第一个数
def lis(in_arr):
    longest = [1] * len(in_arr)
    result = [in_arr[0]]
    arr_ls = list(enumerate(in_arr, 0))
    for idx, value in arr_ls[1:]:
        if value > result[-1]:
            result.append(value)
            longest[idx] = len(result)
        else: # 打不过就加入的原则
            idx = bisect.bisect_left(result, value)
            result[idx] = value
            longest[idx] = longest[idx - 1]
    return longest, result


# 动态规划求法
def func(l):
    # 第一步创建保存右边比左边大的初始值，每个值的初始值都为1
    dp = [1] * len(l)

    for i in range(len(l)):
        for j in range(i):
            if l[i] > l[j]:
                # 相当于选择排序，轮到该值的时候和前面的值进行依次比较，如果比前值大，dp列表中就在前值的基础上加1
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    return max(dp)


arr = [10, 22, 9, 10, 33, 21, 50, 41, 60, 80]
print(lis(arr))
print(func(arr))
