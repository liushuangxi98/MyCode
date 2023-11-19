def fun2():
    def is_prime(_value):
        if _value == 1:
            return False
        for _i in range(2, 1 + int(_value ** 0.5)):
            if _value % _i == 0:
                return False
        return True

    # 遍历每一个左边节点，给它找一个右边节点
    def find(i):
        for j, right in enumerate(right_lis):  # 遍历右
            if matchable[i][j] and left_visit_right[i][j] is False:  # 如果左右能匹配,且没访问过
                left_visit_right[i][j] = True
                if match_dict.get(j) is None:  # 右边没有匹配
                    match_dict[j] = i  # 给右边匹配左边
                    return True
                elif find(match_dict.get(j)):  # 右边已经匹配上了左某，试着给左某的再找过一个
                    match_dict[j] = i  # 如果能给左某找到，则右现匹配左现
                    return True
        return False

    n = input()
    arr = list(map(int, input().split()))
    left_lis = [i for i in arr if i % 2 == 0]  # 二分图左边
    right_lis = [i for i in arr if i % 2 != 0]  # 二分图右边
    matchable = [[is_prime(i + j) for j in right_lis] for i in left_lis]  # 二分图里所有可能的路径能否匹配的结果
    match_dict = dict()
    for i, left in enumerate(left_lis):
        left_visit_right = {i: [False for j in right_lis] for i in range(len(left_lis))}  # 每一个左边保存一个它右边是否访问列表
        find(i)
    print(len(match_dict))


fun2()
