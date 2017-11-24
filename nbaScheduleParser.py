class Team():

    def __init__(self, teamname, teamcity):
        self.teamname = teamname
        self.teamcity = teamcity
    def __str__(self):
        return "This is the representation of the class team name {  and city {}".format(self.teamname, self.teamcity)

class Schedule():

    def __init__(self, dateAndTime, isTelevized, homeTeamId, awayTeamId, homeTeamScore, awayTeamScore):
        self.dateAndTime = dateAndTime
        self.isTelevized = isTelevized
        self.homeTeamId = homeTeamId
        self.awayTeamId = awayTeamId
        self.homeTeamScore = homeTeamScore
        self.awayTeamScore = awayTeamScore

    def __str__(self):
        return "Hey"

import json

data = json.load(open('nba_schedule_2017.json'))

for monthlyGames in data['lscd']:
    for game in monthlyGames['mscd']['g']:
        # print(game)
        awayTeam = Team(game['v']['tn'], game['v']['tc'])
        homeTeam = Team(game['h']['tn'], game['h']['tc'])
        print(awayTeam)
        exit()
         # try and find based on team name, if nothing insert and get id
        isTelevized = False
        if len(game['bd']['b']) > 0:
            if game['bd']['b'][0]['scope'] == 'natl':
                isTelevized = True

        schedule = Schedule(game['etm'], isTelevized, homeTeamId, awayTeamId, game['h']['s'], game['a']['s'])

