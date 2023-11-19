#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/12 22:54
# @Author  : 刘双喜
# @File    : HJ95.py
# @Description : 逻辑
# https://www.nowcoder.com/practice/00ffd656b9604d1998e966d555005a4b?tpId=37&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D2%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=&judgeStatus=&tags=&title=&gioEnter=menu
# 核心解题思路：大于0的数放左边，小于0的放右边。左边每4位为一组，添加'仟', '佰', '拾'，再replace掉特殊情况。


def fun():
    def print_epoch(four_num, big_unit):
        # 每四位数字化为一个单位
        unit, s, four_num = ['仟', '佰', '拾'], '', four_num.rjust(4, '0')
        if int(four_num[0]) > 0:
            s += num_map_word[int(four_num[0])] + unit[0]
            s += num_map_word[int(four_num[1])] + (unit[1] if int(four_num[1]) != 0 else '')
            s += num_map_word[int(four_num[2])] + (unit[2] if int(four_num[2]) != 0 else '')
            s += num_map_word[int(four_num[3])] if int(four_num[3]) != 0 else ''
        elif int(four_num[1]) > 0:
            s += num_map_word[int(four_num[1])] + unit[1]
            s += num_map_word[int(four_num[2])] + (unit[2] if int(four_num[2]) != 0 else '')
            s += num_map_word[int(four_num[3])] if int(four_num[3]) != 0 else ''
        elif int(four_num[2]) > 0:
            s += (num_map_word[int(four_num[2])] if int(four_num[2]) != 1 else '') + unit[2]
            s += num_map_word[int(four_num[3])]
        else:
            s += num_map_word[int(four_num[3])] if int(four_num[3]) != 0 else ''
        s = (s + big_unit).replace('零零', '零').replace('零壹拾', '零拾').replace('仟零万', '仟万').replace('万万', '亿')
        return s

    def print_two(s):
        res = f'{num_map_word[int(s[0])]}角{num_map_word[int(s[1])]}分'
        res = res.replace('零角零分', '整').replace('零角', '').replace('零分', '')
        return res
    # 数字对应中文的列表
    num_map_word = '零、壹、贰、叁、肆、伍、陆、柒、捌、玖、拾'.split('、')
    left, right = input().split('.')
    # 小数点左边的
    left_list = [left[max(i - 4, 0):i] for i in range(len(left), 0, -4)][::-1]
    ret = [print_epoch(i, '万' * idx) for idx, i in enumerate(left_list[::-1])]
    ret = ['人民币'] + ret[::-1] + ['元']
    # 小数点右边的
    ret.append(print_two(right))
    # 最终合并的结果
    ret_final = ''.join(ret).replace('人民币元', '人民币')
    print(ret_final)


fun()
