# -*-coding:utf-8 -*-
import urllib2
import urllib
import re
import time
import requests
import html_error2
import download_urls2
from bs4 import BeautifulSoup
import urlparse

class mainmethod(object):
    def __init__(self):
        self.htmlerror = html_error2.html_errorSovler()
        self.htmlurls = download_urls2.load_urls()
    def pachong(self,urll,nnn):
        page_url = 'https://www.gatra.com'
        n = 685
        nn = 100
        while nn<nnn:
            num = nn * 7
            result,result_url = self.htmlurls.geturls(urll,num,n)
            urls = re.findall('<div class="catItemImageBlock-inner">.*?<a href="(.*?)"', result, re.S)
            for url in urls:
                url = urlparse.urljoin(page_url,url)
                print str(n)+'\n'+str(nn)+'\n'
                print url+'\n'
                result1,response_url = self.htmlurls.getcontent(url,n)
                with open('/home/qin/pachong/zy/www.gatra.com.html/html/'+str(n)+'.html','w') as fff:
                    fff.write(result1)
                soup = BeautifulSoup(result1,"html.parser")
                with open('/home/qin/pachong/zy/www.gatra.com.html/data/' + str(n) + '.json', 'a') as uuu:
                    source_id = '65change a web to "https://www.gatra.com"'
                    language = 'eng'
                    request_url = url
                    uuu.write('source_id :' + source_id + '\n' + 'language :' + language + '\n' +'request_url :' + request_url + '\n' + 'response_url :' + response_url.encode('utf-8','ignore') + '\n')
                    classification = soup.find('span', class_='category')
                    uuu.write('classification:'+classification.a.get_text() + '\n')
                    uuu.write('abstract:'+'\n')
                    title = soup.find('h2', class_='itemTitle')
                    uuu.write('title:'+title.get_text().strip().encode('utf-8','ignore') + '\n')
                    bodys = soup.find_all('p')
                    uuu.write('body:'+'\n')
                    for body in bodys:
                        uuu.write(body.get_text().encode('utf-8','ignore') + '\n')
                    uuu.write('\n')
                    pub_time = soup.find('span',class_='itemDateCreated')
                    pub_times = re.search('([A-Za-z]+), ([0-9]+) ([A-Za-z]+) ([0-9]+) ([0-9]+):([0-9]+)', pub_time.get_text())
                    uuu.write('pub_time:' + pub_times.group(4).encode('utf-8','ignore') + '-' + pub_times.group(3).encode('utf-8','ignore') + '-' + pub_times.group(1).encode('utf-8','ignore') + '-' + pub_times.group(2).encode('utf-8','ignore') + ' ' + pub_times.group(5).encode('utf-8','ignore') + ':' + pub_times.group(6).encode('utf-8','ignore') + ':00'+'\n')
                    cole_time = time.time()
                    uuu.write('cole_time:'+str(cole_time)+'\n'+'\n')
                #     # images = re.findall(' src="(.*?)"', result1, re.S)
                    out_first_links = soup.find_all('a', href=re.compile('/.+'))
                    uuu.write('out_links:'+'\n')
                    for out_first_link in out_first_links:
                        new_full_url = urlparse.urljoin(page_url,out_first_link['href'])
                        uuu.write(new_full_url.encode('utf-8','ignore') + '\n')
                    out_links = soup.find_all('a', href=re.compile('h.+'))
                    for out_link in out_links:
                        uuu.write(out_link['href'].encode('utf-8','ignore') + '\n')
                    uuu.write('\n\n'+'images:' + '\n')
                    images = soup.find_all('img')
                    for image in images:
                        uuu.write(image['src'].encode('utf-8','ignore') + '\n')

                n+=1
            nn+=1
        print str(n)+ '\n'

lala = mainmethod()
lala.pachong('https://www.gatra.com/politik/partai?start=',213)
# lala.pachong('https://www.gatra.com/politik/politik?start=',823)
# lala.pachong('https://www.gatra.com/politik/pemilu/kpu?start=',37)
# lala.pachong('https://www.gatra.com/politik/pemilu/bawaslu?start=',11)
# lala.pachong('https://www.gatra.com/politik/pemilu/pilkada?start=',292)
# lala.pachong('https://www.gatra.com/nusantara/nasional?start=',1411)
# lala.pachong('https://www.gatra.com/nusantara/jabodetabek?start=',499)
# lala.pachong('https://www.gatra.com/nusantara/sumatera?start=',169)
# lala.pachong('https://www.gatra.com/nusantara/jawa?start=',1002)
# lala.pachong('https://www.gatra.com/nusantara/kalimantan?start=',39)
# lala.pachong('https://www.gatra.com/nusantara/sulawesi?start=',53)
# lala.pachong('https://www.gatra.com/nusantara/bali-nusa-tenggara?start=',90)
# lala.pachong('https://www.gatra.com/nusantara/maluku-papua?start=',94)
# lala.pachong('https://www.gatra.com/internasional/amerika?start=',77)
# lala.pachong('https://www.gatra.com/internasional/eropa?start=',80)
# lala.pachong('https://www.gatra.com/internasional/timur-tengah?start=',67)
# lala.pachong('https://www.gatra.com/internasional/asia-oseania?start=',126)
# lala.pachong('https://www.gatra.com/ekonomi/makro?start=',323)
# lala.pachong('https://www.gatra.com/ekonomi/properti?start=',103)
# lala.pachong('https://www.gatra.com/ekonomi/finansial?start=',334)
# lala.pachong('https://www.gatra.com/ekonomi/industri?start=',518)
# lala.pachong('https://www.gatra.com/ekonomi/perdagangan?start=',185)
# lala.pachong('https://www.gatra.com/hukum?start=',2954)
# lala.pachong('https://www.gatra.com/life-health/sehat?start=',138)
# lala.pachong('https://www.gatra.com/life-health/intim?start=',4)
# lala.pachong('https://www.gatra.com/olahraga?start=',496)
# lala.pachong('https://www.gatra.com/iltek/gadget?start=',79)
# lala.pachong('https://www.gatra.com/iltek/telko?start=',67)
# lala.pachong('https://www.gatra.com/iltek/sains?start=',60)
# lala.pachong('https://www.gatra.com/iltek/internet?start=',162)
# lala.pachong('https://www.gatra.com/entertainment/apa-siapa?start=',599)
# lala.pachong('https://www.gatra.com/entertainment/musik?start=',351)
# lala.pachong('https://www.gatra.com/entertainment/film?start=',255)
# lala.pachong('https://www.gatra.com/entertainment/televisi?start=',83)


