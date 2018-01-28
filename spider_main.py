# coding=utf-8
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self, ):
        # 初始化url管理器
        self.urls = url_manager.Urlmanager()
        # 初始化url下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 初始化url解析器
        self.parser = html_parser.HtmlParser()
        # 初始化输出器
        self.outputer = html_outputer.HtmlOutputer()

    # 爬虫调度程序
    def craw(self, root_url):
        count = 1
        # 添加入口url到url管理器
        self.urls.add_new_url(root_url)
        # 从url管理器获取url
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count = count + 1
            except:
                print 'craw failed'
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
