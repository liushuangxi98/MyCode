#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/10 23:30
# @Author  : 刘双喜
# @File    : HJ71.py
# @Description : https://www.nowcoder.com/practice/43072d50a6eb44d2a6c816a283b02036?tpId=37&tqId=21294&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
import time


def fun():
    rule, s = input().lower(), input().lower()
    is_match = []

    def dfs(i_s, i_rule):
        # s当前位置都到最后了
        if i_s == len(s) and i_rule == len(rule):  # rule也到最后则ok
            return True
        elif i_s == len(s) and i_rule != len(rule):
            if set(rule[i_rule:]) == set('*'):  # rule未到最后但是后面都是*可不匹配也ok
                return True
            else:
                return False
        elif i_s != len(s) and i_rule == len(rule):  # s还没结束 rule结束了，不ok
            return False
        # 记录匹配的位置
        if (i_s, i_rule) not in is_match:
            is_match.append((i_s, i_rule))
        else:
            return False
        # 当前位置相等的时候，下一个位置
        if rule[i_rule] == s[i_s]:
            return dfs(i_s + 1, i_rule + 1)
        # 当前位置不相等的时候
        else:
            # 如果通配符是？，并且当前位置是字母或英文，下一个位置
            if rule[i_rule] == '?' and s[i_s].isalnum():
                return dfs(i_s + 1, i_rule + 1)
            # 如果通配符是* ，判断rule下一个位置是否相等，
            elif rule[i_rule] == '*':
                # *匹配
                if s[i_s].isalnum() and dfs(i_s + 1, i_rule):
                    return True
                # *不匹配
                elif dfs(i_s, i_rule + 1):
                    return True
                else:
                    return False
            else:
                return False

    if dfs(0, 0):
        print('true')
    else:
        print('false')


def fun2():
    def dfs(s: str, rule: str):
        if (s, rule) in visit:  # 当前组合已经访问过了就抬走
            return False
        visit.append((s, rule))
        if s == '' and rule == '':  # s完毕且rule刚好完毕，ok
            return True
        elif s != '' and rule == '':  # s未完毕，rule完毕，gg
            return False
        elif s == '' and rule != '':  # s完毕，rule未完毕，看rule是否只剩下*
            if rule.replace('*', '') == '':  # 只剩下*，ok
                return True
            else:  # 还有其他rule值，gg
                return False
        # 直接就相等抬走下一位
        if s[0] == rule[0]:
            return dfs(s[1:], rule[1:])
        else:
            # 是？的时候必须要是数字字母才进入匹配
            if rule[0] == '?' and s[0].isalnum():
                return dfs(s[1:], rule[1:])
            # 是*的时候分进入和跳过
            elif rule[0] == '*':
                # * 匹配，s往后移
                if s[0].isalnum() and dfs(s[1:], rule):
                    return True
                # * 不匹配， rule往后移
                elif dfs(s, rule[1:]):
                    return True
                else:
                    return False

    rule, s, visit = input().lower(), input().lower(), []
    print('true' if dfs(s, rule) else 'false')

fun2()
