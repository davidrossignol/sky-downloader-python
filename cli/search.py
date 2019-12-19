'''
 Created on Tue Dec 17 2019

 Author:  2019 David Rossignol
'''
from video import Video
from audio import Audio
from bs4 import BeautifulSoup
import urllib.request

class Search:
    def __init__(self, type):
        self.query = ''
        self.type = type
        self.source = 'yt'
        self.url = ''
        self.results = []

    def askUserChoice(self):
        answer = input("Which one would you like to download? (0) to Exit: \n")
        if int(answer) > 0 and int(answer) < 31:
            choice = int(answer) - 1
            if self.type == 'video':
                self.results[choice].downloadVideo()
            elif self.type == 'audio':
                self.results[choice].downloadAudio()
        elif answer == 0:
            pass
        else:
            self.showQueryResults()
            self.askUserChoice()


    def showQueryResults(self):
        counter = 0
        for vid in self.results:
            counter += 1
            print(str(counter) + '.' + vid.title)



    def initiateSearch(self):
        passedQuery = urllib.request.quote(self.query)
        self.url = "https://www.youtube.com/results?search_query=" + passedQuery
        res = urllib.request.urlopen(self.url)
        html = res.read()
        soup = BeautifulSoup(html, 'html.parser')

        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            if not vid['href'].startswith("https://googleads.g.doubleclick.net/"):
                video = Video(vid['title'], vid['href']) if (self.type == 'video') is True else Audio(vid['title'], vid['href'])
                self.results.append(video)

                '''
                title
                class
                data-sessionlink
                dir
                href
                rel
                '''


    def initiateQuery(self):
        if self.type == 'video':
            self.query = input("Enter name of video: ")
            if self.source == 'yt':
                self.initiateSearch()
        elif self.type == 'audio':
            self.query = input("Enter name of audio: ")
            if self.source == 'yt':
                self.initiateSearch()


    
