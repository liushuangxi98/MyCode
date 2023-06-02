from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import requests

url = 'https://image.baidu.com/search/index?ct=201326592&tn=baiduimage&word=%E8%A1%A8%E6%83%85%E5%8C%85&pn=&spn=&ie=utf-8&oe=utf-8&cl=2&lm=6&fr=ala&se=&sme=&hd=0&latest=0&copyright=0&cs=&os=&objurl=&di=&gsm=1fe&dyTabStr=MTEsMCwzLDYsMSw1LDQsMiw3LDgsOQ%3D%3D'

driver = webdriver.Chrome()
driver.get(url)

# 滚动页面以加载更多图片
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

# 获取图片元素
img_tags = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//img[@class="main_img img-hover"]')))

# 获取图片链接
urls = []
for img in img_tags:
    # 点击图片以显示大图
    img.click()
    time.sleep(1)

    # 获取大图URL
    img_url = driver.find_element('xpath', '//img[@class="currentImg"]')
    urls.append(img_url.get_attribute('src'))

driver.close()

if not os.path.exists('images'):
    os.makedirs('images')

for i, url in enumerate(urls):
    response = requests.get(url)
    filename = os.path.join('images', f'image_{i}.gif')
    with open(filename, 'wb') as f:
        f.write(response.content)
