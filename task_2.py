import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import time

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\Vahan\Desktop\SEO Task\seo-task-2-386bca8682c9.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('Keyword Qualifier For SEO')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(1)

# get all the records of the data
records_data = sheet_instance.get_all_records()

# view the data
records_data[:2]

# convert the json to dataframe
records_df = pd.DataFrame.from_dict(records_data)

# view the top records
records_df.head()

query = list(records_df['Search Query'])
# query = query[:30]
query


def search(query, d, f, cnt):
    x = requests.get(f"https://www.google.com{query}", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "referer": 'https://www.google.com/'}).text
    soup = BeautifulSoup(x, 'html.parser')

    if cnt == 0:
        if "did not match any documents" in soup.text:
            d.append(0)
            f.append(0)
            return
        s = soup.find(id="result-stats").text

        r = re.findall(r"(About)(.+)(result[s]?)", s)[0][1]
        f.append(r)
        cnt += 1

    pause = 2.0
    try:
        table = soup.find("table", attrs={"role": ["presentation"]})
        pages = table.find_all("td")
        lastpage = pages[-2]
        lpurl = lastpage.a["href"]
        time.sleep(pause)
        cnt += 1
        search(lpurl, d, f, cnt)
    except:
        if cnt == 1:
            d.append(f[0])
            return
        else:
            stats = soup.find(id="result-stats").text
            res = re.findall(r"Page (\d+) of (about )*(\d+) results", stats)[0][-1]
            d.append(res)
#             print(soup.prettify())

import requests
from bs4 import BeautifulSoup
import re

lp_cnt = []
fp_cnt = []

for q in query:
    d=[]
    f=[]
    print(q)
    qu=f"/search?q={q}"
#     print(qu)
    search(qu,d,f,0)
    lp_cnt.append([d[0]])
    fp_cnt.append([f[0]])

print(lp_cnt)

print(fp_cnt)

sheet_instance.update('C2', fp_cnt)

sheet_instance.update('D2', lp_cnt)