import requests
from bs4 import BeautifulSoup
import re
import json
import datetime
from selenium import webdriver
from lxml import etree


def get_content(url):
    The_new_model_list = []
    driver = webdriver.Chrome('/Users/k-mac/Downloads/Compressed/chromedriver')
    driver.get(url)
    page_text = driver.page_source
    driver.close()
    soup = BeautifulSoup(page_text, 'html.parser')
    dom = etree.HTML(page_text)
    tags = soup.find('div', class_='path').find_all('a')[-1].get_text()
    print(tags)
    carbox = soup.find('div', id='config_nav').find_all('a', href=re.compile('//www.autohome.com.cn/spec/(\d+)/#pvareaid=(\d+)'))

    if carbox != []:
        print('carbox is not None')
        The_car_num = len(carbox)
        print('The car number:', The_car_num)
        for i in carbox:
            The_new_model = i.get_text()
            print('the new car model:', The_new_model)
            The_new_model_list.append(The_new_model)

        for i in range(1, int(The_car_num) + 1):
            price = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[1]/tbody[1]/tr[1]/td[{}]/div[1]/text()'.format(i))[0]
            energy_types = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[4]/td[{}]/div[1]/text()'.format(i))[0]
            #config:
            if energy_types == '汽油':
                environmental_standards = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[5]/td[{}]/div[1]/text()'.format(i))[0]
                time_to_market = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[6]/td[{}]/div[1]/text()'.format(i))[0]
                maximum_power = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[7]/td[{}]/div[1]/text()'.format(i))[0]
                engine_torque = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[8]/td[{}]/div[1]/text()'.format(i))[0]
                engine = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[9]/td[{}]/div[1]/text()'.format(i))[0]
                gearbox = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[10]/td[{}]/div[1]/text()'.format(i))[0]
                length_width_and_height = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[11]/td[{}]/div[1]/text()'.format(i))[0]
                body_structure = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[12]/td[{}]/div[1]/text()'.format(i))[0]
                top_speed = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[13]/td[{}]/div[1]/text()'.format(i))[0]
                g_km_acceleration = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[14]/td[{}]/div[1]/text()'.format(i))[0]
                s_km_acceleration = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[15]/td[{}]/div[1]/text()'.format(i))[0]
                zhidong = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[16]/td[{}]/div[1]/text()'.format(i))[0]
                comprehensive_fuel_consumption = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[17]/td[{}]/div[1]/text()'.format(i))[0]
                vehicle_warranty = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[2]/tbody[1]/tr[19]/td[{}]/div[1]/text()'.format(i))
                vehicle_warranty_text = []
                for x in vehicle_warranty:
                    vehicle_warranty_text.append(x)
                    if len(vehicle_warranty_text) == 1:
                        vehicle_warranty_text_xpath = vehicle_warranty_text[0]
                    elif len(vehicle_warranty_text) == 3:
                        vehicle_warranty_text_xpath = vehicle_warranty_text[0] + '年或' + vehicle_warranty_text[1] + '万' + vehicle_warranty_text[2]

                #body
                Wheelbase = dom.xpath('/html[1]/body[1]/div[4]/div[3]/table[3]/tbody[1]/tr[5]/td[{}]/div[1]/text()'.format(i))[0]
                print(i)
                print('the price:', price)
                print('energy types:', energy_types)
                print('the environmental standards:', environmental_standards)
                print('the time to market:', time_to_market)
                print('the maximum_power:',maximum_power)
                print('the engine_torque:',engine_torque)
                print('the engine:',engine)
                print('the gearbox:',gearbox)
                print('length_width_and_height:',length_width_and_height)
                print('body structure:',body_structure)
                print('top speed:',top_speed)
                print('g_km_acceleration:',g_km_acceleration)
                print('s_km_acceleration:',s_km_acceleration)
                print('zhidong:',zhidong)
                print('comprehensive_fuel_consumption:',comprehensive_fuel_consumption)
                print('vehicle_warranty_text:',vehicle_warranty_text_xpath)
                print('-------------')
                print('#body')
                print('Wheelbase:',Wheelbase)




if __name__ == '__main__':
    print("--------")
    print("The Process Start.......")
    Start = datetime.datetime.now()
    print('The Start time:', Start)
    url = 'https://car.autohome.com.cn/config/series/19-23.html#pvareaid=102192'
    get_content(url)
    print("--------")
    print("The Process Finished.......")
    Finished = datetime.datetime.now()
    print('The Finished time:', Finished)
    print('Time:', Finished - Start)







