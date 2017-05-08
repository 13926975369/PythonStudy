# -*-coding:utf-8 -*-
import requests

class HtmlDownloader(object):
    def download(self,url):
        res = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
        }, proxies={
            'http': 'http://127.0.0.1:37867',
            'https': 'https://127.0.0.1:37867'
        })
        result = res.content
        response_url = res.url
        return result,response_url