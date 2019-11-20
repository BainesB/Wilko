from bs4 import BeautifulSoup
import requests
import re 
from HeadingsToScrape import Titles
import time
import csv

page = requests.get('https://www.wilko.com')
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup.prettify())

links = soup.find_all('a')

pages = {}

for i in links:
    if i.text in Titles:
        #print(i.text, i['href'])
        pages[i.text]= i['href']
    else: 
        pass 

#print(pages)
print(len(pages))

for i in Titles: 
    #time.sleep(1)
    try:
        newpage = requests.get('https://www.wilko.com'+pages[i])
        print(pages[i])
        print(newpage)
        newsoup = BeautifulSoup(newpage.text, 'html.parser')
        prodnumb = newsoup.find_all('p')
        # Putting this stuff into a db is breaking it.  
        #DBName = 'wilko.db'
        #conn = sqlite3.connect(DBName)
        #cursor = conn.cursor()

        #for a in prodnumb:
         #   if 'Viewing' in a.text:
        line = a.text
        words = line.split(' ')
        totalprods =words[len(words)-2]
        URL = 'https://www.wilko.com'+pages[i]
        print('Title:',i,'|','Products:',totalprods,'|','URL', URL)
               # '''
                #try:
                 #   cursor.execute(f'''
                    #INSERT INTO PM (Title, Products, URL)
                    #VALUES('{i}', '{name}', {URL});
                        #''')
                   # conn.commit()

                #except:
                 #   print(f'''unable to enter value into database: {DBName}''')
                  #  pass
                   # '''
        #conn.close()

    except:
        print("D'oh")


