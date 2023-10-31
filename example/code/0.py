while 1:
    try:
        s = [int(input()) for i in range(int(input()))]
        s.sort()
        for i in s:
            print(i)
    except:
        break
