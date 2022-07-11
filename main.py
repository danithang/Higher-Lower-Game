import random
from replit import clear
from art import logo, vs
from game_data import data


#defining random choice 
def choice():
    return random.choice(data)
    
#defining the 2 choices and most followers and comparing the follower counts between the 2 choices
def compare(answer_a, answer_b, most_followers):
    #if statement is saying if answer_a has more followers than answer_b then return "a" has true or if not true it will return false...the same is for the else statement, if most followers = "b" then it will return true or if not return false
    if answer_a > answer_b:
        return most_followers == "a"
            
    else:
        return most_followers == "b"
#making a play the game function 
def play_game():
    #establishing game play for the whike loop
    game_on = True
    score = 0
    #establishing person 1 from person 2 and giving each the random choice
    person_1 = choice()
    person_2 = choice()
    
    #looping the gameplay
    while game_on:
        print(logo)
        #establishing that player 1 will become player 2 if user gets the person with the higher followers right and continue with the game
        person_1 = person_2
        person_2 = choice()

        #making sure player 1 and player 2 don't have the same matches, if they do then player 2 will get a new random choice
        while person_1 == person_2:
            person_2 = choice()
        
        #printing all comparisons...printing output of original data in the dictionary  
        print(f"Compare A: {person_1['name']}, {person_1['description']}, {person_1['country']}")
        print(vs)
        print(f"Against B: {person_2['name']}, {person_2['description']}, {person_2['country']}")
        #asking user which has most followers 
        most_followers = input("Which one do you think has the most followers?  'A' or 'B': ").lower()
        #estasblishing follower a and b by tying each to person 1 and 2 and getting follower count from dictionary
        follower_a = person_1['follower_count']
        follower_b = person_2['follower_count']
        #putting compare function in variable and changing the outputs to follower_a and follower_b instead of answer_a and answer_b like when originally defined function
        is_correct = compare(follower_a, follower_b, most_followers)
        #clearing for next set of choices
        clear()
        print(logo)
        #seeing if is_correct is right or not...adding plus 1 if user is correct...else game over and final score will add how many user got right
        if is_correct:
            score += 1
            print(f"You are right. Current score: {score}")
        else:
            game_on = False
            print(f"Sorry, wrong choice. Your final score is {score}")
#asking if want to play again and calling play_game function     
while input("Would you like to play the game?  Type 'y' or 'n'. ") == "y":
        play_game()
        
