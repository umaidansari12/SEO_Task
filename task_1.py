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
sheet_instance = sheet.get_worksheet(0)

# get all the records of the data
records_data = sheet_instance.get_all_records()

# view the data
# records_data[:2]

# convert the json to dataframe
records_df = pd.DataFrame.from_dict(records_data)

# view the top records
records_df.head()

keywords = ['reddit', 'quora', 'pinterest', 'forum', 'question', 'discussion', 'thread']

def search(query, d, page=0):
    x = requests.get(f"https://www.google.com/search?q={query}").text
    soup = BeautifulSoup(x, 'html.parser')
    divs = soup.find_all("div",{"class":["egMi0 kCrYT", "yuRUbf"]})
    try:
        nextpage = soup.find("a", attrs = {"aria-label":["Next page"]})["href"]
        pause = 2.0
        for i in divs:
            link = i.a["href"][7::]
    #         d.append(link)
            for keyword in keywords:
                if keyword in link:
                    d.append(link)
                    break
        if page == 0:
            return

        time.sleep(pause)
        search(nextpage[10::],d,page+1)
    except:
        return

import requests
from bs4 import BeautifulSoup

# to search
query = list(records_df['Search Query \n(Dummy Keywords for now)'])

cnt = []
for q in query:
    d = []
    search(q,d,0)
    cnt.append([len(d)])

print(cnt)
#     for i in d:
#         print(i)

sheet_instance.update('B2', cnt)

cnt

# from autoscraper import AutoScraper

# url = 'https://www.google.com/'

# try:
#     from googlesearch import search
# except ImportError:
#     print("No module named 'google' found")

# # to search
# query = list(records_df['Search Query \n(Dummy Keywords for now)'])
# ans = []


# for q in query:
#     count = 0
#     index = 0
#     for j in search(q, num=10, start=0, stop=10, pause=3):
#         print(j)
#         for i in keywords:
# #             print(i)
#             if i in j:
# #                 print(i)
#                 count+=1
#                 break
#     ans.append(count)
#     records_df['result'][i] = count
#     index+=1
# #     print(q)
#     print(count)
