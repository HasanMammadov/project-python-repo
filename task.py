def print_team(team_name, team_list):
    print(f'Here is the list for {team_name}')
    for player in team_list:
        print(player)


team_usa = ['Ethan H', 'Sean J', 'Goi R', 'Tiom W']
team_brazil = ['Neymar', 'Pele']
team_argentina = ['Messi']


print_team('Team Usa',team_usa)
print_team('Team Brazil',team_brazil)
print_team('Team Argentina',team_argentina)