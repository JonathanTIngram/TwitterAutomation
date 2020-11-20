#Jonathan Ingram
#12/20/2019
#Open files for the Twitter bot

import random

class OpenFiles:
    def __init__(self):
        print("File Openings")


    #API keys

    def openApiKey():

        with open("Keys/apiKey.txt", "r") as a:
            apiKey = a.read()

        return apiKey

    def openApiSecretKey():

        with open("Keys/apiSecretKey.txt", "r") as b:
            apiSecretKey = b.read()

        return apiSecretKey

    def openAccessToken():

        with open("Keys/accessToken.txt", "r") as c:
            accessToken = c.read()

        return accessToken

    def openAccessTokenSecret():

        with open("Keys/accessTokenSecret.txt", "r") as d:
            accessTokenSecret = d.read()

        return accessTokenSecret


    #Words


    def getNoun():
        with open("Words/nouns.txt", "r") as n:
            nouns = n.readlines()

        noun = random.choice(nouns)

        return noun

    def getVerb():
        with open("Words/verbs.txt", "r") as v:
            verbs = v.readlines()

        verb = random.choice(verbs)

        return verb

    def getPastTenseVerb():

        with open("Words/pastTenseVerbs.txt", "r") as ptv:

            pastTensev = ptv.readlines()

        PTV = random.choice(pastTensev)

        return PTV

    def getName():
        
        with open("Words/names.txt", "r") as na:
            names = na.readlines()

        name = random.choice(names)

        return name



