#!/usr/bin/env python
# coding: utf-8

# # Question1 -  Use the yfinance to extract stock data

# In[ ]:


pip install yfinance


# In[ ]:


import yfinance as yf


# In[ ]:


tesla=yf.Ticker('TSLA')


# In[ ]:


start_date = '2022-01-01'
end_date = '2022-12-31'
tesla_data=tesla.history(start=start_date, end=end_date)


# In[ ]:


tesla_data.reset_index(inplace=True)
tesla_data.head()


# # Question2 - Extracting Tesla Revenue Data Using Webscraping 

# In[ ]:


import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/TSLA/financials?p=TSLA'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    financial_data_section = soup.find('div', class_='D(tbrg)')
    
    if financial_data_section:
        revenue_row = financial_data_section.find_all('div', class_='D(tbr)')[1]
        
        revenue_data = revenue_row.find_all('div', class_='D(tbc)')[-1].text
        

        revenue = float(revenue_data.replace(',', '').replace('M', '').replace('B', '').replace('T', ''))         
        print("Tesla's Total Revenue:", revenue)
    else:
        print("Financial data section not found on the webpage.")
else:
    print("Failed to retrieve data from the website.")


# # Question3 - Extracting GameStop Stock Data Using yfinance

# In[ ]:


gme_data = yf.download("GME", start='2022-01-01', end='2022-12-31')
gme_data.reset_index(inplace=True)
gme_data.head()


# # Question4 - Extracting GameStop Revenue Data Using Webscraping

# In[ ]:


url = 'https://finance.yahoo.com/quote/GME/financials?p=GME'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    revenue_section = soup.find('div', {'data-test': 'fin-row'})
    
    if revenue_section:
        revenue_data = revenue_section.find('div', {'data-test': 'fin-col'}).text
        
        revenue = revenue_data.replace(',', '')  
        revenue = float(revenue) 
        
        print("GameStop's Total Revenue:", revenue)
    else:
        print("Revenue data not found on the webpage.")
else:
    print("Failed to retrieve data from the website.")


# # Question5 - Tesla Stock and Revenue Dashboard

# 1. Tesla Stock
# 
# - Display a line chart illustrating Tesla's stock performance over a selected period, such as one year, with the date on the x-axis and the stock price on the y-axis
# - Include key events or milestones, such as product launches, earnings announcements, or major news, marked on the chart for reference
# - Add interactive features like tooltips that display the stock price and date when hovering over data points
# - Optionally, include additional visualizations like candlestick charts or moving averages to provide more insights into price trends and patterns
# 
# 2. Revenue Dashboard
# 
# - Present a bar or line chart depicting Tesla's quarterly or yearly revenue over a chosen timeframe
# - Include annotations or markers to highlight significant changes in revenue, such as spikes or dips, and provide context for these fluctuations
# - Incorporate a secondary axis to show any relevant factors that may influence revenue, such as vehicle deliveries, production capacity, or market share
# - Offer filtering options to allow users to view revenue breakdowns by geographical region, product category, or business segment, providing deeper insights into revenue sources and trends

# 

# # Question6 - GameStop Stock and Revenue Dashboard

# 1. GameStop Stock
#  - Similar to the Tesla dashboard, include a line chart showing GameStop's stock performance over a selected period, such as one year
#  - Highlight key events or milestones that may have influenced the stock price, such as earnings releases, short squeezes, or changes in company leadership
#  - Utilize interactive features like tooltips to display stock price and date information when hovering over data points
#  - Optionally, include additional visualizations like volume charts or relative strength index (RSI) indicators to provide further insights into trading activity and stock momentum
#  
# 2. Revenue Analysis
#  - Present a bar or line chart illustrating GameStop's quarterly or yearly revenue over a chosen timeframe
#  - Include annotations or markers to highlight significant changes in revenue, such as increases or decreases compared to previous periods
#  - Incorporate a secondary axis to display additional relevant metrics, such as same-store sales growth, digital sales, or average transaction value
#  - Offer filtering options to allow users to analyze revenue trends by product category, geographical region, or distribution channel, providing deeper insights into sales performance and market demand

# # Question7 - Sharing your Assignment Notebook

# In[ ]:




