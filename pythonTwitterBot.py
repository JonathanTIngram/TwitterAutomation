#Jonathan Ingram
#12/10/2019
#Twitter Automation



#Two functions one that post random word in a sentense format: Noun-Verb-Noun
#Other format: Name-Past Tense Verb-Adj-Noun

import tweepy
import time
from time import strftime
import random
from random import randint

import openFiles
import PostTypes

#keys
apiKey = openFiles.OpenFiles.openApiKey()
apiSecretKey = openFiles.OpenFiles.openApiSecretKey()

accessToken = openFiles.OpenFiles.openAccessToken()
accessTokenSecret = openFiles.OpenFiles.openAccessTokenSecret

auth = tweepy.OAuthHandler(apiKey, apiSecretKey)

auth.set_access_token(accessToken,accessTokenSecret)

api = tweepy.API(auth)


#update status
postTime = "17:30:30"

imageList = []
messageList = []



def getTime():
    string = strftime('%H:%M:%S') 
    print(string)
    return string

def tweetImage():
    media = api.media_upload("image.png")

    post_result = api.update_status(status="#image:\n\n\n", media_ids=[media.media_id])

def onePost():
    api.update_status(status="test")
    



def post():
    while (postTime != getTime()): #loop until it's the time specified



        print(str(getTime()))
        time.sleep(1)



        if(postTime == getTime()):
            PostTypes.Posts.nounVerbNoun()


if __name__ == "__main__":
    post()
