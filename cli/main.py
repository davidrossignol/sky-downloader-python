'''
 Created on Tue Dec 17 2019

 Author:  2019 David Rossignol
'''

from search import Search


def audioAnswer():
    pass

def videoAnswer():
    search = Search('video')
    search.initiateQuery()

    


def askUser():
    answer = input("What would you like to do? \n\n(1) Download a video\n(2) Download an audio\n(3) Exit\n\nAnswer: ")

    if answer == '1':
        videoAnswer()
    elif answer == '2':
        audioAnswer
    elif answer == '3':
        pass
    else:
        print("\nInvalid Answer.")
        askUser()


askUser()