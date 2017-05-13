# -*-coding:utf-8 -*-
import html_downloader

#出现错误的时候用递归反复发出请求
class html_errorSovler(object):
    def __init__(self):
        self.htmlDownloader=html_downloader.HtmlDownloader()

    def errorRedo(self,url,cot):
        try:
            print 'RE:craw %d: %s' % (cot, url)
            html_cont,response_url=self.htmlDownloader.download(url)
            return html_cont,response_url
        except Exception, e:
            html_cont,response_url=self.errorRedo(url,cot)
            return html_cont,response_url