def fun(num):
    count =int((2*num+0.25)**0.5-0.5)+1     # num最多等于count个数相加
    if num%2 == 1:                          # num是奇数的情况下，必定可以
        return 'YES'
    else:                                   # num是偶数的情况
        for i in range(3,count):            # 可以等于i个数相加
            if i%2 == 1:                    # i是奇数
                if num%i == 0:              # 能等于奇数个连续数相加，必定是它的倍数
                    print(i)
                    return 'YES'
                else:
                    continue
            else:
                if i%4 == 2:                # 由于4个连续数相加必为偶数，6个连续数相加必为奇数，所以余2时的情况不可能
                    continue
                else:
                    if (num-(i+1)*i/2) % i == 0:
                        print(num-(i+1)*i/2, i)
                        return 'YES'
                    else:
                        continue
        return "NO"


if __name__ == '__main__':
    print(fun(14156))