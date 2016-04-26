import urllib,requests,time
from bs4 import BeautifulSoup
import os
def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        print(path + ' 创建成功')
        os.makedirs(path)
    else:
        print(path + ' 目录已存在')
def get_start_url(pages):
    path = 'd://Pythontest/3/'
    url = 'http://pic.yesky.com/c/6_61091_{}.shtml'.format(str(pages))
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('body > div.wrap2 > div.content > div.lb_box > dl > dd > a')
    for items in titles:
            url2  = items.get('href')
            # print(url2)

            for i in range(1,51):
                if i!=1:
                    url3 = url2.split('.s')[0] + '_' + str(i) + '.s' + url2.split('.s')[1]
                else:
                    url3 = str(url2)
                print(url3)
                wb_data2 = requests.get(str(url3))
                wb_data2.encoding ='gb2312'
                soup2 = BeautifulSoup(wb_data2.text, 'lxml')
                if soup2.find_all('div','box_1'):
                    print(' first or the end ')
                    break
                else:
                    # print('1')
                    imgpath = soup2.select('#l_effect_img > div > a > img')[0].get('src')
                    title3 = soup2.select('#l_effect_img > div > a > img')[0].get('alt')
                    path2 = path + title3
                    mkdir(path2)
                    # print('path2='+path2)
                    # print('imgpath='+imgpath)
                    # print('path=' +path2 + '/'+imgpath[-10:])
                    urllib.request.urlretrieve(imgpath, path2+ '/' + imgpath[-10:])
for page in range(1,51):
    time.sleep(5)
    get_start_url(page)

