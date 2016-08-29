#!/usr/bin/python
# http://docs.python-requests.org/en/latest/user/quickstart/
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/

import csv
import re
import pafy
import sys
import requests
from sets import Set 
import time
from bs4 import BeautifulSoup



# scrapes the title 
def getTitle():
    d = soup.find_all("h1", "branded-page-header-title")
    for i in d:
        name = i.text.strip().replace('\n',' ').replace(',','').encode("utf-8")
        f.write(name+',')
        print('\t\t%s') % (name)

# scrapes the subscriber and view count
def getStats():
    b = soup.find_all("li", "about-stat ") # trailing space is required.
    for i in b:
        value = i.b.text.strip().replace(',','')
        name = i.b.next_sibling.strip().replace(',','')
        f.write(value+',')
        print('\t\t%s = %s') % (name, value)

# scrapes the description
def getDescription():
    c = soup.find_all("div", "about-description")
    for i in c:
        description = i.text.strip().replace('\n',' ').replace(',','').encode("utf-8")
        f.write(description+',')
        #print('\t\t%s') % (description)

# scrapes all the external links 
def getLinks():
    a = soup.find_all("a", "about-channel-link ") # trailing space is required.
    for i in a:
        url = i.get('href')
        f.write(url+',')
        print('\t\t%s') % (url)

# scrapes the related channels
def getRelated():
    s = soup.find_all("h3", "yt-lockup-title")
    for i in s:
        t = i.find_all(href=re.compile("user"))
        for i in t:
            url = 'https://www.youtube.com'+i.get('href')
            rCSV.write(url+'\n')
            print('\t\t%s,%s') % (i.text, url)  

reload(sys)  
sys.setdefaultencoding('utf8')
of = open("youtube-scrape-data.csv", "w")
ifile = open('namesi.csv', "rUb")
reader = csv.reader(ifile)
#reader = csv.reader(ifile)
visited = []
base = "https://www.youtube.com/results?search_query="
q = []
q = ['ALS ICE Bucket Tim Cook Apple','ALS ICE Bucket Zuckerberg Facebook']
page = "&page=1"
count = 1
pages = 1
pagesToScrape = 1
urls = Set()
for row in reader:
    query  = 'ALS ICE Bucket ' + row[0] + ' ' + row[1]
    #print query
    q.append(query)
#urlquery = 
for query in q:
    pages = 1
    while pages <= pagesToScrape:
        scrapeURL = base + str(query) + page 
        print scrapeURL
        r = requests.get(scrapeURL)
        soup = BeautifulSoup(r.text)
        count = 0
        for a in soup.find_all('a', href=True):
            video = "http://www.youtube.com"
           # print "Found the URL:", a['href']
            k=a['href'].find("watch")
            if (k == 1):
                url = video + a['href']
         #       print url
                urls.add(url)
                count += 1 
            if (count >= 2):
                break
#          
#        for each in users:
#            print each
#            a = each.find_all(href=re.compile("user"))
#            for i in a:
#                  print "----"+i
        #         url = 'https://www.youtube.com'+i.get('href')+'/about'
        #         if url in visited:
        #             print('\t%s has already been scraped\n\n') %(url)
        #         else:
        #             r = requests.get(url)
        #             soup = BeautifulSoup(r.text)
        #             f.write(url+',')
        #             print('\t%s') % (url)
        #             getTitle()
        #       #      getStats()
        #             getDescription()
        #        #     getLinks()
        # #            getRelated()
        #             f.write('\n')   
        #             print('\n')
        #             visited.append(qurl)
        #             time.sleep(3)
       
      #  time.sleep(1)
        # print('\n')
        pages = pages + 1
    # print('\n')
# print urls 

for videourl in set(urls):
    print videourl
    print "\n"
    video = pafy.new(videourl)
    of.write (video.title + "^" + video.description.replace("\n", ".") + "^" +  video.author + "^" + videourl + "^" + video.published )
    of.write("\n") 
    #+ "Published" + video.published
#                print "Title: " + video.title + " Description " + video.description + " Author " + video.author + "Published" + video.published

ifile.close()