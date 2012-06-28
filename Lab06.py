##PART II DATA ENCAPSULATION
import datetime

class Player:
    def __init__(self,firstname,lastname,team = None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team

    def add_score(self,date,score):
        self.scores.append(score)

    def total_score(self):
        summ = 0
        for i in range(len(self.scores)):
            summ+=self.scores[i]
        return summ

    def average_score(self):
        return self.total_score()/len(self.scores)
    
## Testing with these lines of codes
"""
player = Player('Nana','Galore','Manchester United')
player.add_score(datetime.date(2012,06,23) , 1)
player.add_score(datetime.date(2012,06,23) , 2)
player.add_score(datetime.date(2012,06,23) , 3)
player.add_score(datetime.date(2012,06,23) , 4)
player.add_score(datetime.date(2012,06,23) , 5)


print player.total_score()
print player.average_score()

"""

torres = Player('Fernando','Torres','Chelsea FC')
torres.add_score(datetime.date(2012,06,23) , 0)
torres.add_score(datetime.date(2012,06,23) , 0)
torres.add_score(datetime.date(2012,06,23) , 1)
torres.add_score(datetime.date(2012,06,23) , 0)
torres.add_score(datetime.date(2012,06,23) , 1)

print "Torres' average score is " + str(torres.average_score())
#print datetime.date(2012,06,23)
#print sum(torres.scores)



##PART II YOUR FIRST CLASSES
class Team:
    def __init__(self,name, league, manager_name, points = None):
        self.name = name
        self.league = league
        self.manager_name = manager_name
        self.points = points
        self.players = []

    def add_player(self,player):
        self.players.append(player)

    def __str__(self):
        msg = 'TEAM NAME: '+ self.name + '\nLEAGUE: ' + self.league + '\nMANAGER: ' + self.manager_name + '\nPOINTS: '+ str(self.points)
        #msg = msg + 'LEAGUE: ' + self.league + '\n'
        #msg = msg + 'MANAGER: ' + self.manager_name + '\n'
        #msg = msg + 'POINTS: '+ str(self.points),'\n'
       # msg = msg + 'LINE-UP: '+ str(self.players)
        return msg


        
portugal = Team('Portugal','Euro 2012','Paulo Bento',6)
spain = Team('Spain','Euro 2012','Vicente Del Bosque',7)
#spain.add_player('Iniesta')


## 6
torres = Player('Fernando','Torres',spain)
ronaldo = Player('Christiano','Ronaldo',portugal)        
        
## 7
portugal.add_player(ronaldo)
spain.add_player(torres)

print ronaldo.team



class Match:
    def __init__(self,home_team ,away_team,date=None):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.home_scores = {'Torres':1}
        self.away_scores = {'Ronaldo':1}

    
    def home_score(self):
        add = 0
        for p in self.home_scores:
            add+=int(self.home_scores[p])
        return add
    
    def away_score(self):
        add = 0
        for p in self.away_scores:
            add+=int(self.away_scores[p])
        return add

    def winner(self):
        h = self.home_score()
        a = self.away_score()
        if h > a :
            return self.home_team + ' wins'
        elif a > h:
            return self.away_team + ' wins'
        else:
            return 'Draw Match.'

    def add_score(self,player_obj, player_score):
        team = player_obj.team.name
        if self.home_team == team:
            #print 'Home Team'
            for hp in self.home_scores:
                #print hp
                if player_obj.last_name in self.home_scores:
                    self.home_scores[hp] = self.home_scores[hp] + int(player_score)
                    break
                else:
                    self.home_scores[player_obj.last_name] = player_score
                    #print 'Home Teamas'
                    break
        else:
            #print 'Away Team'
            for ap in self.away_scores:
                #print p
                if player_obj.last_name in self.away_scores:
                    self.away_scores[ap] = self.away_scores[ap] + int(player_score)
                    break
                else:
                    self.away_scores = {player_obj.last_name : player_score}
                    break
        
euro_semi_final = Match('Spain','Portugal',datetime.date(2012,06,27))
euro_semi_final.add_score(torres,1)
euro_semi_final.add_score(ronaldo,1)
euro_semi_final.add_score(torres,1)
#print torres.team.name

#print euro_semi_final.home_scores
#print euro_semi_final.away_scores

print euro_semi_final.winner() 
