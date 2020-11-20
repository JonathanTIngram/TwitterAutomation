#Jonathan Ingram
#12/20/2019
#define differnt types of posts
import random
import openFiles
import tweepy


apiKey = openFiles.OpenFiles.openApiKey()
apiSecretKey = openFiles.OpenFiles.openApiSecretKey()

accessToken = openFiles.OpenFiles.openAccessToken()
accessTokenSecret = openFiles.OpenFiles.openAccessTokenSecret()


auth = tweepy.OAuthHandler(apiKey, apiSecretKey)

auth.set_access_token(accessToken,accessTokenSecret)

api = tweepy.API(auth)

class Posts:
    def __init__(self):
        print("Instance of posts class within PostTypes.py")

    def nounVerbNoun():
        

        nvn = openFiles.OpenFiles.getNoun() + openFiles.OpenFiles.getVerb() + openFiles.OpenFiles.getNoun()
        print(nvn)
        api.update_status(status=nvn)

    def pastTenseNounVerbNoun():

        nPTVn = "The\n" + openFiles.OpenFiles.getNoun() + openFiles.OpenFiles.getPastTenseVerb().lower() + "the\n" +  openFiles.OpenFiles.getNoun()

        print(nPTVn)

    def nameVerbNoun():

        nPTVn = openFiles.OpenFiles.getName() + openFiles.OpenFiles.getPastTenseVerb().lower() + "the\n" +  openFiles.OpenFiles.getNoun()

        print(nPTVn)


    def newMeme():

        with open("Words/memeWords.txt", "r") as m:
            memes = m.readlines()


        freshMeme = True

        while(freshMeme == True):

            meme = random.choice(memes) + random.choice(memes)

            print(meme)

            answer = input("Is this a good meme? ")

            if(answer == "y" or answer == "yes"):
                print("Posted to twitter")
                return meme
                

                newM = input("Would you like another meme? ")
                if(newM == "y" or newM == "yes"):
                   print("Coming in hot\n\n")
                   
                else:
                    print("\n\nYour call my guy\n\n")
                    freshMeme = False

            else:
                print("\nshid u right")
                print("Not posted\n\n")

a = Posts.newMeme()



api.update_status(a)
