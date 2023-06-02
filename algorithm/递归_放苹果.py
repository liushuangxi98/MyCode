'''
放苹果分为两种情况，一种是有盘子为空，一种是每个盘子上都有苹果。
令(m,n)表示将m个苹果放入n个盘子中的摆放方法总数。
1.假设有一个盘子为空，则(m,n)问题转化为将m个苹果放在n-1个盘子上，即求得(m,n-1)即可
2.假设所有盘子都装有苹果，则每个盘子上至少有一个苹果，即最多剩下m-n个苹果，问题转化为将m-n个苹果放到n个盘子上
即求(m-n，n)
'''
def f(m,n):
    if m<0 or n<0:
        return 0
    elif m==1 or n==1:
        return 1
    else:
        return f(m,n-1)+f(m-n,n)
while True:
    try:
        m,n=map(int,input().split())
        print(f(m,n))
    except:
        break