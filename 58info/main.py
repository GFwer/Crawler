from multiprocessing import Pool
from spider import  get_url
from pakage import pakage

def get_all_links(pakage):
    for i in range(1,101):
        get_url(pakage,i)

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_all_links,pakage.split())