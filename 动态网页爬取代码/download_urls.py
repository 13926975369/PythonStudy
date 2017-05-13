# -*-coding:utf-8 -*-
import requests
import html_error


class load_urls(object):
    def __init__(self):
        self.htmlerror=html_error.html_errorSovler()

    def geturls(self,url,num,n):
        try:
            res =  r = requests.post(url='http://www.tnp.sg/views/ajax',data=url, proxies={
                'http': 'http://127.0.0.1:37867',
                'https': 'https://127.0.0.1:37867'
            })
            result = res.content
            response_url = res.url
            return result,response_url
        except Exception, e:
            result,response_url = self.htmlerror.errorRedo(url,n)
            return result,response_url

    def getcontent(self,url,num):
        try:
            res = r = requests.post(url='http://www.tnp.sg/sports/football/target-man-left-winger-and-fullback-all-rolled-one', data=url, proxies={
                'http': 'http://127.0.0.1:37867',
                'https': 'https://127.0.0.1:37867'
            })
            result = res.content
            response_url = res.url
            return result,response_url
        except Exception, e:
            result,response_url = self.htmlerror.errorRedo(url,num)
            return result,response_url