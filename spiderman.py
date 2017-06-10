import urllib.request

class Baidu:
    def __init__(self, baseUrl, para):
        self.baseURL = baseUrl
        self.param = para

    def getPage(self, pageNum):

        url = "http://www.baidu.com"
        webheader1 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        webheader2 = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
            #'Accept-Encoding': 'gzip, deflate',
            'Host': 'www.douban.com',
            'DNT': '1'
            }
        req = urllib.request.Request(url=url, headers=webheader2)
        webPage = urllib.request.urlopen(url)
        data = webPage.read()
        data = data.decode('UTF-8')
        print(type(webPage))
        print("URL: " + webPage.geturl())
        print(webPage.info())
        print(webPage.getcode())
        print("\nData: \n" + data)