"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/23/2012	| 1
"""
import datetime

## create the player_stats data structure
player_stats = {'rooney':([datetime.date(2012,06,23),2], [datetime.date(2012,06,25),2]),
                'ronaldo':([datetime.date(2012,06,19),0], [datetime.date(2012,06,20),3]),
                'torres':([datetime.date(2012,06,21),0], [datetime.date(2012,06,23),1])}

##Choice of data structure
"""
A dictionary with keys as player names and values
as list of tuples that hold the dates and number of
goals scored by each player. This is so because
the number of goals and the dates cannot change and
it has a list because a player has one or more days
he has scored goals.

"""

## implement highest_score

def highest_score(player_stats):
    ct1 = 0
    ct2 = 0
    for player in player_stats:
        p1 = player_stats[player]
        if p1[0][1] > ct1:
            ct1 = p1[0][1]
            ls1 = (player,player_stats[player][0][0],ct1)
        if p1[1][1] > ct2:
            ct2 = p1[1][1]
            ls2 = (player,player_stats[player][1][0],ct2)
            
    if ct1 > ct2:
        print 'Top Scorer---',ls1
    if ct1 == ct2:
        print '1.Top Scorer---',ls1,'\n','2.Top Scorer---',ls2
    if ct1 < ct2:
        print 'Top Scorer--',ls2
    

            
    
## implement highest_score_for_player
def highest_score_for_player(player_stats,player):
    ct = 0
    for i in player_stats:
        if str(player) in player_stats:
            n = len(player_stats[str(player)])
            for j in range(n):
                sc = player_stats[player][j][1]
                if sc > ct:
                    ct = sc
            print "Highest score by " + player + " is " + str(ct)
            break
        else:
            print player + " not in system."
            break

    


## implement highest_scorer
def highest_scorer(player_stats):
    
    ct = 0
    for p in player_stats:
        n = len(player_stats[str(p)])
        summ = 0
        for k in range(n):
            summ+=player_stats[p][k][1]
        if summ > ct:
            ct = summ
            player = p
    print player + " has the highest scoring sum of " + str(ct) + " goals."
    
