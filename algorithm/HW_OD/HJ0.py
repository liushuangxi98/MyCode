def get_longest(num_list):
    dp = [1 for i in num_list]
    for i in range(1,len(num_list)):
        for j in range(0, i):
            if num_list[i] > num_list[j]:
                dp[i] = max(dp[i], dp[j]+1)
            elif num_list[i] == num_list[j]:
                dp[i] = dp[j]
    return dp


n, people_list = int(input()), list(map(int, input().split()))
left,right = get_longest(people_list),get_longest(people_list[::-1])[::-1]
longest = [left[i]+right[i] for i in range(len(people_list))]
print(n - max(longest)+1)