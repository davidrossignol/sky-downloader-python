'''
 Created on Thu Dec 19 2019

 Author:  2019 David Rossignol
'''
from __future__ import unicode_literals

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


class Audio:

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


  def downloadAudio(self):
    with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
      ydl.download(['https://www.youtube.com' + self.url])