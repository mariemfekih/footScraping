import requests #nemshy l safha l feha les donnees(Yallakora page :matchCenter)
from bs4 import BeautifulSoup #parsing lel html code ykhalini nkharej les donnees
import csv 


date= input("Please enter a Date in the following format MM/DD/YYYY :")
page= requests.get(f"https://www.yallakora.com/match-center/?date={date}") #formated string
#page= requests.get("https://www.yallakora.com/match-center/?date=11/23/2022")
def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    #print(soup)
    matches_details= []

    championships= soup.findAll("div", {'class': 'matchCard'}) #kol boutoula li

    def get_match_info(championships): #tags children are available in a list called .contents
       championship_title= championships.contents[1].find("h2").text.strip()#text bsh nkharej l text w strip nahy espace
       all_matches=championships.contents[3].findAll('li') #kol match f li
       number_of_matches= len(all_matches)
       for i in range(number_of_matches):
          
        #get team names
          team_A=all_matches[i].find('div',{'class': 'teamA'}).text.strip()
          team_B=all_matches[i].find('div',{'class': 'teamB'}).text.strip()
          
          #get score
          match_result=all_matches[i].find('div',{'class':'MResult'}).find_all('span', {'class': 'score'})#andi 2 span score wehed mtaa score teamA et team B
          score=f"{match_result[0].text.strip()} - {match_result[0].text.strip()}"

         
          #get match time
          match_time=all_matches[i].find('div',{'class':'MResult'}).find('span', {'class':'time'}).text.strip()
         
          #add match info to matches_details
          matches_details.append({"Tournament type":championship_title,"first team":team_A,"second team":team_B,"match time":match_time,"result":score})#"key":value
  
    for i in range (len(championships)): 
        get_match_info(championships[i]) 
    
    keys=matches_details[0].keys()

    with open('C:\\Users\\marie\\Desktop\\Projects\\yalaKoora\\matches_details.csv', 'w') as output_file:
  
       dict_writer= csv.DictWriter(output_file,keys)
       dict_writer.writeheader()#nhotha l 3anewin
       dict_writer.writerows(matches_details)
       print("file created")

main(page)#nlanci l function
