#!/opt/homebrew/bin/python3

from bs4 import BeautifulSoup
import requests
import sys
import shutil

imageName = sys.argv[1]
baseURL = 'https://www.google.com/search?tbm=isch&q='

def request(url):
   request = requests.get(url)
   if request.status_code == 200:
      return request.text
   else:
      return None

def parseHtml(html):
   return BeautifulSoup(html, 'html.parser')

def getFirstImageSrc(soup):
   try:
      return soup.find_all('img')[1]['src']
   except:
      return None

def downloadImage(url, fileName):
   request = requests.get(url, stream = True)

   if request.status_code == 200:
      request.raw.decode_content = True
      with open(fileName,'wb') as f:
         shutil.copyfileobj(request.raw, f)

try:
   request = request(baseURL + imageName)
except requests.exceptions.RequestException as e:
   raise SystemExit(e)
if request != None:
   soup = parseHtml(request)
   if soup != None:
      imageSrc = getFirstImageSrc(soup)
      if imageSrc != None:
         downloadImage(imageSrc, sys.argv[2])
