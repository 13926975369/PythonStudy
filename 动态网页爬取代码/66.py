# -*-coding:utf-8 -*-
import urllib2
import urllib
import re
import time
import requests
import html_error
import download_urls
from bs4 import BeautifulSoup
import urlparse

class mainmethod(object):
    def __init__(self):
        self.htmlerror = html_error.html_errorSovler()
        self.htmlurls = download_urls.load_urls()
    def pachong_sports(self,nn,numm,page,zhengze):
        page_url = 'http://www.tnp.sg'
        n = nn
        num = numm
        while num<page:
            params_sports = {
                'view_name': 'articles',
                'view_display_id': 'story_card_by_url_term_infinite',
                'view_args': '4',
                'view_path': 'taxonomy/term/4',
                'view_path': '',
                'view_dom_id': '37ac4e76a043770a96f87a0b41f7bc8e',
                'pager_element': '0',
                'views_exclude_previous': 'views_exclude_previous_GDyYZ_M4RMAU4RTy_fV6zqC2tAanBhTTJP8uDF-54ZI',
                'page': num
            }
            result,result_url = self.htmlurls.geturls(params_sports,num,n)
            urls = re.findall(zhengze , result, re.S)
            flag = n
            for url in urls:
                if (flag % 2 == 0):
                    flag += 1
                    continue
                print str(n)+'\n'+str(num)+'\n'
                print url+'\n'

                result1,response_url = self.htmlurls.getcontent(url,n)
                with open('/home/qin/pachong/zy/www.tnp.sg.html/html/'+str(n)+'.html','w') as fff:
                    fff.write(result1)
                soup = BeautifulSoup(result1,"html.parser")
                with open('/home/qin/pachong/zy/www.tnp.sg.html/data/' + str(n) + '.json', 'a') as uuu:
                    source_id = '66'
                    language = 'eng'
                    request_url = url
                    uuu.write('source_id :' + source_id + '\n' + 'language :' + language + '\n' +'request_url :' + request_url + '\n' + 'response_url :' + response_url + '\n')
                    classification = soup.find('div', class_='story--web-category')
                    uuu.write('classification:'+classification.a.get_text() + '\n')
                    uuu.write('abstract:'+'\n')
                    title = soup.find('h1', class_='story-headline')
                    uuu.write('title:'+title.get_text().encode('utf-8','ignore') + '\n')
                    bodys = soup.find_all('p')
                    uuu.write('body:'+'\n')
                    for body in bodys:
                        uuu.write(body.get_text().encode('utf-8','ignore') + '\n')
                    uuu.write('\n')
                    pub_time = soup.find('div',class_='story--published-date field field-name-post-date field-type-ds field-label-hidden')
                    pub_times = re.search('([A-Za-z]+) ([0-9]+), ([0-9]+) ([0-9]+):([0-9]+)', pub_time.get_text())
                    uuu.write('pub_time:' + pub_times.group(3).encode('utf-8','ignore') + '-' + pub_times.group(1).encode('utf-8','ignore') + '-' + pub_times.group(2).encode('utf-8','ignore') + ' ' + pub_times.group(4).encode('utf-8','ignore') + ':' + pub_times.group(5).encode('utf-8','ignore') + ':00'+'\n')
                    cole_time = time.time()
                    uuu.write('cole_time:'+str(cole_time)+'\n')
                #     # images = re.findall(' src="(.*?)"', result1, re.S)
                    out_first_links = soup.find_all('a', href=re.compile('/.+'))
                    for out_first_link in out_first_links:
                        new_full_url = urlparse.urljoin(page_url,out_first_link['href'])
                        uuu.write(new_full_url.encode('utf-8','ignore') + '\n')
                    out_links = soup.find_all('a', href=re.compile('h.+'))
                    for out_link in out_links:
                        uuu.write(out_link['href'].encode('utf-8','ignore') + '\n')
                    images = soup.find_all('img')
                    for image in images:
                        uuu.write(image['src'].encode('utf-8','ignore') + '\n')
                flag+=1
                n+=1
            num+=1
        return n
    def pachong_news(self,nn,numm,page,zhengze):
        page_url = 'http://www.tnp.sg'
        n = nn
        num = numm
        while num<page:
            params_news = {
                'view_name': 'articles',
                'view_display_id': 'story_card_by_url_term_infinite',
                'view_args': '17',
                'view_path': 'taxonomy/term/17',
                'view_path': '',
                'view_dom_id': '11a4e75085275d2af23b8611c6cc64b0',
                'pager_element': '0',
                'views_exclude_previous': 'views_exclude_previous_QGCo0aCj-jZQc63n2XFZXfSYX4WdqcrxqVoEvLxmm6g',
                'page': num
            }
            result,result_url = self.htmlurls.geturls(params_news,num,n)
            urls = re.findall(zhengze , result, re.S)
            flag = n
            for url in urls:
                if (flag % 2 == 0):
                    flag += 1
                    continue
                print str(n)+'\n'+str(num)+'\n'
                print url+'\n'
                result1,response_url = self.htmlurls.getcontent(url,n)
                with open('/home/qin/pachong/zy/www.tnp.sg.html/html/'+str(n)+'.html','w') as fff:
                    fff.write(result1)
                soup = BeautifulSoup(result1,"html.parser")
                with open('/home/qin/pachong/zy/www.tnp.sg.html/data/' + str(n) + '.json', 'a') as uuu:
                    source_id = '66'
                    language = 'eng'
                    request_url = url
                    uuu.write('source_id :' + source_id + '\n' + 'language :' + language + '\n' +'request_url :' + request_url + '\n' + 'response_url :' + response_url + '\n')
                    classification = soup.find('div', class_='story--web-category')
                    uuu.write('classification:'+classification.a.get_text() + '\n')
                    uuu.write('abstract:'+'\n')
                    title = soup.find('h1', class_='story-headline')
                    uuu.write('title:'+title.get_text().encode('utf-8','ignore') + '\n')
                    bodys = soup.find_all('p')
                    uuu.write('body:'+'\n')
                    for body in bodys:
                        uuu.write(body.get_text().encode('utf-8','ignore') + '\n')
                    uuu.write('\n')
                    pub_time = soup.find('div',class_='story--published-date field field-name-post-date field-type-ds field-label-hidden')
                    pub_times = re.search('([A-Za-z]+) ([0-9]+), ([0-9]+) ([0-9]+):([0-9]+)', pub_time.get_text())
                    uuu.write('pub_time:' + pub_times.group(3).encode('utf-8','ignore') + '-' + pub_times.group(1).encode('utf-8','ignore') + '-' + pub_times.group(2).encode('utf-8','ignore') + ' ' + pub_times.group(4).encode('utf-8','ignore') + ':' + pub_times.group(5).encode('utf-8','ignore') + ':00'+'\n')
                    cole_time = time.time()
                    uuu.write('cole_time:'+str(cole_time)+'\n')
                #     # images = re.findall(' src="(.*?)"', result1, re.S)
                    out_first_links = soup.find_all('a', href=re.compile('/.+'))
                    for out_first_link in out_first_links:
                        new_full_url = urlparse.urljoin(page_url,out_first_link['href'])
                        uuu.write(new_full_url.encode('utf-8','ignore') + '\n')
                    out_links = soup.find_all('a', href=re.compile('h.+'))
                    for out_link in out_links:
                        uuu.write(out_link['href'].encode('utf-8','ignore') + '\n')
                    images = soup.find_all('img')
                    for image in images:
                        uuu.write(image['src'].encode('utf-8','ignore') + '\n')
                flag += 1
                n+=1
            num+=1
        return n
    def pachong_entertainments(self,nn,numm,page,zhengze):
        page_url = 'http://www.tnp.sg'
        n = nn
        num = numm
        while num<page:
            params_entertainments = {
                'view_name': 'articles',
                'view_display_id': 'story_card_by_url_term_infinite',
                'view_args': '7',
                'view_path': 'taxonomy/term/7',
                'view_path': '',
                'view_dom_id': 'bb26ba29cc894ac4efd41f84ccf26d40',
                'pager_element': '0',
                'views_exclude_previous': 'views_exclude_previous_9gKzDh5j4G7Xk0175Vz-KzQIZmcxTFkuAWJY6Jlk3d0',
                'page': num
            }
            result,result_url = self.htmlurls.geturls(params_entertainments,num,n)
            urls = re.findall(zhengze , result, re.S)
            flag = n
            for url in urls:
                if (flag % 2 == 0):
                    flag += 1
                    continue
                print str(n)+'\n'+str(num)+'\n'
                print url+'\n'
                result1,response_url = self.htmlurls.getcontent(url,n)
                with open('/home/qin/pachong/zy/www.tnp.sg.html/html/'+str(n)+'.html','w') as fff:
                    fff.write(result1)
                soup = BeautifulSoup(result1,"html.parser")
                with open('/home/qin/pachong/zy/www.tnp.sg.html/data/' + str(n) + '.json', 'a') as uuu:
                    source_id = '66'
                    language = 'eng'
                    request_url = url
                    uuu.write('source_id :' + source_id + '\n' + 'language :' + language + '\n' +'request_url :' + request_url + '\n' + 'response_url :' + response_url + '\n')
                    classification = soup.find('div', class_='story--web-category')
                    uuu.write('classification:'+classification.a.get_text() + '\n')
                    uuu.write('abstract:'+'\n')
                    title = soup.find('h1', class_='story-headline')
                    uuu.write('title:'+title.get_text().encode('utf-8','ignore') + '\n')
                    bodys = soup.find_all('p')
                    uuu.write('body:'+'\n')
                    for body in bodys:
                        uuu.write(body.get_text().encode('utf-8','ignore') + '\n')
                    uuu.write('\n')
                    pub_time = soup.find('div',class_='story--published-date field field-name-post-date field-type-ds field-label-hidden')
                    pub_times = re.search('([A-Za-z]+) ([0-9]+), ([0-9]+) ([0-9]+):([0-9]+)', pub_time.get_text())
                    uuu.write('pub_time:' + pub_times.group(3).encode('utf-8','ignore') + '-' + pub_times.group(1).encode('utf-8','ignore') + '-' + pub_times.group(2).encode('utf-8','ignore') + ' ' + pub_times.group(4).encode('utf-8','ignore') + ':' + pub_times.group(5).encode('utf-8','ignore') + ':00'+'\n')
                    cole_time = time.time()
                    uuu.write('cole_time:'+str(cole_time)+'\n')
                #     # images = re.findall(' src="(.*?)"', result1, re.S)
                    out_first_links = soup.find_all('a', href=re.compile('/.+'))
                    for out_first_link in out_first_links:
                        new_full_url = urlparse.urljoin(page_url,out_first_link['href'])
                        uuu.write(new_full_url.encode('utf-8','ignore') + '\n')
                    out_links = soup.find_all('a', href=re.compile('h.+'))
                    for out_link in out_links:
                        uuu.write(out_link['href'].encode('utf-8','ignore') + '\n')
                    images = soup.find_all('img')
                    for image in images:
                        uuu.write(image['src'].encode('utf-8','ignore') + '\n')
                flag += 1
                n+=1
            num+=1
        return n
    def pachong_lifestyles(self,nn,numm,page,zhengze):
        page_url = 'http://www.tnp.sg'
        n = nn
        num = numm
        while num<page:
            params_lifestyles = {
                'view_name': 'articles',
                'view_display_id': 'story_card_by_url_term_infinite',
                'view_args': '3',
                'view_path': 'taxonomy/term/3',
                'view_path': '',
                'view_dom_id': '53ce46cf37f702cdce9cd49dcdc16eab',
                'pager_element': '0',
                'views_exclude_previous': 'views_exclude_previous_j-x-ijpg4RI-v1DnSbaiC3yu50PKo1qcK75zyLINUdc',
                'page': num
            }
            result,result_url = self.htmlurls.geturls(params_lifestyles,num,n)
            urls = re.findall(zhengze , result, re.S)
            flag = n
            for url in urls:
                if (flag % 2 == 0):
                    flag += 1
                    continue
                print str(n)+'\n'+str(num)+'\n'
                print url+'\n'
                result1,response_url = self.htmlurls.getcontent(url,n)
                with open('/home/qin/pachong/zy/www.tnp.sg.html/html/'+str(n)+'.html','w') as fff:
                    fff.write(result1)
                soup = BeautifulSoup(result1,"html.parser")
                with open('/home/qin/pachong/zy/www.tnp.sg.html/data/' + str(n) + '.json', 'a') as uuu:
                    source_id = '66'
                    language = 'eng'
                    request_url = url
                    uuu.write('source_id :' + source_id + '\n' + 'language :' + language + '\n' +'request_url :' + request_url + '\n' + 'response_url :' + response_url + '\n')
                    classification = soup.find('div', class_='story--web-category')
                    uuu.write('classification:'+classification.a.get_text() + '\n')
                    uuu.write('abstract:'+'\n')
                    title = soup.find('h1', class_='story-headline')
                    uuu.write('title:'+title.get_text().encode('utf-8','ignore') + '\n')
                    bodys = soup.find_all('p')
                    uuu.write('body:'+'\n')
                    for body in bodys:
                        uuu.write(body.get_text().encode('utf-8','ignore') + '\n')
                    uuu.write('\n')
                    pub_time = soup.find('div',class_='story--published-date field field-name-post-date field-type-ds field-label-hidden')
                    pub_times = re.search('([A-Za-z]+) ([0-9]+), ([0-9]+) ([0-9]+):([0-9]+)', pub_time.get_text())
                    uuu.write('pub_time:' + pub_times.group(3).encode('utf-8','ignore') + '-' + pub_times.group(1).encode('utf-8','ignore') + '-' + pub_times.group(2).encode('utf-8','ignore') + ' ' + pub_times.group(4).encode('utf-8','ignore') + ':' + pub_times.group(5).encode('utf-8','ignore') + ':00'+'\n')
                    cole_time = time.time()
                    uuu.write('cole_time:'+str(cole_time)+'\n')
                #     # images = re.findall(' src="(.*?)"', result1, re.S)
                    out_first_links = soup.find_all('a', href=re.compile('/.+'))
                    for out_first_link in out_first_links:
                        new_full_url = urlparse.urljoin(page_url,out_first_link['href'])
                        uuu.write(new_full_url.encode('utf-8','ignore') + '\n')
                    out_links = soup.find_all('a', href=re.compile('h.+'))
                    for out_link in out_links:
                        uuu.write(out_link['href'].encode('utf-8','ignore') + '\n')
                    images = soup.find_all('img')
                    for image in images:
                        uuu.write(image['src'].encode('utf-8','ignore') + '\n')
                flag += 1
                n+=1
            num+=1
        return n
    def pachong_racings(self,nn,numm,page,zhengze):
        page_url = 'http://www.tnp.sg'
        n = nn
        num = numm
        while num<page:
            params_racings = {
                'view_name': 'articles',
                'view_display_id': 'story_card_by_url_term_infinite',
                'view_args': '39',
                'view_path': 'taxonomy/term/39',
                'view_path': '',
                'view_dom_id': '1640665f47b4c81928fa60b1b176d5c6',
                'pager_element': '0',
                'views_exclude_previous': 'views_exclude_previous_0jAqptA_SGt6LvNfbTvx9S3IyrZAbqlmGPtfQWTJ0iY',
                'page': num
            }
            result,result_url = self.htmlurls.geturls(params_racings,num,n)
            urls = re.findall(zhengze , result, re.S)
            flag = n
            for url in urls:
                if (flag % 2 == 0):
                    flag += 1
                    continue
                print str(n)+'\n'+str(num)+'\n'
                print url+'\n'
                result1,response_url = self.htmlurls.getcontent(url,n)
                with open('/home/qin/pachong/zy/www.tnp.sg.html/html/'+str(n)+'.html','w') as fff:
                    fff.write(result1)
                soup = BeautifulSoup(result1,"html.parser")
                with open('/home/qin/pachong/zy/www.tnp.sg.html/data/' + str(n) + '.json', 'a') as uuu:
                    source_id = '66'
                    language = 'eng'
                    request_url = url
                    uuu.write('source_id :' + source_id + '\n' + 'language :' + language + '\n' +'request_url :' + request_url + '\n' + 'response_url :' + response_url + '\n')
                    classification = soup.find('div', class_='story--web-category')
                    uuu.write('classification:'+classification.a.get_text() + '\n')
                    uuu.write('abstract:'+'\n')
                    title = soup.find('h1', class_='story-headline')
                    uuu.write('title:'+title.get_text().encode('utf-8','ignore') + '\n')
                    bodys = soup.find_all('p')
                    uuu.write('body:'+'\n')
                    for body in bodys:
                        uuu.write(body.get_text().encode('utf-8','ignore') + '\n')
                    uuu.write('\n')
                    pub_time = soup.find('div',class_='story--published-date field field-name-post-date field-type-ds field-label-hidden')
                    pub_times = re.search('([A-Za-z]+) ([0-9]+), ([0-9]+) ([0-9]+):([0-9]+)', pub_time.get_text())
                    uuu.write('pub_time:' + pub_times.group(3).encode('utf-8','ignore') + '-' + pub_times.group(1).encode('utf-8','ignore') + '-' + pub_times.group(2).encode('utf-8','ignore') + ' ' + pub_times.group(4).encode('utf-8','ignore') + ':' + pub_times.group(5).encode('utf-8','ignore') + ':00'+'\n')
                    cole_time = time.time()
                    uuu.write('cole_time:'+str(cole_time)+'\n')
                #     # images = re.findall(' src="(.*?)"', result1, re.S)
                    out_first_links = soup.find_all('a', href=re.compile('/.+'))
                    for out_first_link in out_first_links:
                        new_full_url = urlparse.urljoin(page_url,out_first_link['href'])
                        uuu.write(new_full_url.encode('utf-8','ignore') + '\n')
                    out_links = soup.find_all('a', href=re.compile('h.+'))
                    for out_link in out_links:
                        uuu.write(out_link['href'].encode('utf-8','ignore') + '\n')
                    images = soup.find_all('img')
                    for image in images:
                        uuu.write(image['src'].encode('utf-8','ignore') + '\n')
                flag+=1
                n+=1
            num+=1
        return n





lala = mainmethod()
# lala.pachong_sports(635,65,98,'(http:././www.tnp.sg./sports./.*?/.*?).u0022')
rrr = lala.pachong_news(963,1,146,'(http:././www.tnp.sg./news./.*?/.*?).u0022')
rrr = lala.pachong_entertainments(rrr,1,18,'(http:././www.tnp.sg./entertainment./.*?/.*?).u0022')
rrr = lala.pachong_lifestyles(rrr,1,31,'(http:././www.tnp.sg./lifestyle./.*?/.*?).u0022')
rrr = lala.pachong_racings(rrr,1,19,'(http:././www.tnp.sg./sports./racing./.*?).u0022')
