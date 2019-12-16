import json

# Main class that will manage what can be done to a video
class Video:
  def __init__(self, title, url):
    self.title = title
    self.url = url
    self.length = 0
    self.author = ''
    
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
        'length': self.getVideoLength(), 
        'author': self.getVideoAuthor, 
        'url': self.url 
      }}
      
      print(json.dumps(vid, indent=4, seperators=(". ", " = ")))
    
    
    # Returns a boolean weither that video has already been downloaded in the past or no. Does not check for audio.
    def checkIfDownloaded(self)
      return false
    
    
"""

Example dict

vids = {'videos': 
        {
        'title': title, 'length': length, 'author': author, 'url': url
        }
      }


"""
