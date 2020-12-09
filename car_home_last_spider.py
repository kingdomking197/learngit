import requests
from bs4 import BeautifulSoup
import re
import json
import datetime


def get_content(url):
    print("--------")
    print("The ProStart.......")
    print('The time:', datetime.datetime.now())


if __name__ == '__main__':
    url = 'https://car.autohome.com.cn/config/series/3895-7717.html#pvareaid=102192'
    get_content(url)

