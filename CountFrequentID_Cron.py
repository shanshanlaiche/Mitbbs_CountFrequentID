"""
Depends: cron (pip install cron.py)
use cron to run the "CountFrequentyID" hourly or daily
a time marker is printed everytime
"""
import  time
import cron
import datetime
from CountFrequentID import *
from datetime import datetime

frequency = 'hourly' # the running frequency of "CountFrequentID.py"

def PrintTime():
        print ("The job is done at:  ", str(datetime.now()))

if frequency == 'hourly':
        job = cron.Cron()
        job.add('0 */1 * * *', PrintTime)
        job.add('0 */1 * * *', CountFrequentyID, Board, Browser,
                   TopN, Today, Year, Month, Day, RecentMonth)
elif frequency == 'daily':
        job = cron.Cron()
        job.add('0 0 */1 * *', PrintTime)
        job.add('0 0 */1 * *', CountFrequentyID, Board, Browser,
                   TopN, Today, Year, Month, Day, RecentMonth)


job.start()

# if you want to stop the job,  type "job.stop()" in the command line
# and hit "Enter"
