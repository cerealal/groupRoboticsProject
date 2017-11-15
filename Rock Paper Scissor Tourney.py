#The Rock paper scissors game file
playerOneQuery = "Player one please select a move "
playerTwoQuery = "Player two please select a move "
#Queries players are asked before info is stored

def Winner_Calculator(p1Choice,p2Choice):
    if p1Choice == "1" and p2Choice == 1:
        print("It's a Draw...")
            
    elif p1Choice == "1" and p2Choice == 2:
        print("Paper gets cut by Scissors, Player 2 wins!!")
        
    elif p1Choice == "1" and p2Choice == 3:
        print("Paper covers Rock, Player 1 wins!!")            

    elif p1Choice == "2" and p2Choice == 1:
        print("Scissors cut Paper, Player 1 wins!!")            

    elif p1Choice == "2" and p2Choice == 2:
        print("It's a Draw...")

    elif p1Choice == "2" and p2Choice == 3:
        print("Scissors get broken by Rock, Player 2 wins!!")

    elif p1Choice == "3" and p2Choice == 1:
        print("Rock gets covered by Paper, Player 2 wins!!")            

    elif p1Choice == "3" and p2Choice == 2:
        print("Rock breaks Scissors, Player 1 wins!")            

    elif p1Choice == "3" and p2Choice == 3:
        print("It's a Draw...")

    else:
        print("invalid answer")



