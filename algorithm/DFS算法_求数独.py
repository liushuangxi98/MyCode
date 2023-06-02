def check(row, col, val):
    data_row = array[row]
    data_col = [array[i][col] for i in range(9)]
    grid_list = [i[0 + int(col / 3) * 3:3 + int(col / 3) * 3] for i in array[0 + int(row / 3) * 3:3 + int(row / 3) * 3]]
    data_grid = []
    for i in grid_list:
        data_grid.extend(i)
    if val not in data_col and val not in data_row and val not in data_grid:
        return True
    else:
        return False


def find(row, col):
    data_col = [array[i][col] for i in range(9)]
    no_row = {i for i in range(1, 10) if i not in array[row]}
    no_col = {i for i in range(1, 10) if i not in data_col}
    no_grid = set(range(10))
    data_grid = [i[0 + int(col / 3) * 3:3 + int(col / 3) * 3] for i in array[0 + int(row / 3) * 3:3 + int(row / 3) * 3]]
    for i in data_grid:
        for j in i:
            try:
                no_grid.remove(j)
            except:
                pass
    return no_col & no_row & no_grid


def dsf(row, col):
    if col == 9:
        row += 1
        col = 0
    if row == 9 and col == 0:
        global find_answer
        find_answer = True
        return ''
    if array[row][col] == 0:
        for i in find(row, col):
            if check(row, col, i):
                array[row][col] = i
                dsf(row, col + 1)
                if find_answer:
                    return ''
                array[row][col] = 0
    else:
        dsf(row, col + 1)


def out():
    for i in array:
        for j in i:
            print(j, sep='', end=' ')
        print()

array = [input().split() for i in range(9)]

for i in range(9):
    for j in range(9):
        array[i][j] = int(array[i][j])
#输入的是一个9*9数独二维列表
#array = [[0, 9, 2, 4, 8, 1, 7, 6, 3], [4, 1, 3, 7, 6, 2, 9, 8, 5], [8, 6, 7, 3, 5, 9, 4, 1, 2], [6, 2, 4, 1, 9, 5, 3, 7, 8], [7, 5, 9, 8, 4, 3, 1, 2, 6], [1, 3, 8, 6, 2, 7, 5, 9, 4], [2, 7, 1, 5, 3, 8, 6, 4, 9], [3, 8, 6, 9, 1, 4, 2, 5, 7], [0, 4, 5, 2, 7, 6, 8, 3, 1]]

find_answer = False
dsf(0, 0)
out()

