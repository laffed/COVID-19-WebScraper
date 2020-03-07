# index.py
# Werkzeug released 1.0 which breaks flask.
# pip3 install Werkzeug==0.16.0

# API imports
from flask import Flask
from flask_restplus import Resource, Api, fields
from werkzeug.utils import cached_property
from werkzeug.contrib.fixers import ProxyFix
# scraper imports
from selenium import webdriver
from datetime import date, timedelta
import requests
import csv
import json
import bs4 as bs
import urllib.request
import pandas as pd

# Scraper
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
soup_string = str(soup)


# test _________________
html = open("https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/03-05-2020.csv").read()

soup_2 = BeautifulSoup(html)

table_2 = soup_2.find("table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)

with open('output.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

print(output.csv)


# API
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app,
          version='0.1',
          title='COVID Data',
          description='Return CSV data updated daily via Johns Hopkins'
          )


@api.route('/covid')
class HelloWorld(Resource):
    def get(self):
        return output.csv


if __name__ == '__main__':
    app.run(debug=True)
