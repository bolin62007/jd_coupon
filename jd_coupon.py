# -*- coding: utf-8 -*-
import requests
import random

# 禁用InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_cookies():
    with open('cookies.txt','r') as f:
        Cookie = {}
        for line in f.read().split(';'):
            name, value = line.strip().split('=', 1)
            Cookie[name] = value
        return Cookie
    
def get_coupon(key):
    rand = str(random.random())[0:-1]
    s = requests.Session()
    url = 'https://a.jd.com/ajax/freeGetCoupon.html?key='+ key +'&r=' + rand
    headers = {
               'Host': 'a.jd.com',
               'Connection': 'keep-alive',
               'Accept': 'application/json, text/javascript, */*; q=0.01',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
               'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
               'Accept-Encoding':'gzip, deflate, sdch, br',
               'Referer':'https://a.jd.com/'
               }
    req = s.get(url, headers = headers, cookies = get_cookies(), verify=False)
    result = req.content
    return result

if __name__ == "__main__":
    coupon_key = 'e71a1312faf7dca9bc7f215ab25b29fc482d207b93c5f7b8c16bea1f4349f49d60cf3f433e6b2e6d1f2dad85d53ca965'
    result = get_coupon(coupon_key)
    print result

# {"value":999,"desc":"领取成功！感谢您的参与，祝您购物愉快~"}
# {"value":14,"desc":"您已经参加过此活动，别太贪心哟，下次再来~"}
# {}key出错
    
    
