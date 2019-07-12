import requests
import sys
reload(sys)
from bs4 import BeautifulSoup
sys.setdefaultencoding('utf-8')
import json
def get_movies():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 FireFox/3.5.6',}


link = "http://www.santostang.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 FireFox/3.5.6'}
r1 = requests.get(link)
print("coding:", r1.encoding)
print("status code:", r1.status_code)
#print("text:", r1.text)
r = requests.get(link, headers = headers)

soup = BeautifulSoup(r.text, "lxml")
title = soup.find("h1", class_="post-title").a.text.strip()
print(title)
with open('title.txt', "a+") as f:
    f.write(title)
    f.close()
#print(r.text)
key_dict = {'key1': 'value1', 'key2': 'value2'}
r2 = requests.get('http://httpbin.org/get', params=key_dict)
print ("URL code:", r2.url)
print ("url text:", r2.text)

json_data = {"jsonrpc":"2.0","id":"0","method":"on_get_block_hash","params":[1885096]}

headers= {'Content-Type': "application/json"}
r11 = requests.post("http://192.168.0.40:18081/json_rpc",json=json_data, headers = headers)
print(r11.text)
