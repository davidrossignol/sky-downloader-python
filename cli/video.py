'''
 Created on Tue Dec 17 2019

 Author:  2019 David Rossignol
'''

from __future__ import unicode_literals
import json

import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


# Main class that will manage what can be done to a video
class Video:
  def __init__(self, title, url):
    self.title = title
    self.url = url
    self.length = 0
    self.author = ''
    self.ydl_opts = {
    'format': 'bestaudio/best',
    'download_archive': 'downloaded_songs.txt',
    'outtmpl': 'C:/Users/Panda/Music/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
  }
    
  def downloadVideo(self):
    with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
      ydl.download(['https://www.youtube.com' + self.url])


    # Returns the url to the video's thumbnail
  def getVideoThumbnail(self):
    pass

    # Returns the author of the video as a string
  def getVideoAuthor(self):
    pass

  # Return the video length in seconds as an integer
  def getVideoLength(self):
    pass

  # Add the video to a 'Already downloaded' file to not download duplicates.
  def addVideoToDownloadedList(self):
    vid = {'video': {
      'title': self.title,
      #'length': self.getVideoLength(),
      #'author': self.getVideoAuthor,
      'url': self.url
    }}

    print(json.dumps(vid, indent=4, seperators=(". ", " = ")))


  # Returns a boolean weither that video has already been downloaded in the past or no. Does not check for audio.
  def checkIfDownloaded(self):
    return False


"""

Example dict

vids = {'videos':
        {
        'title': title, 'length': length, 'author': author, 'url': url
        }
      }


"""
