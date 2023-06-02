#nums = list(map(int,input().split()))
nums = [9,3,3,4]
#nums = [7,2,1,10]
res = nums[0]
old = 0
find_ans = False
def dfs(idx):
    global res
    global find_ans
    if res == 24 and idx == 4:
        find_ans = True
    if idx >= 4:
        return
    for i in ['+', '-', '*', '/']:
        old = res
        res =eval(f'res{i}{nums[idx]}')
        dfs(idx+1)
        if find_ans:
            # 由深层递归输出运算过程，便于理解
            #print(i,nums[idx])
            return
        res = old
    return
dfs(1)
if find_ans:
    print('true')
else:
    print('false')