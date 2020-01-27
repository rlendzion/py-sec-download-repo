# Check every hour if it's been at least a full day since the last download. If true - initiate download sequence. Repeat if the downloaded file is in fact the same file.
# Prerequisites: https://chromedriver.chromium.org/downloads

import time
import numpy as np
import glob
import datetime as dt
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

fun = ['Download in progress','Still waiting for the file','Not yet','Just a little more','We are almost there','Hmm...']
# start a loop
i = 0
while i < 10: # iterate as many times as you like
    dir = glob.glob('C:/Users/DOM/Downloads/*.zip') # define directory and select only those files with valid extensions, eg. *.zip
    f = max(dir, key=os.path.getmtime) # select the latest file based on mtime
    results = os.stat(f) # get stats
    mtime = os.stat_result(results).st_mtime # get mtime
    mt = dt.datetime.fromtimestamp(mtime)
    # print(mt) # check #1 for debugging
    now = dt.datetime.now()
    last_mtime = now-mt
    # print(last_mtime) # check #2 for debugging
    val_time = dt.timedelta(days=1)
    # i += 1 # use for debugging
    # print(val_time) # check #3 for debugging
    if last_mtime > val_time: # run if it's been at least 24hours since the .zip file was downloaded
        service = Service('C:/Users/DOM/Downloads/chromedriver.exe')
        service.start()
        driver = webdriver.Remote(service.service_url)
        driver.get('https://adviserinfo.sec.gov/IAPD/InvestmentAdviserData.aspx');
        driver.find_element_by_link_text("Investment Adviser Representatives Report").click()
        # Create a notification that would pop up when the download is complete
        f2 = f
        while f == f2: # loop until
            subdir = glob.glob('C:/Users/DOM/Downloads/*.zip') # refresh the list of all available .zip files
            f2 = max(subdir, key=os.path.getmtime).replace(' (1)','')  # select the latest file based on mtime
            print(np.random.choice(fun))
            if f != f2:
                print('Download finished successfully!')
                break
            time.sleep(10)
    if i == 1:
        break
    i += 1
    print('Nothing to download yet')
    time.sleep(3600) # wait an hour before next iteration
print('Process ended')