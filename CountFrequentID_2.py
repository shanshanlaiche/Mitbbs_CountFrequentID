"""
Count the most recent "RecentMonth" months first "TopN" most frequent post author
Stored in "MostRecentFrequentID.py"
Combine the current list with all previous list
Previous list was stored in "CountFrequentID_Output"
Input parameters are stored in "CountFrequentID_Input"


Author: babyrabbit_che(wechat)
Packages used: 1. BeautifulSoup (pip install BeautifulSoup);2. requests
"""
from datetime import date
import datetime
import re, sys
from bs4 import BeautifulSoup
import requests
from CountFrequentID_Input import *

# find the most TopN frequent post author from IDList
#if the total author count is less than TopN, return all the author's ID
def FindRecentFrequentID(IDList, TopN):
    IDCount = {} # a dictionary to use ID as key and the appearing time as value
    for i in range(len(IDList)):
        IDCount[IDList[i]] = 0 # set initial count to zero
    for i in range(len(IDList)):
        IDCount[IDList[i]] = IDCount[IDList[i]] + 1

    RecentFrequentID = []
    for i in range(min(TopN,len(IDCount))):
        RecentFrequentID.append(sorted(IDCount)[len(IDCount)-1-i] + '\n');
    return RecentFrequentID # a List of most TopN frequent post author

###### main project  ######################################
def CountFrequentyID (Board, Browser, TopN, Today, Year, Month, Day, RecentMonth):

    OutPutList = open('CountFrequentID_Output.py', 'r+')
    HistoricalID = []
    for line in OutPutList:
        HistoricalID.append(line)
    HistoricalID = set(HistoricalID)    
    OutPutList.close()
    OutPutList = open('CountFrequentID_Output.py', 'w')

    if Today == "Yes":
        Year = (datetime.date.today()).year
        Month =(datetime.date.today()).month
        Day = (datetime.date.today()).day

    RecentDays = (date(Year, Month, Day) - date(Year, Month - RecentMonth, Day)).days

    URL = "http://www.mitbbs.com/mitbbs_bbsbfind.php?board=" + Board  

    form_data = {'submit':"递交查询结果", 'dt' : str(RecentDays), 'year':str(Year),
                 'month':str(Month), 'day':str(Day)}
    session = requests.session()
    r = session.post(URL, data=form_data, verify = False)
    r.encoding = "gb2312"
    soup = BeautifulSoup(r.text)

    author_initial = [u.text for u in soup.findAll('a', class_='news1')]

    for i in range(int(len(author_initial)/2)):
          del author_initial[i+1] # clean the list, only the author name left

    ID = FindRecentFrequentID(author_initial, TopN)
    for i in range(len(ID)):
        HistoricalID.add(ID[i])
        
    OutPutIDList = []
    for i in range(len(HistoricalID)):
        OutPutIDList.append(HistoricalID.pop())# random output
        
    OutPutIDList.sort()
    OutPutList.writelines(OutPutIDList)

    OutPutList.close()

CountFrequentyID (Board, Browser, TopN, Today, Year, Month, Day, RecentMonth)
