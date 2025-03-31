import random

print("=================GAME================")
print("MOVES: 0 = 'rock', 1='paper',2='scisors")

def play():
    moves = ['rock','paper','scisors']
    computer_score=0
    player_score=0
    winner=[]
    counter=0
    try:
        while counter < 5:
            computer_move= random.choice(moves)
            print("+++++++++++++++++++++++++++++++++++++++++++++++")
            player_move = moves[int(input("Enter your move\n"))]
            print()
            print("You swang : ", player_move)
            print("Computer swang : ", computer_move)
            print()
                    #GAME LOGIC
            if (computer_move==player_move):
                print("🙂TIE")
            #
            elif (computer_move=='rock') and (player_move=='paper'):
                print("😁Player win!")
                player_score+=1
            elif (computer_move=='rock') and (player_move=='scisors'):
                print("💻Computer win!")
                computer_move+=1
            #
            elif (computer_move=='paper') and (player_move=='scisors'):
                print("😁Player win!")
                player_score+=1
            elif (computer_move=='paper') and (player_move=='rock'):
                print("💻Computer win!")
                computer_score+=1
            #
            elif (computer_move=='scisors') and (player_move=='paper'):
                print("💻Computer win!")
                computer_score+=1
            elif (computer_move=='scisors') and (player_move=='rock'):
                print("😁Player win!")
                player_score+=1
            #
            counter+=1
    except IndexError:
        print("invalid input")
    
    #game results board
    print()
    print("GAME RESULTS BEST OF FIVE")
    print("Player score", player_score)
    print("Computer score", computer_score)
    if player_score>computer_score:
        print("WINNER : PLAYER")
    elif player_score<computer_score:
        print("WINNER : COMPUTER")
    else:
        print("TIE ROUND")



play()