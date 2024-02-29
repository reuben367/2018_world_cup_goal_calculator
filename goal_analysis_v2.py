#2018 Football World Cup Challenge -  www.101computing.net/2018-world-cup-goals-analysis/
import time
from collections import defaultdict

def menu():
    print("*********************************************")
    print("*                                           *")
    print("*      2018 World Cup: Goals Analysis       *")
    print("*                                           *")
    print("*********************************************")
    print("")
    print("> Select an option:")
    print("       > A: Total number of goals scored by a given country")
    print("       > B: Total number of goals scored by a given player")
    print("       > C: List the name of all the players who scored for a given country")
    print("       > D: Total number of goals by all countries")
    print("       > E: Total number of goals scored during the first half (45 minutes)")
    print("       > F: Total number of goals scored during the second half (45 minutes to 90 minutes)")
    print("       > G: Total number of goals scored during extra time (after 90 minutes of play)")
    print("       > X: Exit")
    print("")

def create_country_list(file_name):
    '''
    Creates list of unique contries
    '''
    try:
        with open(file_name, "r") as file:
            country_list = []
            for line in file:
                data = line.split(";")
                country_new = data[1].strip()
                if country_new not in country_list:
                    country_list.append(country_new)
        return country_list
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return[]
    
def create_player_list(file_name):
    '''
    create unique list of players in world cup
    '''
    try:
        with open(file_name, "r") as file: 
            player_list = []
            for line in file:
                data = line.split(";")
                player_new = data[0]
                if player_new not in player_list:
                    player_list.append(player_new)
        return player_list
    
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return[]
    


def goals_per_country(file_name, countries):
    '''
    Takes user defined country, checks against list of countries in file and outputs numbers of goals
    scored.
    
    '''
    with open(file_name, "r") as file:
        while True:
            chosen_country = input("> Enter country:").lower()
            if chosen_country in countries:
                goals = 0
                for line in file:
                    data = line.split(";")
                    country = data[1]
                    if country == chosen_country:
                        goals = goals + 1
                print("\n> " + chosen_country.title() + " scored " + str(goals) + " goal(s) in the 2018 world cup.")
                break
            print("This country was not in the 2018 World Cup, try again")

def goals_per_player(file_name,players):
    '''
    Takes user defined player, checks against list of players in file and outputs numbers of goals
    scored.
    '''
    with open(file_name, "r") as file:
        while True:
            chosen_player = input("> Enter Player:").lower()
            if chosen_player in players:
                goals = 0
                for line in file:
                    data = line.split(";")
                    player = data[0]
                    if player == chosen_player:
                        goals = goals + 1
                
                print("\n> " + chosen_player.title() + " scored " + str(goals) + " goal(s) in the 2018 world cup.")
                break
            print("This player was not in the 2018 World Cup, try again")
        

def country_goal_scorers(file_name, countries):
    '''
    returns goal scorers for user specified country
    '''
    with open(file_name, "r") as file:
        goal_scorers_for_country_list = []
        while True:
            goal_scorers_for_country = input(">Enter country: ").lower()
            if goal_scorers_for_country in countries:
                for line in file:
                    data = line.split(";")
                    country = data[1]
                    player = data[0]
                    if country == goal_scorers_for_country and player != "og":
                        if player not in goal_scorers_for_country_list:
                            goal_scorers_for_country_list.append([player])


                name_counts = defaultdict(int)
                for sublist in goal_scorers_for_country_list:
                    name_counts[sublist[0]] += 1

                print(f"The goal scorers for {goal_scorers_for_country} where:")
                for name, count in name_counts.items():
                    print(f"{name} x {count} goals")
                break
            print("This country was not in the 2018 World Cup, try again")

def total_goals(file_name):

    file = open(file_name,"r")

    line_count = 0

    for line in file:
        line_count +=1

    file.close()
    return print(f"The total number of goals scored in the 2018 World Cup is {line_count}.")

def first_half_goals(file_name, countries):
    '''
    Function calculates total first half goals for user defined team
    '''


    with open(file_name, "r") as file:

        while True:
            chosen_country = input("> Enter country:").lower()
            if chosen_country in [country.lower() for country in countries]:
                first_half_goals = 0  # Reset the counter for each country
                for line in file:
                    data = line.strip().split(";")
                    if int(data[2]) < 46 and data[1].lower() == chosen_country:
                        first_half_goals += 1
                print(f"Total first half goals for {chosen_country}: {first_half_goals}")
                break 
            print("This country was not in the 2018 FIFA World Cup.")

def second_half_goals(file_name, countries):
    '''
    Function calculates total second half goals for user defined team
    '''


    with open(file_name, "r") as file:

        while True:
            chosen_country = input("> Enter country:").lower()
            if chosen_country in [country.lower() for country in countries]:
                first_half_goals = 0  # Reset the counter for each country
                for line in file:
                    data = line.strip().split(";")
                    if int(data[2]) > 45 and int(data[2]) < 91 and data[1].lower() == chosen_country:
                        first_half_goals += 1
                print(f"Total second half goals for {chosen_country}: {first_half_goals}")
                break 
            print("This country was not in the 2018 FIFA World Cup.")

def extra_time_goals(file_name, countries):
    '''
    Function calculates extra time goals for user defined team
    '''

    with open(file_name, "r") as file:

        while True:
            chosen_country = input("> Enter country:").lower()
            if chosen_country in [country.lower() for country in countries]:
                first_half_goals = 0  # Reset the counter for each country
                for line in file:
                    data = line.strip().split(";")
                    if int(data[2]) > 90  and data[1].lower() == chosen_country:
                        first_half_goals += 1
                print(f"Total extra time goals for {chosen_country}: {first_half_goals}")
                break 
            print("This country was not in the 2018 FIFA World Cup.")
##################### Main Program Starts Here ##############################
# define file path and call functions to create list 


user_choice=""

while user_choice!="X":
    menu()
    user_choice = input("> Select an option from the menu (A to G) or X to exit:").upper()
    if user_choice=="A":
        goals_per_country("goals.csv", create_country_list("goals.csv"))
    elif user_choice=="B":
        goals_per_player("goals.csv", create_player_list("goals.csv"))
    elif user_choice =="C":
        country_goal_scorers("goals.csv", create_country_list("goals.csv"))
    elif user_choice =="D":
        total_goals("goals.csv")
    elif user_choice == "E":
        first_half_goals("goals.csv", create_country_list("goals.csv"))
    elif user_choice == "F":
        second_half_goals("goals.csv", create_country_list("goals.csv"))
    elif user_choice == "G":
        extra_time_goals("goals.csv", create_country_list("goals.csv"))

    
  #...
    time.sleep(3)
    print("\n\n\n")
    print("Good bye!")    
