'''
 Created on Tue Dec 17 2019

 Author:  2019 David Rossignol
'''
from video import Video
from bs4 import BeautifulSoup
import urllib.request

class Search:

    def __init__(self, type):
        self.query = ''
        self.type = type
        self.source = 'yt'
        self.url = ''
        self.results = []

    def initiateSearch(self):
        passedQuery = urllib.request.quote(self.query)
        self.url = "https://www.youtube.com/results?search_query=" + passedQuery
        res = urllib.request.urlopen(self.url)
        html = res.read()
        soup = BeautifulSoup(html, 'html.parser')

        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            self.results.append(vid)



    def initiateQuery(self):
        if self.type == 'video':
            self.query = input("Enter name of video: ")

            if self.source == 'yt':
                self.initiateSearch()


    
