# coding=utf-8
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        # 新建beautifulsoup对象,解析类型为html.parser,编码方式为utf-8
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    # 解析url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # re.compile使用 Python 模块 re（Regular Expression）把正则表达式的模式和标识转化成正则表达式对象
        links = soup.find_all('a',href=re.compile(r"/wiki/"))
        print len(links)
        for link in links:
            # 获得新的urld
            new_url = link['href']
            print new_url
            # 拼接url
            new_full_url = urlparse.urljoin(page_url, new_url)

            new_urls.add(new_full_url)
        return new_urls

    # 解析数据
    def _get_new_data(self, page_url, soup):
        # 将解析到的数据存在字典容器中
        res_data = {}
        res_data['url'] = page_url
        # 获取标题
        title_node = soup.find_all('p')
        content=[]
        for program in title_node
            content.append(program.get_text())
        res_data['data']=content

        return res_data


# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
# # 新建soup对象
# soup=BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
# # 获取所有的链接
# print 'get all links'
# links=soup.find_all('a')
# for link in links:
#     print link.name,link['href'],link.get_text()
#
# print '获取lacie的链接'
# link=soup.find('a',href='http://example.com/lacie')
# print link.name,link,link.get_text()
#
# print '正则匹配'
# link=soup.find('a',href=re.compile(r"ill"))
# print link.name,link,link.get_text()
#
# print '获取p段落文字'
# p_node=soup.find('p',class_="title")
# print p_node.name, p_node.get_text()
