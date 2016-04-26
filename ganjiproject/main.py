from multiprocessing import Pool
from geturl import get_url,get_info,urls,info
from get_start_url import start_url
db_url= [item['url'] for item in urls.find()]
index_url = [item['url'] for item in info.find()]
x = set(db_url)
y = set(index_url)
rest_of_url = x-y
# def get_all_link(start_url):
#     for i in range(1,100):
#         get_url(start_url,i)
# if __name__ == '__main__':
#     pool = Pool()
#     print(start_url)
#     pool.map(get_all_link,start_url.split())
if __name__ == '__main__':
    pool = Pool()
    pool.map(get_info,x)
    print('Done')
