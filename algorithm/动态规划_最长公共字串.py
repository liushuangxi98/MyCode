"""
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个.输入：
efgyiffxoonftmmvd
exwzdcwjsttuhsxrcpzplpnfqxqsqtlfctdkgacejitayoafucmfxxhkxyixxykndchyjc
"""
n1,n2 = input(),input()
# 选出短的那个字符串
if len(n1)<len(n2):
    n1,n2 = n2,n1
dp = [[0 for i in range(len(n1))] for i in range(len(n2))]
max_len = 0
res = ''
# 用长的匹配短的，输出第一次遇到的答案
for j in range(1,len(n2)):
    for i in range(1,len(n1)):
        # 如果字符相同，则在上一个基础上加1
        if n1[i-1] == n2[j-1]:
            dp[j][i] = dp[j-1][i-1] +1
        else:
            dp[j][i] = 0
        # 最长的字串，第一次出现即答案
        if max_len < dp[j][i]:
            max_len = dp[j][i]
            res = n2[j-max_len:j]
# for i in dp:
#     print(i)
print(res)
