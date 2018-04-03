# coding=utf-8
import cookielib
import urllib2
#
# url = "http://www.baidu.com"
#
# print "第一种方法"
# response1 = urllib2.urlopen(url)
# print response1.getcode()
# print len(response1.read())
#
# print "第二种方法"
# request = urllib2.Request(url)
# request.add_header("user-agent", "Mozilla/5.0")
# response2 = urllib2.urlopen(request)
# print response2.getcode()
# print len(response2.read())
#
# print "第三种方法"
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# urllib2.install_opener(opener)
# response3 = urllib2.urlopen(url)
# print response3.getcode()
# # 打印cookie
# print cj
# # 打印网页内容
# print response3.read()


class HtmlDownloader(object):
    def download(self, url):
        # url为空则不做处理
        if url is None:
            return None
        # 新建response对象，获取页面对象
        response = urllib2.urlopen(url)
        # 若响应不成功，则不做处理
        if response.getcode() != 200:
            return None
        # 否则，读取页面内容
        return response.read()
