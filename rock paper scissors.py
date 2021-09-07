#create a game with a rock paper scissors, and it will print an error if the spelling is wrong
#also it will take the users player

#variables are t, player player and computer

from random import randint #for the random integer variable

#this is for the play
t = ["rock", "paper", "scissors"] #list of play of the computer

#set up for variables
name = input("Enter player name here: ")
computer = t[randint(0, 2)] #format is player of list[randint(indexes of list)]
player = False #to make the loop continuous

#setting the player into true
while player == False: #while loop to start the loop
    player = input("Whats your move " + name + "?: ") #this is the input of the players
    if player == computer: #if the roll is player == computer
        print("Its a tie!")
    elif player == "rock": #for the interaction of the user to the computer and player choses a rock
        if computer == "paper": #this is if the computers rolls for the paper
            print("You lose " + name + "! " + computer + " covers " + player)
        elif computer == "scissors": #this if the computer losses the roll
            print("You win " + name + "! " + player + " smashes the " + computer)
    elif player == "paper":
        if computer == "scissors": #we need to do the losing first inorder for the loop to continue
            print("You lose " + name + "!" + computer + " cut " + player)
        elif computer == "rock":
            print("You win " + name + "! " + player + " covers " + computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose " + name + "! " + computer + " Smashes " + player)
        elif computer == "paper":
            print("You win " + name + "! " + player + " cut " + computer)
    else:
        print("Error please look at your spelling, the first letter should be capital")




