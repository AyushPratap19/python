import random

choice_list = ["snake" , "water" , "gun"]
win_matrix = [['Draw' , 'Win' , 'Lose'],['Lose' , 'Draw' , 'Win'],['Win' , 'Lose' , 'Draw']]
dict_points = {'snake' : 0 , 'water' :1 , 'gun':2 }

player_1 = input("Player1 Select your option from (snake,water,gun)?")


player_2 = random.choice(choice_list)
print("computer selected :",player_2)

print("Player1  you : " , win_matrix[dict_points[player_1]][dict_points[player_2]])