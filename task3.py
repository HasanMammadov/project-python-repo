def score(game_id):
    print (f'User asked for game {game_id}')
    if game_id==1:
        score = '3-0'
    elif game_id == 2:
        score ='2-1'
    elif game_id == 3:
        score = '1-2'
    else:
        score = '0-0'

    return score

game1_score = score(1)
game2_score = score(2)
game3_score = score(3)
game4_score = score(4)

print(f'Game 1 score was {game1_score}')
print(f'Game 2 score was {game2_score}')
print(f'Game 3 score was {game3_score}')
print(f'Game 4 score was {game4_score}')