from bs4 import  BeautifulSoup
import requests,time,pymongo

client = pymongo.MongoClient('localhost',27017)
test = client['58test']
quanbu = test['quanbu']
info = test['info']
def get_url(pakage,page,type=0):
    list_view = '{}/{}/pn{}'.format(pakage,str(type),str(page))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find_all('td'):
        for item in soup.select('td.t a.t'):
            link = item.get('href').split('?')[0]
            quanbu.insert_one({'url':link})
        print('Done~!')
    else:
        pass
# get_url('http://hrb.58.com//shouji/',2)
def get_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if '404' in soup.find('script',type='text/javascript').split('/'):
        pass
    else:
        data = {
            'title': (soup.title.text).split('-')[0].strip(),
            'price': soup.select('.price')[0].text if soup.find_all('span', 'price c_f50') else '暂无',
            'date': soup.select('.time')[0].text if soup.find_all('li', 'time') else '暂无',
            'area': list(soup.select('.c_25d')[-1].stripped_strings) if soup.find_all('span', 'c_25d') else '暂无',
        }
        info.insert_one(data)
        print('Done!~')
# get_info('http://hrb.58.com/shouji/25480244744655x.shtml')
