
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv



class SteamData:

    def __init__(self) -> None:
        self.url =  "https://steamdb.info/"
        self.top_100_url = 'https://steamdb.info/charts/'
        self.top_100_games_xpath = '//*[@id="table-apps"]/tbody'
        self.top_games_xpath = '//*[@id="main"]/div[2]/div[1]/div[1]/table/tbody'
        self.popular_xpath = '//*[@id="main"]/div[2]/div[2]/div[1]/table/tbody'
        self.hot_realeses_xpath =  '//*[@id="main"]/div[2]/div[2]/div[2]/table/tbody'
        
    def get_content(self,url,xpath):
        
        Chrome_options = webdriver.ChromeOptions()
        Chrome_options.add_experimental_option('detach', True)
        browser = webdriver.Chrome(options=Chrome_options)
       
        browser.get(url)
        sleep(2)

        contents = browser.find_elements(By.XPATH,value=xpath)
        data = []
        for ele in contents:
            data.append(ele.text)

        browser.quit()
        return data

    def select_data(self,action):

        if action == '1':
            xpath_100 = self.top_games_xpath
            url_100 = self.url
            data = self.get_content(url_100,xpath_100)
            return data
        
        elif action == '2':
            xpath = self.top_100_games_xpath
            url = self.top_100_url
            data = self.get_content(url,xpath)
            return data
        
        elif action == '3':
            xpath = self.popular_xpath
            url = self.url
            data = self.get_content(url,xpath)
            return data
        
        elif action == '4':
            xpath = self.hot_realeses_xpath
            url = self.url
            data = self.get_content(url,xpath)
            return data

    def format_data(self,data):

        data_clear = [s.replace(',','.') for s in data]
        content = data_clear[0].splitlines()
        data_games = []
          
        for line in content:
            parts = line.split()
            if len(parts) <= 3:
                name = ''.join(parts[0])
                players = ''.join(parts[-2]) 
                peak = ''.join(parts[-1]) 
                full_name = [f'{name}, {players} ,{peak}']
                data_games.append(full_name) 

            elif len(parts) >= 5:
                name = ' '.join(parts[0:3])
                players = ''.join(parts[-2]) 
                peak = ''.join(parts[-1]) 
                full_name = [f'{name}, {players} ,{peak}']
                data_games.append(full_name) 

            else:
                name = ' '.join(parts[0:2])
                players = ''.join(parts[-2]) 
                peak = ''.join(parts[-1]) 
                full_name = [f'{name}, {players} ,{peak}']
                data_games.append(full_name) 

        return data_games
    
    def formate_data_more(self,data):
        list = [s.replace(',','.').replace('+','') for s in data]
        games = list[0].splitlines()
        top_100_more = []

        for line in games:
            parts = line.split()
            if len(parts) <= 5:
                name = ''.join(parts[1:2])
                players = ''.join(parts[-3]) 
                peak = ''.join(parts[-2]) 
                all_time = ''.join(parts[-1]) 
                full_name = [f'{name}, {players} ,{peak}, {all_time}']
                top_100_more.append(full_name)

            elif len(parts) == 6:
                name = ' '.join(parts[1:3])
                players = ''.join(parts[-3]) 
                peak = ''.join(parts[-2]) 
                all_time = ''.join(parts[-1]) 
                full_name = [f'{name}, {players} ,{peak}, {all_time}']
                top_100_more.append(full_name)

            elif len(parts) == 7:
                name = ' '.join(parts[1:4])
                players = ''.join(parts[-3]) 
                peak = ''.join(parts[-2]) 
                all_time = ''.join(parts[-1]) 
                full_name = [f'{name}, {players} ,{peak}, {all_time}']
                top_100_more.append(full_name)


            elif len(parts) == 8:
                name = ' '.join(parts[1:5])
                players = ''.join(parts[-3]) 
                peak = ''.join(parts[-2]) 
                all_time = ''.join(parts[-1]) 
                full_name = [f'{name}, {players} ,{peak}, {all_time}']
                top_100_more.append(full_name)

            elif len(parts) >= 9:
                name = ' '.join(parts[1:6])
                players = ''.join(parts[-3]) 
                peak = ''.join(parts[-2]) 
                all_time = ''.join(parts[-1]) 
                full_name = [f'{name}, {players} ,{peak}, {all_time}']
                top_100_more.append(full_name)
        return top_100_more
    
    
    def content_formated(self,data,action):
        if action == '1':
            top_games = self.format_data(data)
                
            return top_games
        
        elif action == '2':
            top_100_more = self.formate_data_more(data)

            return top_100_more
           
        
        elif action == '3':
            popular_releases = self.format_data(data)
            return popular_releases
        
        elif action == '4':
            hot_releases = self.format_data(data)

            return hot_releases
        
    def save_data(self,games_list,name_file,name,like,price):
        with open(f'data/{name_file}.csv','w',newline='',encoding='utf-8') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ',delimiter=',')
                writer.writerow([f'{name}',f'{like}',f'{price}'])   
                for line in games_list:    
                    writer.writerow(line)
                print('save')
        
    def save_csv_gamesdata(self,games_list,action):

        if action == '1':
            self.save_data(games_list,'top_games','Most Player Games','Players Now','24h Peak')

        elif action =='2':
            with open('data/Top_100_Game.csv','w',newline='',encoding='utf-8') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ',delimiter=',')
                writer.writerow(['Most Player Game','player Now','24h peak','All-Time_Peak'])   
                for line in games_list:    
                    writer.writerow(line)
                print('save')

        elif action == '3':
            self.save_data(games_list,'Popular Realeses','Popular Releases','24h Peak','Price')
        
        elif action == '4':
            self.save_data(games_list,'Hot Realeses','Hot Releases','Rating','Price')












