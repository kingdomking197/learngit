import requests
from bs4 import BeautifulSoup
import re
import datetime
from pandas.core.frame import DataFrame
from pymongo import MongoClient
import json


def get_content(url):
    parameter_list = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
    r = requests.get(url, headers=headers)
    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text, 'html.parser')

    # 品牌/车系/车型
    brand = soup.find('div', class_="breadnav").find_all('a', href=re.compile('/price/brand-(\d+).html'))[0].get_text()
    sub_brand = soup.find('div', class_="breadnav").find_all('a', href=re.compile('/price/brand-(\d+)-(\d+).html'))[
        0].get_text()
    series = soup.find('div', class_="breadnav").find_all('a', href=re.compile('/price/series-(\d+).html'))[
        0].get_text()

    print(brand)
    print(sub_brand)
    print(series)

    # 车型参数.指导价格
    parameter_element = soup.find('div', class_='main-lever-left').find_all('li')[:4]
    for i in parameter_element:
        parameter = i.get_text().split('：')[0]
        content = i.get_text().split('：')[1]
        parameter_list.append(parameter)
        parameter_list.append(content)
    print(parameter_list)
    # 指导价
    price = soup.find('div', class_='main-lever-right').find_all('span')[0].get_text()
    # parameter Url
    judage = soup.find('div', class_ = 'main-lever-link')

    print(judage)
    if judage == None:
        parameter_url = 'None'
    elif judage != None:
        parameter_url = 'https://car.autohome.com.cn' + soup.find('div', class_ = 'main-lever-link').find_all('a')[-1].get('href')
    print(parameter_url)


    print(parameter_url)
    data = parameter_list
    df = DataFrame(data)
    df = df.T
    df.rename(columns={0: 'parameter_1', 1: 'content_1', 2: 'parameter_2', 3: 'content_2',
                       4: 'parameter_3', 5: 'content_3', 6: 'parameter_4', 7: 'content_4', }, inplace=True)
    df['brand'] = brand
    df['sub_brand'] = sub_brand
    df['series'] = series
    df['price'] = price
    df['parameter_url'] = parameter_url
    print(df)
    client = MongoClient(host='localhost', port=27017)  # 连接mongodb端口
    db = client['car_data']
    crowd = db['car_autohome_parameter']
    crowd.insert_many(json.loads(df.T.to_json()).values())

def main():
    file = "/Users/k-mac/Documents/auto_carhome.txt"
    with open(file)as f:
        for line in f:
            url = line.split('\n')[0]
            get_content(url)

if __name__ == '__main__':
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    print('使用时间：',end-start)


