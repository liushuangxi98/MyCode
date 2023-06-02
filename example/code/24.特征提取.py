#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 20:45
# @Author  : 刘双喜
# @File    : 24.特征提取.py
# @Description : 添加描述
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


def dict_feature_extra():
    """
    对字典进行特征提取
    :return:
    """
    data = [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}]
    # 实例化转换器
    transfer = DictVectorizer(sparse=False)  # sparse默认True
    # 训练
    data = transfer.fit_transform(data)
    print(f'结果：{data}')
    print(f'特征名字:\n:{transfer.get_feature_names_out()}')

def txt_english_feature_extra():
    """
    对文本进行特征提取, 默认以空格分隔
    :return:
    """
    data = ["life is short,i like python", "life is too long,i dislike python"]
    # 实例化转换器
    transfer = CountVectorizer()
    # 训练
    data = transfer.fit_transform(data)
    print(f'结果：{data.toarray()}')
    print(f'特征名字:\n:{transfer.get_feature_names_out()}')

def txt_chinese_feature_extra():
    """
    对中文文本进行特征提取, 先转换成空格的形式
    :return:
    """
    def word_cut(txt):
        """
        将一句话按照中文习惯以空格断句
        :return:
        """
        import jieba
        ls_txt = list(jieba.cut(txt))
        res = ' '.join(ls_txt)
        return res

    data = ["《三体》，豆瓣9分，，主演：张鲁一 于和伟 陈瑾 王子文 林永健 李小冉 王传君 张帆 白客 涂松岩 刘敏 孔琳 张峻.",
            "2007年，地球基础科学出现了异常的扰动，一时间科学界风雨飘飘，人心惶惶。离奇自杀的科学家，近乎神迹的倒计时，行事隐秘的科学边，神秘莫测的《三体》游戏……纳米科学家汪淼被警官史强带到联合作战中心，并潜入名为“科学边界”的组织协助调查。",
            "迷雾之中，汪淼接触到一个名为ETO的 组织，发现其幕后统帅竟是自杀身亡的科学家杨冬的母亲——叶文洁。随着ETO与作战中心你来我往的不断博弈，汪淼和史强逐渐确定《三体》游戏中的世界真实存在。而所有事件的源起，是两个文明为了生存空间，孤注一掷的生死相逐。在联合作战中心及科学家们的共同努力下，汪淼、史强等人坚定信念、重燃希望，带领大家继续准备着在今后与即将入侵的三体人展开殊死斗争"]
    data_cut = [word_cut(txt) for txt in data]
    # 实例化转换器
    transfer = CountVectorizer()
    # 训练
    data = transfer.fit_transform(data_cut)
    print(f'结果：{data.toarray()}')
    print(f'特征名字:\n:{transfer.get_feature_names_out()}')

def txt_chinese_tfidf_extra():
    """
    对中文文本进行特征提取, 先转换成空格的形式, 计算词频
    :return:
    """
    def word_cut(txt):
        """
        将一句话按照中文习惯以空格断句
        :return:
        """
        import jieba
        ls_txt = list(jieba.cut(txt))
        res = ' '.join(ls_txt)
        return res

    data = ["《三体》，豆瓣9分，，主演：张鲁一 于和伟 陈瑾 王子文 林永健 李小冉 王传君 张帆 白客 涂松岩 刘敏 孔琳 张峻.",
            "2007年，地球基础科学出现了异常的扰动，一时间科学界风雨飘飘，人心惶惶。离奇自杀的科学家，近乎神迹的倒计时，行事隐秘的科学边，神秘莫测的《三体》游戏……纳米科学家汪淼被警官史强带到联合作战中心，并潜入名为“科学边界”的组织协助调查。",
            "迷雾之中，汪淼接触到一个名为ETO的 组织，发现其幕后统帅竟是自杀身亡的科学家杨冬的母亲——叶文洁。随着ETO与作战中心你来我往的不断博弈，汪淼和史强逐渐确定《三体》游戏中的世界真实存在。而所有事件的源起，是两个文明为了生存空间，孤注一掷的生死相逐。在联合作战中心及科学家们的共同努力下，汪淼、史强等人坚定信念、重燃希望，带领大家继续准备着在今后与即将入侵的三体人展开殊死斗争"]
    data_cut = [word_cut(txt) for txt in data]
    # 实例化转换器
    transfer = TfidfVectorizer(stop_words=['一个', '为了'])
    # 训练
    data = transfer.fit_transform(data_cut)
    print(f'结果：{data.toarray()}')
    print(f'特征名字:\n:{transfer.get_feature_names_out()}')

txt_chinese_tfidf_extra()