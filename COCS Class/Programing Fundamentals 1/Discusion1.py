
#Input from player
player = input("Pick One Number: [1]Rock, [2]Paper, [3]Scissor... ")

def start_game(pick): #Game function of paper, rock, scissors

    #check if input can be converted to int, if not quit 
    try: #so it checks if int() works
        int(pick)
    except: #if error quit
        print("I said pick One Number, not spell")
        quit()
    pick = int(pick) #change to int here to pervent ValueError 

    #list with picks form player and computer
    choice = ['Rock','Paper','Scissor','Rock']
    player = choice[pick-1]
    computer = choice[pick]

    #check if pick is 1-3
    if pick<=3 and pick>0:
        #Make sure player always loses
        print(f"{player} loses to {computer}, you lost but keep trying!") 
    else:
        print("I crashed") #if num not 1-3, then crash

start_game(player) #calls function
