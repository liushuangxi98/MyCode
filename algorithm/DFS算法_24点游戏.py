from itertools import permutations
def fun(nums):
    def dfs(idx):
        nonlocal res
        nonlocal old
        global find_ans
        if res == 24 and idx == 4:
            find_ans = True
        if idx >= 4:
            return
        for i in ['+', '-', '*', '/']:
            old = res
            res = eval(f'res{i}{nums[idx]}')
            dfs(idx + 1)
            if find_ans:
                # 由深层递归输出运算过程，便于理解
                # print(i,nums[idx])
                return
            res = old
        return

    res = nums[0]
    old = 0
    dfs(1)


find_ans = False
inp = list(map(int, input().split()))
for i in list(permutations(inp)):
    fun(i)

if find_ans:
    print('true')
else:
    print('false')