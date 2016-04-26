from bs4 import BeautifulSoup
import requests,pymongo,random,lxml,time,urllib

client = pymongo.MongoClient('localhost',27017)
ganji = client['ganji']
urls = ganji['urls']
info = ganji ['info']
proxy_list = [
    'http://1.193.75.202:80',
    'http://182.90.10.40:80',
    'http://219.82.166.113:80'
]
proxy_ip = random.choice(proxy_list)
proxies = {'http' : proxy_ip}

headers = [
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}
]
def get_url(start_url,pages):
    url = '{}/o{}/'.format(start_url,str(pages))
    time.sleep(2)
    wb_data = requests.get(url , headers = random.choice(headers))
    soup = BeautifulSoup(wb_data.text , 'lxml')
    if soup.find('ul', 'pageLink'):
        links = soup.select('#wrapper > div.leftBox > div.layoutlist > dl > dd.feature > div > ul > li > a')
        for i in links:
            link = i.get('href')
            urls.insert_one({'url':link})
            print(link)
    else:
        print('ok')
        pass
# get_url('http://bj.ganji.com/jiaju/',1)
def get_info(url):
    time.sleep(2)
    wb_data = requests.get(url,headers = random.choice(headers))
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find_all('div','det-laybox'):
        # try:
            data = {
                'title': soup.title.text.strip().replace(u'\xa0', ''),
                'price': soup.select('.f22.fc-orange.f-type')[0].text.strip().replace(u'\xa0', '') if soup.find_all('i','f22 fc-orange f-type') else 'None',
                'pub_date': soup.select('.pr-5')[0].text.strip().split(' ')[0].replace(u'\xa0', '') if soup.find_all('i','pr-5') else 'None',
                'area': list(map(lambda x: x.text, soup.select('ul.det-infor > li:nth-of-type(3) > a'))),
                'cates': list(soup.select('ul.det-infor > li:nth-of-type(1) > span')[0].stripped_strings),
                'url': url
            }
            info.insert_one(data)
            print(data)
            # except requests.exceptions.RequestException:
            #     pass
        # except(IndexError):
        #     print(print(url))
        #     pass
        #     # except(AttributeError):
        #     #     pass
        # except:
        #     print(url)
        #     pass
    else:
        print('404页面' + url)
        urls.remove({'url': url})
        pass
get_info('http://bj.ganji.com/bangong/1423888916x.htm')
# urls.remove({"url":'/jiaju/2054315854x.htm'})