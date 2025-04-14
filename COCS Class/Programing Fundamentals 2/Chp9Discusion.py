import random #need for stats

class Npc:
    
    def __init__(self, name, race, npc_class, level=1): #constructor
        self.name = name.capitalize()
        self.race = race.capitalize()
        self.npc_class = npc_class.capitalize()
        self.level = int(level)

        self.stats = self._roll_stats() #dict method
    
    def _roll_stats(self): #getting stats by random, also a hidden method
        return {'str':random.randint(3,18),
        'dex':random.randint(3,18),
        'con':random.randint(3,18),
        'int':random.randint(3,18),
        'wis':random.randint(3,18),
        'cha':random.randint(3,18)}
    
    def re_roll_stats(self): #incase I want to re-roll stats
        self.stats = self._roll_stats()

    def __str__(self): #print() special method
        return f"{self.name} is a {self.race} that's a level-{self.level} {self.npc_class}.\n"
    
    def change_name(self, new_name): #edit name
        self.name = new_name
    
    def change_class(self, new_class): #edit class
        self.npc_class = new_class
    
    def level_up(self, new_level): #change level to a higher number
        if new_level > self.level:
            self.level = new_level
    
    def _print_stats(self): #hidden method to print stats
        print("---Stats---")
        for score in self.stats:
            print(f'{score}:{self.stats[score]}')
    
    def character_sheet(self): #prints all the info
        print(f"Name: {self.name}, Race: {self.race}, Class: {self.npc_class}, Level: {self.level}")
        self._print_stats()

#example code
bob = Npc('bob', 'human', 'wizard') #bob instance
print(bob) #print special method
bob.re_roll_stats() #re-roll stats
bob.character_sheet() #get all npc info