import re
import requests

# 爬文本
# url = 'https://mp.weixin.qq.com/s?__biz=MzU5MDYwMDA0OQ==&mid=2247485995&idx=3&sn=44cf46cc595d45ab1f991fd799a3559b&chksm=fe3a8835c94d012399e00624aa2f64723646df6eb7d799b5f891df3b515a2ac654c1d3476c12&scene=27'
# agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
# header = {'User-agent': agent}
# response = requests.get(url, headers=header)
# a = response.text
# s = re.findall(re.compile('[\u4e00-\u9fff]+'), a)
# print(s)


# 爬图片
# import requests
# from bs4 import BeautifulSoup
# import os
#
# url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B1%ED%C7%E9%B0%FC&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MTEsMCwzLDYsMSw1LDQsMiw3LDgsOQ%3D%3D'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# img_tags = soup.find_all('img')
# urls = [img['src'] for img in img_tags]
#
# if not os.path.exists('images'):
#     os.makedirs('images')
#
# for url in urls:
#     response = requests.get(url)
#     filename = os.path.join('images', url.split('/')[-1])
#     with open(filename, 'wb') as f:
#         f.write(response.content)

from selenium import webdriver
import os
import time
import requests

count = 100
save_path = '23.爬虫'
url_ls = []
# url_ls.append('https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B1%ED%C7%E9%B0%FC&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MTEsMCwzLDYsMSw1LDQsMiw3LDgsOQ%3D%3D')
# 程序员
# url_ls.append('https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1685160250076_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MTEsMCwzLDIsNCwxLDYsNSw3LDgsOQ%3D%3D&ie=utf-8&sid=&word=%E8%A1%A8%E6%83%85%E5%8C%85%E7%A8%8B%E5%BA%8F%E5%91%98')
# 动图,目前有bug，跑不出来
# url = 'https://image.baidu.com/search/index?ct=201326592&tn=baiduimage&word=%E8%A1%A8%E6%83%85%E5%8C%85&pn=&spn=&ie=utf-8&oe=utf-8&cl=2&lm=6&fr=ala&se=&sme=&hd=0&latest=0&copyright=0&cs=&os=&objurl=&di=&gsm=1fe&dyTabStr=MTEsMCwzLDYsMSw1LDQsMiw3LDgsOQ%3D%3D'
# 沙雕
# url_ls.append('https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1685162924862_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MTEsMCwzLDIsNCwxLDYsNSw3LDgsOQ%3D%3D&ie=utf-8&sid=&word=%E8%A1%A8%E6%83%85%E5%8C%85%E6%B2%99%E9%9B%95')
# 怼人
# url_ls.append('https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1685164355725_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MTEsMCwzLDIsNCwxLDYsNSw3LDgsOQ%3D%3D&ie=utf-8&sid=&word=%E8%A1%A8%E6%83%85%E5%8C%85%E6%80%BC%E4%BA%BA')
# 可爱
# url_ls.append('https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1685165974714_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MTEsMCwzLDIsNCwxLDYsNSw3LDgsOQ%3D%3D&ie=utf-8&sid=&word=%E8%A1%A8%E6%83%85%E5%8C%85+%E5%8F%AF%E7%88%B1&f=3&oq=%E8%A1%A8%E6%83%85%E5%8C%85&rsp=3')
# 王者容易
# url_ls.append('https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1685166445706_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MTEsMCwzLDIsNCwxLDYsNSw3LDgsOQ%3D%3D&ie=utf-8&sid=&word=%E8%A1%A8%E6%83%85%E5%8C%85%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&f=3&oq=%E8%A1%A8%E6%83%85%E5%8C%85%E7%8E%8B%E8%80%85&rsp=0')
# 上班搞怪
url_ls.append('https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1685166589438_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MTEsMCwzLDIsNCwxLDYsNSw3LDgsOQ%3D%3D&ie=utf-8&sid=&word=%E8%A1%A8%E6%83%85%E5%8C%85%E4%B8%8A%E7%8F%AD%E6%90%9E%E6%80%AA')

def get_img(url_ls):
    for url in url_ls:
        driver = webdriver.Chrome()
        driver.get(url)

        # 滚动页面以加载更多图片
        for i in range(count):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

        # 获取图片链接
        img_tags = driver.find_elements('xpath', '//img[@class="main_img img-hover"]')
        urls = [img.get_attribute('src') for img in img_tags]

        driver.close()

        if not os.path.exists(save_path):
            os.makedirs(save_path)

        for i, url in enumerate(urls):
            try:
                response = requests.get(url)
                filename = os.path.join(save_path, f'image_{i}.jpg')
                with open(filename, 'wb') as f:
                    f.write(response.content)
            except:
                print('error')

if __name__ == '__main__':
    get_img(url_ls)