from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import lxml
import time
import sqlite3

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

def main():
    page = 0
    while True:
        page +=1
        url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273'
        # print(url)

        if page ==40:
            time.sleep(2)
            break

        r = requests.get(url, headers=headers)
        # print(r.text)

        s = BeautifulSoup(r.text, 'lxml')
        # print(s)


        link = s.find_all('div', class_='container-results large-images')

        urls = s.find_all('div', class_='image')
        print(urls)
        prices = s.find_all('div', class_='price')
        print(prices)



        def insert_db(prices, urls):
            connection = sqlite3.connect('newdata_db.sqlite')
            cursor = connection.cursor()
            cursor.execute("""
            INSERT INTO info (prices, urls)
            VALUE (?, ?)
            """, (urls, prices))
            connection.commit()






if __name__ == '__main__':
    main()