import urllib
from bs4 import BeautifulSoup as bs
import re

page = urllib.request.urlopen("http://mnregaweb4.nic.in/netnrega/MISreport4.aspx?fin_year=2013-2014&rpt=RP")
soup = bs(page,'html.parser') 

down = []
for a in soup.find_all('a'):                                            
    down.append(a.get('href')) 
#print(down)
alllinks = []
for link in down:                                            
    if not re.match('^java',link):
        if not re.match(r'^http',link):
            alllinks.append('http://mnregaweb4.nic.in/netnrega/'+link)
        else:
            alllinks.append(link)
alllinks = alllinks[1:]
for link in alllinks:
    print(link)
