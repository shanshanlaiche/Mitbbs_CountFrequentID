"""
Count the most recent "RecentMonth" months first "TopN" most frequent post author
Stored in "MostRecentFrequentID.py"
Combine the current list with all previous list
Previous list was stored in "CountFrequentID_Output"
Input parameters are stored in "CountFrequentID_Input"
Now, it only works for Firefox browser!!!


Author: babyrabbit_che(wechat)
Packages used: 1. Selenium (pip install Selenium)
"""
from datetime import date
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
OutPutList = open('CountFrequentID_Output.py', 'r+')
HistoricalID = []
for line in OutPutList:
    HistoricalID.append(line)
HistoricalID = set(HistoricalID)    
OutPutList.close()
OutPutList = open('CountFrequentID_Output.py', 'w')

URL = "http://www.mitbbs.com/mitbbs_bbsbfind.php?board=" + Board  

if Browser == "Firefox":
    driver = webdriver.Firefox()
elif Browser == "Chrome":
    driver = webdriver.Chrome()
elif Browser == "Ie":
    driver = webdriver.Ie()
else:
    print ('Please choose a valid explorer')
    
if Today == "Yes":
    Year = (datetime.date.today()).year
    Month =(datetime.date.today()).month
    Day = (datetime.date.today()).day

RecentDays = (date(Year, Month, Day) - date(Year, Month - RecentMonth, Day)).days
driver.get(URL)
elem = driver.find_element_by_name("dt")
elem.send_keys(Keys.BACK_SPACE)
elem.send_keys(RecentDays)
elem.send_keys(Keys.RETURN)

# read in the author and the title of each article
author_initial = driver.find_elements_by_class_name("news1")


for i in range(int(len(author_initial)/2)):
    del author_initial[i+1] # clean the list, only the author name left

for i in range(len(author_initial)):
    author_initial[i] = author_initial[i].text # get the ID string 
    
ID = FindRecentFrequentID(author_initial, TopN)

for i in range(len(ID)):
    HistoricalID.add(ID[i])
    
OutPutIDList = []
for i in range(len(HistoricalID)):
    OutPutIDList.append(HistoricalID.pop())# random output
    
OutPutIDList.sort()
OutPutList.writelines(OutPutIDList)

OutPutList.close()
driver.close()
