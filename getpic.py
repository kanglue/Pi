import urllib.request
import socket
import re
import sys
import os
import ssl
from collections import deque
#使用队列存放url
queue = deque()
#使用visited防止重复爬同一页面
visited = set()

targetDir = "/Users/jianglei/Documents/python"

#返回本地文件路径
def destFile(path):
    if not os.path.isdir(targetDir):
        os.makedirs(targetDir)
    pos = path.rindex('/')
    t = os.path.join(targetDir, path[pos + 1:])
    return t

def saveFile(data):
    if not os.path.isdir(targetDir):
        os.makedirs(targetDir)
    save_path = targetDir + "/cap"
    f_obj = open(save_path, 'wb') # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()

if __name__ == "__main__":
    weburl = "http://www.baidu.com"
    context = ssl._create_unverified_context()
    webheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=weburl, headers=webheaders)  # 构造请求报头

    try:
        webpage = urllib.request.urlopen(weburl, context=context)  # 发送请求报头
        contentBytes = webpage.read()
    except Exception:
        print("Timeout")

        # 判断是否为html页面
    if 'html' not in webpage.getheader('Content-Type'):
        print("Not Html")

    contentBytes = contentBytes.decode('UTF-8')
    #保存码流
    saveFile(contentBytes.encode(encoding="utf-8"))
    print(contentBytes)
    list = re.findall(r'(http:[^\s]{3,}(jpg|png|gif))', contentBytes)
    print(list)
    for link in set(list):  # 正则表达式查找所有的图片
        print(link)
        try:
            urllib.request.urlretrieve(link, destFile(link))  # 下载图片
        except:
            print('失败')  # 异常抛出