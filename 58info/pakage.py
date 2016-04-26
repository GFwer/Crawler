from bs4 import BeautifulSoup
import requests

first_url='http://hrb.58.com/sale.shtml'

def get_pakage(url):
    wb_data = requests.get(url)
    soup  = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('#ymenu-side > ul > li > ul > li > b > a')
    for item in links:
        # print(item)
        link = 'http://hrb.58.com/'+ item.get('href')
        # print(link)
get_pakage(first_url)

pakage = '''
    http://hrb.58.com//shouji/
    http://hrb.58.com//tongxunyw/
    http://hrb.58.com//danche/
    http://hrb.58.com//fzixingche/
    http://hrb.58.com//diandongche/
    http://hrb.58.com//sanlunche/
    http://hrb.58.com//peijianzhuangbei/
    http://hrb.58.com//diannao/
    http://hrb.58.com//bijiben/
    http://hrb.58.com//pbdn/
    http://hrb.58.com//diannaopeijian/
    http://hrb.58.com//zhoubianshebei/
    http://hrb.58.com//shuma/
    http://hrb.58.com//shumaxiangji/
    http://hrb.58.com//mpsanmpsi/
    http://hrb.58.com//youxiji/
    http://hrb.58.com//jiadian/
    http://hrb.58.com//dianshiji/
    http://hrb.58.com//ershoukongtiao/
    http://hrb.58.com//xiyiji/
    http://hrb.58.com//bingxiang/
    http://hrb.58.com//binggui/
    http://hrb.58.com//chuang/
    http://hrb.58.com//ershoujiaju/
    http://hrb.58.com//bangongshebei/
    http://hrb.58.com//diannaohaocai/
    http://hrb.58.com//bangongjiaju/
    http://hrb.58.com//ershoushebei/
    http://hrb.58.com//yingyou/
    http://hrb.58.com//yingeryongpin/
    http://hrb.58.com//muyingweiyang/
    http://hrb.58.com//muyingtongchuang/
    http://hrb.58.com//yunfuyongpin/
    http://hrb.58.com//fushi/
    http://hrb.58.com//nanzhuang/
    http://hrb.58.com//fsxiemao/
    http://hrb.58.com//xiangbao/
    http://hrb.58.com//meirong/
    http://hrb.58.com//yishu/
    http://hrb.58.com//shufahuihua/
    http://hrb.58.com//zhubaoshipin/
    http://hrb.58.com//yuqi/
    http://hrb.58.com//tushu/
    http://hrb.58.com//tushubook/
    http://hrb.58.com//wenti/
    http://hrb.58.com//yundongfushi/
    http://hrb.58.com//jianshenqixie/
    http://hrb.58.com//huju/
    http://hrb.58.com//qiulei/
    http://hrb.58.com//yueqi/
    http://hrb.58.com//tiaozao/
'''