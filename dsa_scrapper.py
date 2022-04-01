import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

                                                                        
#lists of stocks user wants to get data of
stock_list=['AMD', 'DIDI', 'BABA', 'AMC', 'AAPL', 'NIO', 'F', 'PDD', 'NVDA', 'SOFI', 'ITUB', 'PLAN', 'BAC', 'PLTR', 'TME', 'CCL', 'EDU', 'BEKE', 'IQ', 'AAL', 'OXY', 'TSLA', 'VALE', 'BBD', 'AMZN', 'CSCO', 'FB', 'VZ', 'WFC', 'SQ', 'INTC', 'MRO', 'LCID', 'MSFT', 'PFE', 'OPEN', 'NOK', 'BILI', 'SNAP', 'NLY', 'UPST', 'RBLX', 'DKNG', 'XOM', 'PBR', 'DNA', 'UBER', 'C', 'FCEL', 'PCG']

#list of data of stocks
stock_data=[]



print(stock_list)


#webscrapper function also meme reference ;)
def getData(stonks):
     url=f'https://finance.yahoo.com/quote/{stonks}'#yahoo finance url
     r = requests.get(url)
     soup = BeautifulSoup(r.text,'html.parser')

     #the mainn info div is of class 'D(ib) Mend(20px)'
     #the price,change and percentage are under its fin streamer
     stock = {
     'stock_name' : soup.find('div', {'class': 'Mt(15px) D(f) Jc(sb)'}).find('h1').text,#hehe stonks ;)
     'price' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text, 
     'change' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
     'change_percentage' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text,
     'market_status' : soup.find('div',{'class': 'C($tertiaryColor) D(b) Fz(12px) Fw(n) Mstart(0)--mobpsm Mt(6px)--mobpsm Whs(n)'}).find('span').text,
     'opening_time' : soup.find('div',{'class' : 'D(ib) Fl(end) Pb(6px) Fz(xs) Fw(b) fin-update-style'}).find('span').text
     }
     return stock

#inserting scrapped data in the list
for item in stock_list:
    stock_data.append(getData(item))
    print('GETTING:',item)

print(stock_data)
