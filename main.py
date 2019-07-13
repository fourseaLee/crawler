import requests
import sys
reload(sys)
from bs4 import BeautifulSoup
sys.setdefaultencoding('utf-8')
import json
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

def getComment():
    caps = webdriver.DesiredCapabilities().FIREFOX
    caps["marionette"] = False
    binary = FirefoxBinary(r'firefox')
    driver = webdriver.Firefox(firefox_binary = binary, capabilities = caps)
    driver.get("http://www.santostang.com/2017/03/02/hello-world/")

    for x in range(0, 10):
        for i in range(0, 2):
            try:
                load_more = driver.find_element_by_css_selector('div.tie-load-more')
                load_more.click();
            except:
                pass
            comments = drivers.find_elements_by_css_selector('div.bdy-inner')
        for eachcomment in comments:
            content = eachcomment.find_element_by_tag_name('p')
            print(content.text)
        try:
            next_page = driver.find_element_by_css_selector('span.z-next')
            next_page.click()
            time.sleep(5)
        except:
            break

def getProComment():
    caps = webdriver.DesiredCapabilities().FIREFOX
    caps["marionette"] = False
    binary = FirefoxBinary(r'fixefox')
    fp = webdriver.FirefoxProfile()
    fp.set_preference("permissions.default.stylesheet",2)
    driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, capabilities=caps)
    driver.get("http://www.santostang.com/2017/03/02/hello-world/")


def getRentalShenzhen()
    caps = webdriver.DesiredCapabilities().FIREFOX
    caps['marionette'] = False
    binary = FirefoxBinary(r'firefox')
    driver = webdriver.Firefox(firefox_binary = binary, capabilities = caps)
    driver.get("http://zh.airbnb.com/s/Shenzhen--China?page=1")
    rent_list = driver.find_elements_by_css_selector('span.text_5mbkop-o_O-size_micro_16wifzf-o_O-inline_g86r3e')
    for eachhouse in rent_list:
        comment = comment.text
        price = 



def getSelenium():
    driver = webdriver.Firefox()
    driver.get("https://www.dianping.com/search/category/7/10/p1")

def get_movies():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
            'Host':'movie.douban.com'}
    movie_list = []
    for i in range(0,10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers=headers, timeout = 10)
        print (str(i + 1), "reponse code:", r.status_code)
       # print (r.text);
        soup = BeautifulSoup(r.text, "lxml")
        div_list = soup.find_all('div', class_ = 'hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie.encode('utf-8'))
    return movie_list 


def getContent():
    link = "http://www.santostang.com/"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 FireFox/3.5.6'}
  
    r1 = requests.get(link)
    print("coding:", r1.encoding)
    print("status code:", r1.status_code)

def storageContent():
    link = "http://www.santostang.com/"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 FireFox/3.5.6'}
    
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

def customizationParams():
    key_dict = {'key1':'value1', 'key2':'value2'}
    r = requests.get('http://httpbin.org/get', params = key_dict, timeout=20)
    print("url code:", r.url)
    print("response body:", r.text)
    r1 = requests.get('http://httpbin.org/get', params = key_dict)
    print("post data:", r1.text)

def rpctest():
    json_data = {"jsonrpc":"2.0","id":"0","method":"on_get_block_hash","params":[1885096]}
    headers= {'Content-Type': "application/json"}
    r11 = requests.post("http://192.168.0.40:18081/json_rpc",json=json_data, headers = headers)
    print(r11.text)

def main():
    print("init main")
   # movies = get_movies()
   # for i in range(0, len(movies)):
   #     print(movies[i])
   # getSelenium()
    getComment()

if __name__ == "__main__":
    main()
