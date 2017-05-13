# -*-coding:utf-8 -*-
import requests

class HtmlDownloader(object):
    def download(self,url):
        res = r = requests.post(url, data=url, proxies={
            'http': 'http://127.0.0.1:37867',
            'https': 'https://127.0.0.1:37867'
        })
        result = res.content
        response_url = res.url
        return result,response_url