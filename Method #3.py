import datetime
import webbrowser

now = datetime.date.today()
then = datetime.date(2020,1,24)
dd = (now-then).days
i = 43819+dd*3 #can easily break if ID changes one day - update as of 24/01/2020
url = 'https://adviserinfo.sec.gov/IAPD/Content/BulkFeed/CompilationDownload.aspx?FeedPK=' + str(i) + '&FeedType=IA_INDVL'
webbrowser.open(url)
print('Process ended')