import urllib.request
from bs4 import BeautifulSoup

# Method inspired by Jason Brooks on stack overflow.
# Link to answer: https://stackoverflow.com/questions/29069444/returning-the-urls-as-a-list-from-a-youtube-search-query
def askSearch():
  results = []
  
  query = input("Please enter the name of the video you would like to find: ")
  querypass = urllib.parse.quote(query)
  url = "https://www.youtube.com/results?search_query=" + querypass
  res = urllib.request.urlopen(url)
  html = res.read()
  soup = BeautifulSoup(html, 'html.parser')
  for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    results.append(vid)
    
def showResults(results):
  counter = 1
  for vid in results:
    print(str(counter) + ". " + vid)
  
  

def startProgram():
  askSearch()


