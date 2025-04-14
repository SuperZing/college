class Team:

    def __init__(self):

        self.name = 'none'

        self.wins = 0

        self.losses = 0

 

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        if (self.wins+self.losses) != 0: #for div error
            return self.wins/(self.wins+self.losses)
        else:
            return 0
   

    # TODO: Define print_standing()
    def print_standing(self):
        win_percent = self.get_win_percentage()
        
        print(f'Win percentage: {win_percent:.2f}')
        if win_percent >= 0.5:
            print(f'Congratulations, Team {self.name} has a winning average!')
        else:
            print(f'Team {self.name} has a losing average.')

 

if __name__ == "__main__":

    team = Team()

    user_name = input()

    user_wins = int(input())

    user_losses = int(input())

    team.name = user_name

    team.wins = user_wins

    team.losses = user_losses

    team.print_standing()
