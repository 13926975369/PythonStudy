# -*-coding:utf-8 -*-
import requests
import html_error2


class load_urls(object):
    def __init__(self):
        self.htmlerror=html_error2.html_errorSovler()

    def geturls(self,url,num,n):
        try:
            res = requests.get(url + str(num), headers={
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
            }, proxies={
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
            res = requests.get(url, headers={
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
            }, proxies={
                'http': 'http://127.0.0.1:37867',
                'https': 'https://127.0.0.1:37867'
            })
            result = res.content
            response_url = res.url
            return result,response_url
        except Exception, e:
            result,response_url = self.htmlerror.errorRedo(url,num)
            return result,response_url