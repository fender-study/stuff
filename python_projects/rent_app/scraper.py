from bs4 import BeautifulSoup
import requests
import os

LINK = os.environ["olx"]


class Scrape:

    def __init__(self):
        self.response = requests.get(LINK)
        self.response.raise_for_status()
        self.web_content = self.response.content
        self.soup = BeautifulSoup(self.web_content, 'html.parser')

    def combined_list(self):
        addr_list = self.soup.find_all('h6')
        price_list = self.soup.find_all('p', attrs={'data-testid': 'ad-price', 'class': 'css-10b0gli er34gjf0'})
        link_list = self.soup.find_all('a', attrs={'class': 'css-rc5s2u'})

        prefix = "https://olx.ua"
        olx_list = []
        for item in link_list:
            olx_list.append(prefix + item.get('href'))

        combined_list = []
        for i in range(len(addr_list)):
            combined_list.append((addr_list[i].text, price_list[i].text, olx_list[i]))

        return combined_list

    def print_data(self):
        print(self.soup)
