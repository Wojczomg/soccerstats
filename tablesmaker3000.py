import os
import numpy as np
from collections import deque
from collections import OrderedDict
def registry():
	match_counter = 0
	home_team_won = 0
	home_team_scored = 0
	home_team_not_concede = 0
	home_team_won_margin1 = 0
	home_team_won_margin_over1 = 0
	home_team_won_margin_over2 = 0
	home_team_won_margin_over3 = 0
	total_goals_home_avg = 0 
	total_goals_away_avg = 0 
	over_25_avg = 0 
	team_total_goals_home = {}
	team_total_goals_away = {}
	team_total_concede_home = {}
	team_total_concede_away = {}
	team_match_counter = {}
	team_match_counter_home = {}
	team_match_counter_away = {}
	team_won = {}
	team_lost = {}
	team_draw = {}
	team_scored = {}
	team_concede = {}
	team_scored_goals_home_distrib = {}  
	team_scored_goals_away_distrib = {}  
	team_concede_goals_home_distrib = {}  
	team_concede_goals_away_distrib = {}  
	team_scored_2ndhalf = {}
	team_concede_2ndhalf = {}
	team_scored_1ndhalf = {}
	team_concede_1ndhalf = {}
	team_scored_exl1 = {}
	team_concede_exl1 = {}
	team_scored_over1 = {}
	team_concede_over1 = {}
	team_scored_over2 = {}
	team_concede_over2 = {}
	team_avg_goals_scored = {} 
	team_avg_goals_concede = {} 
	team_goals_scored_last8 = {}
	team_goals_concede_last8 = {}
	team_avg_goals_scored_last8 = {}
	team_avg_goals_concede_last8 = {} 
	team_over25_home = {}
	team_over25_away = {}
	team_over35_home = {}
	team_over35_away = {}

	def fun_match_counter(x):
		nonlocal match_counter
		match_counter+=1

	def fun_home_team_won(x):
		nonlocal home_team_won
		if int(x[2]) > int(x[3]):
			home_team_won+=1

	def fun_home_team_scored(x):
		nonlocal home_team_scored
		if x[2] != 0:
			home_team_scored+=1

	def fun_home_team_not_concede(x):
		nonlocal home_team_not_concede
		if x[3] == 0:
			home_team_not_concede+=1

	def fun_home_team_won_margin1(x):
		nonlocal home_team_won_margin1
		if x[2] == x[3] + 1:
			home_team_won_margin1+=1

	def	fun_home_team_won_margin_over1(x):
		nonlocal home_team_won_margin_over1
		if x[2] > x[3] + 1:
			home_team_won_margin_over1+=1

	def	fun_home_team_won_margin_over2(x):
		nonlocal home_team_won_margin_over2
		if x[2] > x[3] + 2:
			home_team_won_margin_over2+=1

	def	fun_home_team_won_margin_over3(x):
		nonlocal home_team_won_margin_over3
		if x[2] > x[3] + 3:
			home_team_won_margin_over3+=1

	def fun_team_total_goals_home(x):
		nonlocal team_total_goals_home
		if x[0] not in team_total_goals_home:
			team_total_goals_home[x[0]]=0
		team_total_goals_home[x[0]]+=x[2]

	def fun_team_total_goals_away(x):
		nonlocal team_total_goals_away
		if x[1] not in team_total_goals_away:
			team_total_goals_away[x[1]]=0
		team_total_goals_away[x[1]]+=x[3]

	def fun_team_total_concede_home(x):
		nonlocal team_total_concede_home
		if x[0] not in team_total_concede_home:
			team_total_concede_home[x[0]]=0
		team_total_concede_home[x[0]]+=x[3]

	def fun_team_total_concede_away(x):
		nonlocal team_total_concede_away
		if x[1] not in team_total_concede_away:
			team_total_concede_away[x[1]]=0
		team_total_concede_away[x[1]]+=x[2]	

	def fun_team_match_counter(x):
		nonlocal team_match_counter
		if x[0] not in team_match_counter:
			team_match_counter[x[0]]=0
		if x[1] not in team_match_counter:
			team_match_counter[x[1]]=0	
		team_match_counter[x[0]]+=1
		team_match_counter[x[1]]+=1	

	def fun_team_match_counter_home(x):
		nonlocal team_match_counter_home
		if x[0] not in team_match_counter_home:
			team_match_counter_home[x[0]]=0
		team_match_counter_home[x[0]]+=1

	def fun_team_match_counter_away(x):
		nonlocal team_match_counter_away
		if x[1] not in team_match_counter_away:
			team_match_counter_away[x[1]]=0
		team_match_counter_away[x[1]]+=1

	def fun_team_won(x):
		nonlocal team_won
		if x[0] not in team_won:
			team_won[x[0]]=0
		if x[1] not in team_won:
			team_won[x[1]]=0	
		if x[2] > x[3]:
			team_won[x[0]]+=1
		else:
			team_won[x[1]]+=1	

	def fun_team_lost(x):
		nonlocal team_lost
		if x[0] not in team_lost:
			team_lost[x[0]]=0
		if x[1] not in team_lost:
			team_lost[x[1]]=0
		if x[2] > x[3]:
			team_lost[x[1]]+=1
		else:
			team_lost[x[0]]+=1

	def fun_team_draw(x):
		nonlocal team_draw
		if x[0] not in team_draw:
			team_draw[x[0]]=0
		if x[1] not in team_draw:
			team_draw[x[1]]=0
		if x[2] == x[3]:
			team_draw[x[0]]+=1
			team_draw[x[1]]+=1	

	def	fun_team_scored(x):
		nonlocal team_scored
		if x[0] not in team_scored:
			team_scored[x[0]]=0
		if x[1] not in team_scored:
			team_scored[x[1]]=0	
		if x[2] != 0:
			team_scored[x[0]]+=1
		if x[3] != 0:
			team_scored[x[1]]+=1

	def	fun_team_concede(x):
		nonlocal team_concede
		if x[0] not in team_concede:
			team_concede[x[0]]=0
		if x[1] not in team_concede:
			team_concede[x[1]]=0
		if x[2] != 0:
			team_concede[x[1]]+=1
		if x[3] != 0:
			team_concede[x[0]]+=1		

	def fun_team_scored_2ndhalf(x):
		nonlocal team_scored_2ndhalf
		if x[0] not in team_scored_2ndhalf:
			team_scored_2ndhalf[x[0]]=0
		if x[1] not in team_scored_2ndhalf:
			team_scored_2ndhalf[x[1]]=0	
		if x[2] - x[4] != 0:
			team_scored_2ndhalf[x[0]]+=1
		if x[3] - x[5] != 0:
			team_scored_2ndhalf[x[1]]+=1

	def fun_team_concede_2ndhalf(x):
		nonlocal team_concede_2ndhalf
		if x[0] not in team_concede_2ndhalf:
			team_concede_2ndhalf[x[0]]=0
		if x[1] not in team_concede_2ndhalf:
			team_concede_2ndhalf[x[1]]=0	
		if x[2] - x[4] != 0:
			team_concede_2ndhalf[x[1]]+=1
		if x[3] - x[5] != 0:
			team_concede_2ndhalf[x[0]]+=1

	def fun_team_scored_1ndhalf(x):
		nonlocal team_scored_1ndhalf
		if x[0] not in team_scored_1ndhalf:
			team_scored_1ndhalf[x[0]]=0
		if x[1] not in team_scored_1ndhalf:
			team_scored_1ndhalf[x[1]]=0	
		if x[4] != 0:
			team_scored_1ndhalf[x[0]]+=1
		if x[5] != 0:
			team_scored_1ndhalf[x[1]]+=1

	def fun_team_concede_1ndhalf(x):
		nonlocal team_concede_1ndhalf
		if x[0] not in team_concede_1ndhalf:
			team_concede_1ndhalf[x[0]]=0
		if x[1] not in team_concede_1ndhalf:
			team_concede_1ndhalf[x[1]]=0	
		if x[4] != 0:
			team_concede_1ndhalf[x[1]]+=1
		if x[5] != 0:
			team_concede_1ndhalf[x[0]]+=1				

	def fun_team_scored_exl1(x):
		nonlocal team_scored_exl1
		if x[0] not in team_scored_exl1:
			team_scored_exl1[x[0]]=0
		if x[1] not in team_scored_exl1:
			team_scored_exl1[x[1]]=0	
		if x[2] == 1:
			team_scored_exl1[x[0]]+=1
		if x[3] == 1:
			team_scored_exl1[x[1]]+=1

	def fun_team_concede_exl1(x):
		nonlocal team_concede_exl1
		if x[0] not in team_concede_exl1:
			team_concede_exl1[x[0]]=0
		if x[1] not in team_concede_exl1:
			team_concede_exl1[x[1]]=0	
		if x[2] == 1:
			team_concede_exl1[x[1]]+=1
		if x[3] == 1:
			team_concede_exl1[x[0]]+=1	

	def fun_team_scored_over1(x):
		nonlocal team_scored_over1
		if x[0] not in team_scored_over1:
			team_scored_over1[x[0]]=0
		if x[1] not in team_scored_over1:
			team_scored_over1[x[1]]=0	
		if x[2] > 1:
			team_scored_over1[x[0]]+=1
		if x[3] > 1:
			team_scored_over1[x[1]]+=1


	def fun_team_concede_over1(x):
		nonlocal team_concede_over1
		if x[0] not in team_concede_over1:
			team_concede_over1[x[0]]=0
		if x[1] not in team_concede_over1:
			team_concede_over1[x[1]]=0	
		if x[2] > 1:
			team_concede_over1[x[1]]+=1
		if x[3] > 1:
			team_concede_over1[x[0]]+=1

	def fun_team_scored_over2(x):
		nonlocal team_scored_over2
		if x[0] not in team_scored_over2:
			team_scored_over2[x[0]]=0
		if x[1] not in team_scored_over2:
			team_scored_over2[x[1]]=0	
		if x[2] > 2:
			team_scored_over2[x[0]]+=1
		if x[3] > 2:
			team_scored_over2[x[1]]+=1


	def fun_team_concede_over2(x):
		nonlocal team_concede_over2
		if x[0] not in team_concede_over2:
			team_concede_over2[x[0]]=0
		if x[1] not in team_concede_over2:
			team_concede_over2[x[1]]=0	
		if x[2] > 2:
			team_concede_over2[x[1]]+=1
		if x[3] > 2:
			team_concede_over2[x[0]]+=1	

	def fun_team_goals_scored_last8(x):
		nonlocal team_goals_scored_last8
		if x[0] not in team_goals_scored_last8:
			team_goals_scored_last8[x[0]] = deque(maxlen=8)
		if x[1] not in team_goals_scored_last8:
			team_goals_scored_last8[x[1]] = deque(maxlen=8)	
		team_goals_scored_last8[x[0]].append(x[2])
		team_goals_scored_last8[x[1]].append(x[3])	

	def fun_team_goals_concede_last8(x):
		nonlocal team_goals_concede_last8
		if x[0] not in team_goals_concede_last8:
			team_goals_concede_last8[x[0]] = deque(maxlen=8)
		if x[1] not in team_goals_concede_last8:
			team_goals_concede_last8[x[1]] = deque(maxlen=8)	
		team_goals_concede_last8[x[0]].append(x[2])
		team_goals_concede_last8[x[1]].append(x[3])	

	def fun_team_over25_home(x):
		nonlocal team_over25_home
		if x[0] not in team_over25_home:
			team_over25_home[x[0]]=0
		if x[2] + x[3] > 2.5:
			team_over25_home[x[0]]+=1

	def fun_team_over25_away(x):
		nonlocal team_over25_away
		if x[1] not in team_over25_away:
			team_over25_away[x[1]]=0
		if x[2] + x[3] > 2.5:
			team_over25_away[x[1]]+=1	

	def fun_team_over35_home(x):
		nonlocal team_over35_home
		if x[0] not in team_over35_home:
			team_over35_home[x[0]]=0
		if x[2] + x[3] > 3.5:
			team_over35_home[x[0]]+=1

	def fun_team_over35_away(x):
		nonlocal team_over35_away
		if x[1] not in team_over35_away:
			team_over35_away[x[1]]=0
		if x[2] + x[3] > 3.5:
			team_over35_away[x[1]]+=1	
					
	def reader(x):
		row = OrderedDict({"home": x[0],
			"away": x[1],
			"homeFT": x[2],
			"awayFT": x[3],
			"homeHT": x[4],
			"awayHT": x[5],
		"home_win": home_team_won/match_counter,
		"home_team_scored": home_team_scored/match_counter,
		"home_team_not_concede": home_team_not_concede/match_counter,
		"home_team_won_margin1": home_team_won_margin1/match_counter,
		"home_team_won_margin_over1": home_team_won_margin_over1/match_counter,
		"home_team_won_margin_over2": home_team_won_margin_over2/match_counter,
		"home_team_won_margin_over3": home_team_won_margin_over3/match_counter,
		"total_goals_home_avg": sum(list(team_total_goals_home.values()))/match_counter,
		"total_goals_away_avg": sum(list(team_total_goals_away.values()))/match_counter,
		"over_25_avg": np.mean([((team_over25_home[i] + team_over25_away[i])/team_match_counter[i]) for i in team_match_counter]),
		"team1_total_goals_home": team_total_goals_home[x[0]]/team_match_counter_home[x[0]],
		"team1_total_goals_away": team_total_goals_away[x[0]]/team_match_counter_away[x[0]],
		"team1_won": team_won[x[0]]/team_match_counter[x[0]],
		"team1_lost": team_lost[x[0]]/team_match_counter[x[0]],
		"team1_draw": team_draw[x[0]]/team_match_counter[x[0]],
		"team1_scored": team_scored[x[0]]/team_match_counter[x[0]],
		"team1_concede": team_concede[x[0]]/team_match_counter[x[0]],
		"team1_scored_goals_home_distrib": team_total_goals_home[x[0]]/(team_total_goals_home[x[0]] + team_total_goals_away[x[0]]),
		"team1_scored_goals_away_distrib": team_total_goals_away[x[0]]/(team_total_goals_home[x[0]] + team_total_goals_away[x[0]]),
		"team1_concede_goals_home_distrib": team_total_concede_home[x[0]]/(team_total_concede_home[x[0]] + team_total_concede_away[x[0]]),
		"team1_concede_goals_away_distrib": team_total_concede_away[x[0]]/(team_total_concede_home[x[0]] + team_total_concede_away[x[0]]),
		"team1_scored_2ndhalf": team_scored_2ndhalf[x[0]]/team_match_counter[x[0]],
		"team1_concede_2ndhalf": team_concede_2ndhalf[x[0]]/team_match_counter[x[0]],
		"team1_scored_1ndhalf": team_scored_1ndhalf[x[0]]/team_match_counter[x[0]],
		"team1_concede_1ndhalf": team_concede_1ndhalf[x[0]]/team_match_counter[x[0]],
		"team1_scored_exl1": team_scored_exl1[x[0]]/team_match_counter[x[0]],
		"team1_concede_exl1": team_concede_exl1[x[0]]/team_match_counter[x[0]],
		"team1_scored_over1": team_scored_over1[x[0]]/team_match_counter[x[0]],
		"team1_concede_over1": team_concede_over1[x[0]]/team_match_counter[x[0]],
		"team1_scored_over2": team_scored_over2[x[0]]/team_match_counter[x[0]],
		"team1_concede_over2": team_concede_over2[x[0]]/team_match_counter[x[0]],
		"team1_avg_goals_scored": (team_total_goals_home[x[0]] + team_total_goals_away[x[0]])/team_match_counter[x[0]],
		"team1_avg_goals_concede": (team_total_concede_home[x[0]] + team_total_concede_away[x[0]])/team_match_counter[x[0]],
		"team1_avg_goals_scored_last8": sum(team_goals_scored_last8[x[0]])/8,
		"team1_avg_goals_concede_last8": sum(team_goals_concede_last8[x[0]])/8,
		"team1_over25_home": team_over25_home[x[0]]/team_match_counter_home[x[0]],
		"team1_over25_away": team_over25_away[x[0]]/team_match_counter_away[x[0]],
		"team1_over35_home": team_over35_home[x[0]]/team_match_counter_home[x[0]],
		"team1_over35_away": team_over35_away[x[0]]/team_match_counter_away[x[0]],


		"team2_total_goals_home": team_total_goals_home[x[1]]/team_match_counter_home[x[1]],
		"team2_total_goals_away": team_total_goals_away[x[1]]/team_match_counter_away[x[1]],
		"team2_won": team_won[x[1]]/team_match_counter[x[1]],
		"team2_lost": team_lost[x[1]]/team_match_counter[x[1]],
		"team2_draw": team_draw[x[1]]/team_match_counter[x[1]],
		"team2_scored": team_scored[x[1]]/team_match_counter[x[1]],
		"team2_concede": team_concede[x[1]]/team_match_counter[x[1]],
		"team2_scored_goals_home_distrib": team_total_goals_home[x[1]]/(team_total_goals_home[x[1]] + team_total_goals_away[x[1]]),
		"team2_scored_goals_away_distrib": team_total_goals_away[x[1]]/(team_total_goals_home[x[1]] + team_total_goals_away[x[1]]),
		"team2_concede_goals_home_distrib": team_total_concede_home[x[1]]/(team_total_concede_home[x[1]] + team_total_concede_away[x[1]]),
		"team2_concede_goals_away_distrib": team_total_concede_away[x[1]]/(team_total_concede_home[x[1]] + team_total_concede_away[x[1]]),
		"team2_scored_2ndhalf": team_scored_2ndhalf[x[1]]/team_match_counter[x[1]],
		"team2_concede_2ndhalf": team_concede_2ndhalf[x[1]]/team_match_counter[x[1]],
		"team2_scored_1ndhalf": team_scored_1ndhalf[x[1]]/team_match_counter[x[1]],
		"team2_concede_1ndhalf": team_concede_1ndhalf[x[1]]/team_match_counter[x[1]],
		"team2_scored_exl1": team_scored_exl1[x[1]]/team_match_counter[x[1]],
		"team2_concede_exl1": team_concede_exl1[x[1]]/team_match_counter[x[1]],
		"team2_scored_over1": team_scored_over1[x[1]]/team_match_counter[x[1]],
		"team2_concede_over1": team_concede_over1[x[1]]/team_match_counter[x[1]],
		"team2_scored_over2": team_scored_over2[x[1]]/team_match_counter[x[1]],
		"team2_concede_over2": team_concede_over2[x[1]]/team_match_counter[x[1]],
		"team2_avg_goals_scored": (team_total_goals_home[x[1]] + team_total_goals_away[x[1]])/team_match_counter[x[1]],
		"team2_avg_goals_concede": (team_total_concede_home[x[1]] + team_total_concede_away[x[1]])/team_match_counter[x[1]],
		"team2_avg_goals_scored_last8": sum(team_goals_scored_last8[x[1]])/8,
		"team2_avg_goals_concede_last8": sum(team_goals_concede_last8[x[1]])/8,
		"team2_over25_home": team_over25_home[x[1]]/team_match_counter_home[x[1]],
		"team2_over25_away": team_over25_away[x[1]]/team_match_counter_away[x[1]],
		"team2_over35_home": team_over35_home[x[1]]/team_match_counter_home[x[1]],
		"team2_over35_away": team_over35_away[x[1]]/team_match_counter_away[x[1]],
		})
		return list(row.values())
									


	return {"reader": reader,
			"writer": [fun_match_counter, fun_home_team_won, fun_home_team_scored,
			fun_home_team_not_concede, fun_home_team_won_margin1, fun_home_team_won_margin_over1,
			fun_home_team_won_margin_over2, fun_home_team_won_margin_over3, fun_team_total_goals_home, 
			fun_team_total_goals_away, fun_team_total_concede_home, fun_team_total_concede_away, 
			fun_team_match_counter, fun_team_match_counter_home, fun_team_match_counter_away, 
			fun_team_won, fun_team_lost, fun_team_draw, fun_team_scored, fun_team_concede, 
			fun_team_scored_2ndhalf, fun_team_concede_2ndhalf, fun_team_scored_1ndhalf, fun_team_concede_1ndhalf,
			fun_team_scored_exl1, fun_team_concede_exl1, fun_team_scored_over1, fun_team_concede_over1, 
			fun_team_scored_over2, fun_team_concede_over2, fun_team_goals_scored_last8, fun_team_goals_concede_last8,
			fun_team_over25_home, fun_team_over25_away, fun_team_over35_home, fun_team_over35_away],
			"ch": team_concede_1ndhalf
			}

					
