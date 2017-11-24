from bs4 import BeautifulSoup
from datetime import date, timedelta
import requests
import json
import re

yesterday = date.today() - timedelta(1)
r = requests.get("https://stats.nba.com/scores/{}/{}/{}".format(yesterday.month, yesterday.day, yesterday.year))
if r.status_code == 200:
    soup = BeautifulSoup(r.text)
    for link in soup.find_all('script'):
        if link.string and 'window.nbaStatsLineScore' in link.string:
            linkString = link.string
            matchingString = "nbaStatsLineScore = "
            a = re.search(matchingString, linkString)
            startingIndex = a.start()
            linkString = linkString[startingIndex + len(matchingString):] # Finding index of string, then adding len to start
            linkString = linkString[:-2]
            boxScores = json.loads(linkString)
            for boxScore in boxScores:
                # pass
                #
                # teamcity = boxScore['TEAM_CITY_NAME']
                # teamname = boxScore['TEAM_NAME']
                # points = boxScore['PTS']

                print(boxScore)
                # print(boxScore['TEAM_CITY_NAME'], boxScore['TEAM_NAME'], boxScore['PTS'])

else:
    # something has gone wrong