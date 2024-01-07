#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/11 23:16
# @Author  : 刘双喜
# @File    : get_douyin.py
# @Description : 添加描述
# from openpyxl import load_workbook
# date = load_workbook("input2.xlsx")  # 加载
# sheet = date['input2']
import requests
import re

# 抖音视频链接
url = "https://www.douyin.com/video/7306505378936769842"
import requests, re, json, os

cook = 'douyin.com; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; __ac_nonce=06577293700e728bf7fc1; __ac_signature=_02B4Z6wo00f016DKRAwAAIDCquyfp7l7NTOg6kCAAI1O37; ttwid=1%7CoN4JHR9B4SlqxqLxGZ-PYGL5w8XZjml1VY12_CBS3kw%7C1702308151%7Cebcacc61ceedda0be4b466388c11fde0733c1b6635daa5e39b8897ea0f7e74f2; dy_swidth=2048; dy_sheight=1152; strategyABtestKey=%221702308206.621%22; csrf_session_id=585bd22ece1e85da03ef26ae59493688; s_v_web_id=verify_lq12cqra_fJCtvU0Q_5rDU_4OgK_8RcX_wt2Qwz8OxDS1; passport_csrf_token=255c84154f064dcb0a01ef7bc6c93e15; passport_csrf_token_default=255c84154f064dcb0a01ef7bc6c93e15; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; bd_ticket_guard_client_web_domain=2; ttcid=06cd2a69b0cc44b4bb4190b0c6437d5068; tt_scid=.tFZwa0w1wJbZO1OlW-aeQk8e-tkw9wIc1OHEeht7xfAoywbalPkN9k1en1LMl52333b; download_guide=%222%2F20231211%2F0%22; pwa2=%220%7C0%7C2%7C0%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; n_mh=17NPjzXQgoc553LoqGvjAQ-pTfOhuIfAhAljcosxrW8; sso_uid_tt=b6ea5c7168e4dbeb44aa932773c79cf7; sso_uid_tt_ss=b6ea5c7168e4dbeb44aa932773c79cf7; toutiao_sso_user=f121a6e4c7ebe1b888d28ad8e09d139a; toutiao_sso_user_ss=f121a6e4c7ebe1b888d28ad8e09d139a; passport_assist_user=CjxVvccQAzg-99J-IaPmTDwMsBHF1dc_H7gTx3_e1lQKPCLBdOA8shbT1-4KqsltzKl0Lk5qQGTIX9bNSpgaSgo8h_VgdMXMfOyifsebfBGlHa_hvX8z2vJTZIdnwdMCmIiqb_VOOgR7eEFr0tvb7vb6y_h-9xT_0PAn3FsGEK_Uww0Yia_WVCABIgEDDHLGsw%3D%3D; sid_ucp_sso_v1=1.0.0-KDZhMzlhOGEyMGU3ODRjY2VlNzU1MTYzNWY3MGY3Zjk4NWNjZmQxNDIKHQiJ8tfd6AIQg9rcqwYY7zEgDDCFqbDWBTgGQPQHGgJsZiIgZjEyMWE2ZTRjN2ViZTFiODg4ZDI4YWQ4ZTA5ZDEzOWE; ssid_ucp_sso_v1=1.0.0-KDZhMzlhOGEyMGU3ODRjY2VlNzU1MTYzNWY3MGY3Zjk4NWNjZmQxNDIKHQiJ8tfd6AIQg9rcqwYY7zEgDDCFqbDWBTgGQPQHGgJsZiIgZjEyMWE2ZTRjN2ViZTFiODg4ZDI4YWQ4ZTA5ZDEzOWE; passport_auth_status=f4649e618a36265ecb78733dcb5bb5e6%2C; passport_auth_status_ss=f4649e618a36265ecb78733dcb5bb5e6%2C; uid_tt=430fd33414bc97078f7d0ba0a92d57d4; uid_tt_ss=430fd33414bc97078f7d0ba0a92d57d4; sid_tt=ebf9164b766975bc94c57a7b433488e2; sessionid=ebf9164b766975bc94c57a7b433488e2; sessionid_ss=ebf9164b766975bc94c57a7b433488e2; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2048%2C%5C%22screen_height%5C%22%3A1152%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAok73asIQwxtUa8Qff4Yy6OZUI1GsPoZyLYpLIg8Xqlw%2F1702310400000%2F0%2F1702309180417%2F0%22; LOGIN_STATUS=1; store-region=cn-sh; store-region-src=uid; home_can_add_dy_2_desktop=%221%22; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=973c928ba9c2a9394c3077f7eeab4cd5; __security_server_data_status=1; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSmtlSFBocHhTQllhWEZSNERYUU1lT0wyYzNsTTFHUkxlazRGM3BxOVVGRVJ3dnU2UWxsR3E4Nm9DSkptbnl3cFFEelRZbm1wWjNGYkwwOTBnK3c4SU09IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; sid_guard=ebf9164b766975bc94c57a7b433488e2%7C1702309127%7C5183999%7CFri%2C+09-Feb-2024+15%3A38%3A46+GMT; sid_ucp_v1=1.0.0-KDA4MThiNmY5YjE4MjI2NDAwZTE4ZDkxNDdkOWI4ZTRmODc3ZDEyMWUKGQiJ8tfd6AIQh9rcqwYY7zEgDDgGQPQHSAQaAmhsIiBlYmY5MTY0Yjc2Njk3NWJjOTRjNTdhN2I0MzM0ODhlMg; ssid_ucp_v1=1.0.0-KDA4MThiNmY5YjE4MjI2NDAwZTE4ZDkxNDdkOWI4ZTRmODc3ZDEyMWUKGQiJ8tfd6AIQh9rcqwYY7zEgDDgGQPQHSAQaAmhsIiBlYmY5MTY0Yjc2Njk3NWJjOTRjNTdhN2I0MzM0ODhlMg; msToken=7IKIdHFE4xCQqeaUhi7Cl65NLLEMRHXMpvT8whRn4rlKBJodbX8_f3VRRy0lKhgulliUDKA_9fCd7JcV05ffe1KM4i3LTQlz_Tc8GcyOkG-Nt2TcVZHxNPi217MP; msToken=zBinU75jaKXknO4sOlfzqrCgiK_Zzs3JmJSLcHTCzi2xToNyK8bqUdgJSjiZpVpbnF1qMdEh3aj7cwDI92v5WyH8ykpxdlYVBfBuCNNaw34HF4SV8yMS1Ez09yuG; carnival_live_pull=1702309185221; publish_badge_show_info=%220%2C0%2C0%2C1702309185320%22; odin_tt=9f880011d56e86b949a8e8e0f008a080db1773e85c8dbbd2179aca016edcd4878f9628cfa296e560fae38cfa1f049247; IsDouyinActive=false; passport_fe_beating_status=false'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'cookie': cook}
data = requests.get(url=url, headers=headers)
data.encoding = 'utf-8'
data = data.text

# 使用正则表达式匹配点赞数
likes = re.findall('<span class="CE7XkkTw">(\d?)', data)

print("点赞数: ", likes[0])
