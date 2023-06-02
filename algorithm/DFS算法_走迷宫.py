def dfs(x, y):
    global find_answer
    # 当走到终点,不再进行递归
    if x == n-1 and y == m-1:
        find_answer = True
        return ''
    # 往右下左上试探，遍历x，y的增量
    for i, j in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        x = x + i
        y = y + j
        # 当在边境内，并且该试探方向可以访问且未被访问
        if 0 <= x <= n - 1 and 0 <= y <= m - 1 and array[x][y] == '0' and visited[x][y] != True:
            visited[x][y] = True
            path.append(f'({x},{y})')
            dfs(x, y)
            # 当走到终点，不再进行回溯，直接让所有递归终结
            if find_answer:
                return ''
            # 当没走到终点，进行回溯，清除足迹，同时回溯x,y
            visited[x][y] = False
            path.pop()
            x = x - i
            y = y - j
        # 当该试探方向不可行，进行回溯
        else:
            x = x-i
            y = y-j
'''
4 6
0 0 1 1 1 1
1 0 1 0 0 0
1 0 0 0 1 0
1 1 1 1 0 0
'''


n,m = list(map(int,input().split(' ')))
array = [input().split(' ') for i in range(n)]
visited = [[False] * m for i in range(n)]
find_answer = False
path=['(0,0)']
path.sort()
x, y = 0, 0
visited[0][0] = True  # 起点已走过
dfs(x, y)
for i in visited:
    print(i)
print(path)