# 题目描述 ：找到两两相加为素数的最多组合
# 输入:n个数（n为偶数）
# 输出:
# 输出一个整数 K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 将奇数步入函数，for i 循环偶数。 如果偶数的值加奇数为素数并且偶数在这个奇数这一轮没有被使用过，就标记它被使用过。如果偶数还没有配对，则给这个偶数配对这个奇数.
# 如果偶数已经配对了（上一个奇数配对的，但是这轮奇数它是第一次被使用），则查找这个偶数配对的奇数还能不能和这轮没被使用的其他偶数配对。
def is_find(odd):
    for i in range(0, len_evens):
        if is_prime(evens[i][0] + odd) and used_even[i] == 0:  # 如果偶数的值加奇数为素数并且偶数在这个奇数这一轮没有被使用过
            used_even[i] = 1    # 就标记它被使用过。
            if evens[i][1] == 0 or is_find(evens[i][1]):  # 如果偶数还没有配对，
                evens[i][1] = odd  # 则给这个偶数配对这个奇数.
                return True
            elif is_find(evens[i][1]):  # 如果偶数已经配对了（上一个奇数配对的，但是这轮奇数它是第一次被使用），
                evens[i][1] = odd  # 则查找这个偶数配对的奇数还能不能和这轮没被使用的其他偶数配对。
                return True
    return False


n = '24106 14792 27877 13661 7471 21045 13828 1032 24576 16049 16931 3074 3237 29320 1832 6895 7390 5644 6882 ' \
    '2519 13158 22488 28893 2038 28137 16928 24223 5830 3706 4456 1295 10279 6901 28354 27201 6282 16136 ' \
    '14929 12617 20688'
count = 0
nums = n.split(' ')

evens = [int(i) for i in nums if int(i) % 2 == 0]
odds = [int(i) for i in nums if int(i) % 2 != 0]
evens = [list(i) for i in list(zip(evens, len(evens) * [0]))]

len_evens = len(evens)
for i in odds:
    used_even = [0] * len_evens
    if is_find(i):
        count += 1
print(count)
