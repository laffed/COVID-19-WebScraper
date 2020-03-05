# webscraping tool

from selenium import webdriver
from datetime import date, timedelta
import requests
import bs4 as bs
import urllib.request
import pandas as pd

#driver = webdriver.Chrome()

today = date.today()
yesterday = today - timedelta(days=1)
todayFormatted = today.strftime("%m-%d-%Y")
yesterdayFormatted = yesterday.strftime("%m-%d-%Y")

r_today = requests.get(
    f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{todayFormatted}.csv")
if (r_today.status_code == 200):
    confirmedURL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{todayFormatted}.csv"
else:
    confirmedURL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{yesterdayFormatted}.csv"

# driver.get(confirmedURL)

sauce = urllib.request.urlopen(confirmedURL).read()

soup = bs.BeautifulSoup(sauce, "html.parser")
