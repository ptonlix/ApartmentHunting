#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import csv
import codecs


url = "http://sz.58.com/pinpaigongyu/pn/{page}/?minprice=1500_2000"

page = 0
#with open("rent.csv","wb") as datacsv:
#   datacsv.write(codecs.BOM_UTF8)
csv_file = open("rent1.csv","w")
csv_writer = csv.writer(csv_file, delimiter=',')
while True:
    page += 1
    print("fetch: ", url.format(page=page))
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text)
    house_list = html.select(".list > li")

    if not house_list:
        break
    """
    for house in house_list:
        house_title = house.select("h2")[0].string.encode("utf-8")
        house_url = urljoin(url, house.select("a")[0]["href"]).encode("utf-8")
        house_info_list = house_title.split()
        house_location = house_info_list[1]
        house_money = house.select(".money")[0].select("b")[0].string.encode("utf-8")

        # 查看house_title等的类型
        print(type(house_title), type(house_location), type(house_money), type(house_url))

        # 向csv文件写入数据
        with open('rent.csv', 'wb') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow([house_title, house_location, house_money, house_url])
    """
    for house in house_list:
        house_title = str(house.select("h2")[0].string, encoding="utf8")
        print(house_title)
        house_url = urljoin(url, house.select("a")[0]["href"])

        house_info_list = house_title.split()

        house_location = house_info_list[1]

        house_money = str(house.select(".money")[0].select("b")[0].string)
        print(house_url)
        # 把str类型的housetitle、house_location、house_money编码成bytes类型
        #house_title = house_title.encode("utf-8").decode()
        #house_location = house_location.encode("utf-8").decode()
        #house_money = house_money.encode("utf-8").decode()
        #house_url = house_url.encode("utf-8").decode()

        # 查看house_title等的类型
        print(type(house_title), type(house_location), type(house_money), type(house_url))

        csv_writer.writerow([house_title, house_location, house_money, house_url])

csv_file.close()