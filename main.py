from steamstatus.scraper import SteamData
from steamstatus.logo import logo_ascii
import os

def clear_shell():
    os.system('cls' if os.name == 'nt' else 'clear')

steamInfo = SteamData()

get = True
while get:

    clear_shell()
    print(logo_ascii)
    print(' '*25 +"Welcome Key")

    action = input('[1] to get the 10 most played games \n[2] for the 100 games  \n[3] for the Popular Releases \n[4] for the Hot Releases\n[E] to exit key : ? ').lower()

    if action == '1':
        print("search games")
        data_games = steamInfo.select_data(action)
        top_games = steamInfo.content_formated(data_games,action)
        print('saving file')
        steamInfo.save_csv_gamesdata(top_games,action)
        clear_shell()
        

    elif action == '2':
        print("search games")
        data_top_100 = steamInfo.select_data(action)
        top_100_games = steamInfo.content_formated(data_top_100,action)
        print('saving file')
        steamInfo.save_csv_gamesdata(top_100_games,action)
        clear_shell()

    elif action == '3':
        print("search games")
        data_releases = steamInfo.select_data(action)
        popular_releases = steamInfo.content_formated(data_releases,action)
        print('saving file')
        steamInfo.save_csv_gamesdata(popular_releases,action)
        clear_shell()


    elif action == '4':
        print("search games")
        data_hot = steamInfo.select_data(action)
        hot_releases = steamInfo.content_formated(data_hot,action)
        print('saving file')
        steamInfo.save_csv_gamesdata(hot_releases,action)
        clear_shell()
        
    elif action =='e':
        get = False

