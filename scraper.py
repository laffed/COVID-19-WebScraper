# webscraping tool

from selenium import webdriver
from datetime import date, timedelta
import requests
import csv
import json
import bs4 as bs
import urllib.request
import pandas as pd

# driver = webdriver.Chrome()

today = date.today()
todayFormatted = today.strftime("%m-%d-%Y")

daysToSubtract = 1
r_today = requests.get(
    f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{todayFormatted}.csv")

if(r_today.status_code != 200):
    while (r_today.status_code != 200):
        tryDate = today - timedelta(days=daysToSubtract)
        tryDateFormatted = tryDate.strftime("%m-%d-%Y")
        daysToSubtract += 1
        r_today = requests.get(
            f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{tryDateFormatted}.csv")

    confirmedURL = (
        f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{tryDateFormatted}.csv")
else:
    confirmedURL = (
        f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{todayFormatted}.csv")
# driver.get(confirmedURL)

sauce = urllib.request.urlopen(confirmedURL).read()

soup = bs.BeautifulSoup(sauce, "html.parser")
