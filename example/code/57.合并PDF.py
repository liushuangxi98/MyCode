#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/11 9:58
# @Author  : 刘双喜
# @File    : 57.合并PDF.py
# @Description : 添加描述
import os
from PyPDF2 import PdfMerger


def merge_pdfs_in_directory(dir_path, output_filename):
    merger = PdfMerger()

    for item in os.listdir(dir_path):
        if item.endswith('.pdf') and '发票' in item:
            merger.append(os.path.join(dir_path, item))

    merger.write(os.path.join(dir_path, output_filename))
    merger.close()


# 使用方法：指定你想要合并PDFs的目录和输出文件名
merge_pdfs_in_directory(r'E:\file\杂项\入职前材料', '发票.pdf')
