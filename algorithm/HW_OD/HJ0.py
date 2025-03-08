def count_binary_ones_dp(n, weight):
    # 转换为二进制并去掉前缀'0b'
    binary_str = bin(n)[2:]
    length = len(binary_str)

    # 动态规划表，dp[i][j]表示前i位，小于等于j的二进制数中1的个数
    dp = [[0] * 2 for _ in range(length + 1)]

    # 初始化dp表
    dp[0][0] = 0

    for i in range(1, length + 1):
        # 当前位为0的情况
        dp[i][0] = dp[i - 1][0] * 2  # 前面的位可以是任意0或1
        # 当前位为1的情况
        dp[i][1] = dp[i - 1][0] * 2 + dp[i - 1][1] + int(binary_str[i - 1]) * 2 ** (length - i)

    # 最终答案为小于等于n的所有数中1的个数
    result = dp[length][1]
    return result

def count_numbers_with_weight(n, weight):
    # Initialize the counter to zero
    count = 0

    # Loop through all numbers from 1 to n
    for i in range(1, n + 1):
        # Convert the number to binary and remove the '0b' prefix
        binary_representation = bin(i)[2:]

        # Count the number of '1's in the binary representation
        ones_count = binary_representation.count('1')

        # If the number of '1's is equal to weight, increment the counter
        if ones_count == weight:
            print(binary_representation)
            count += 1

    return count


# Given values
n = 8
weight = 3

# Call the function with given parameters
count = count_numbers_with_weight(n, weight)
result = count_ones(n, weight)
print(count, result)