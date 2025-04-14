import os
import sys
import json
#import uuid
import google.generativeai as genai
from my_key import key
from random import randint
#import prompts






#genai.configure(api_key=key)
#model = genai.GenerativeModel("gemini-1.5-flash")
#def chat_with_genai(prompt, folder, file):
#    history = _read_file(folder, file)
#    history = '['+history+']\n'
#    prompt = history+prompt
#    response = model.generate_content(prompt)
#    print(response.text) #this prints it
#    _write_to_file(folder, file, response.text) #saves it to logs to have chat history, it goes by newlines, should go in the functions not here
#    return response.text




###### Google Ai ########
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")
def chat_with_genai(prompt):
    history = _read_file("chat_logs", "logs.txt")
    history = '['+history+']\n'
    prompt = history+prompt
    response = model.generate_content(prompt)
    print(response.text) #this prints it
    _write_to_file("chat_logs", "logs.txt", response.text) #saves it to logs to have chat history, it goes by newlines, should go in the functions not here
    return response.text
#########################


####### OS/Local ###### (and helper functions)

#current path of file
dir_path = os.path.dirname(os.path.realpath(__file__))

def _folder_check(folder): #name of folder (check if directory exist)

    #folder path
    folder_path = dir_path+'\\'+folder

    #Ensures the directory exists (creates folder)
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    except (OSError, PermissionError) as e:
        sys.exit(f"Error {e}, happen in folder creation for folder_path:{folder_path}, program has stopped.")

#file check
def _file_check(folder, file_name):

    #file path
    file_path = dir_path+'\\'+folder+'\\'+file_name

    #check if file exist in directory
    try:
        if not os.path.exists(file_path): #(maybe create file and write the info to it or just edit background)
            with open(file_path, 'w') as fp:
                pass
    except (OSError, PermissionError) as e:
        sys.exit(f"Error {e}, happen in file creation for file_path:{file_path}, program has stopped.")


###def to create file
def create_file(folder, file_name): #create and save file

    #checks if folder exist in directory
    _folder_check(folder)

    #file path
    file_path = dir_path+'\\'+folder+'\\'+file_name

    #check if file exist in directory
    try:
        if not os.path.exists(file_path): #(maybe create file and write the info to it or just edit background)
            with open(file_path, 'w') as fp:
                pass

        #maybe elif if filename arealdy exist so the filename character name changes (or filename = name_race or name_race_class, something like that or name_id)
    except (OSError, PermissionError) as e:
        sys.exit(f"Error {e}, happen in file creation for file_path:{file_path}, program has stopped.")

###def to write into to file
def _write_to_file(folder, file, prompt): #write data to file     #(works like this chat = chat_with_genai(prompt), _write_file(chat))  (append or erase or copy over, idk)
    try:
        with open(dir_path+'\\'+folder+'\\'+file, 'a') as f:
            f.write(prompt)
    except (FileNotFoundError, PermissionError, OSError) as e:
        sys.exit(f"Error {e}, happen when writing data to file:{file}, program has stopped.")

def _read_file(folder, file): #read file data    #(works like this prompt=_read_file(file) in functions)
    try:
        with open(dir_path+'\\'+folder+'\\'+file, 'r') as f:
            file_data = f.read()
        if not file_data: #if file empty
            raise ValueError()
        return file_data
    except ValueError:
        sys.exit(f"Error ValueError, file:{file} is empty")
    except (FileNotFoundError, PermissionError, OSError) as e:
        sys.exit(f"Error {e}, happen when getting data from file:{file}, program has stopped.")

def modify_data():
    pass

#_write_to_file('npc_file', 'name.txt', chat_with_genai('what is your name'))

### def to write summary to file (rember to sumarize the info to save data space/ and maybe hace a normal one as option)
def summaries_prompt(prompt): #idk like I need npc and background and player, maybe like a format that gets edited for npc and player with story info in the bottom like cvs
    pass #maybe summaries importnatn key events from the story/background of the whole sesion


#get npcs, shops, and summary from last file (dont try to sumaries summary, maybe add it as it's on file), move old log file to logs_data in old folder and create new log with all the info gotten
def contiune():
    pass



###############

### vars ###

#monster json #do I really need this, maybe not, or maybe for monsters that are still part of the story

#locations json #for sure need this {name: "text info and summaries of the location"}

#shops #will probly need a shop json of diffrent rating to buy items

#relations json #{friend:bob, bob1, bob3} (maybe can be added by story file just (add story and npc relationships))


### Dnd Machanics ###
def dice_roll(dice_num): #for dices (if rolling for dices use dice_roll function)
    return randint(1,dice_num)

def roll_stats(): #It's a dictonary right now
    return {'str':randint(8,20),
        'dex':randint(8,20),
        'con':randint(8,20),
        'int':randint(8,20),
        'wis':randint(8,20),
        'cha':randint(8,20)}

######## Program Itself ########

#going to need stats

def npc_exist(npc_name, json_data): #return true or false
    return any(npc_dict["name"] == npc_name for npc_dict in json_data)

def generate_npc(folder, npc_json_file, name=None, race=None, npc_class=None, gender=None, alignment=None, stats=None):

    _folder_check(folder) #check if folder exist
    _file_check(folder, npc_json_file) #check if file exist

    ##json to prompt
    #main
    name = "<Name>" #old one
    race = "<Race>"
    npc_class = "<Class>"
    gender = "<Gender>"
    alignment = "<Alignment>"
    stats = {"strength": 0,"dexterity": 0,"constitution": 0,"intelligence": 0,"wisdom": 0,"charisma": 0}
    #attributes
    skills = []
    saving_throws = []
    backstory = "<Backstory>"
    personality_traits = []
    #aperance 
    height = "<Height ft>"
    weight = "<Weight lb>"
    eye_color = "EyeColor"
    hair_color = "<HairColor>"
    features = []
    equipment = []
    #combat
    hp = 0
    ac = 0
    speed = 0
    attacks = []
    languages = []
    motivations = "<Motivations>"
    fears = "<Fears>"


    prompt = ""

    #generate npc
    npc_results = chat_with_genai(prompt)

    #give npc a id ####maybe remove
    #unique_id = str(uuid.uuid4()) #wonder if I really need this
    #code to add that in the begining

    #while name is in get_names(jsonfile): #for loop this until false
    #    chat_with_genai(f"I already have the name {name}, can you make a new name") (create func to get name vars from json file)

   

    #add npc to json file (use if statment)
    #if not npc_exist(unique_id, npc_json_file):
    #    pass #add npc to json
    ####function to add json to file

    #print npc to cmd
    print(npc_results)



    pass



###### MAIN PROGRAM #######
def main():
    generate_npc('npcs', 'npc_data.json')

#main()


def layout():
    ##json to prompt
    #main
    name = "<Name>"
    race = "<Race>"
    npc_class = "<Class>"
    gender = "<Gender>"
    alignment = "<Alignment>"
    stats = {"strength": 0,"dexterity": 0,"constitution": 0,"intelligence": 0,"wisdom": 0,"charisma": 0}
    #attributes
    skills = []
    saving_throws = [] #should I only have this for player
    backstory = "<Backstory>"
    personality_traits = []
    #aperance 
    size = "<Size>"
    eye_color = "<EyeColor>"
    hair_color = "<HairColor>"
    features = []
    equipment = []
    #combat
    hp = 0
    ac = 0
    speed = 0
    attacks = [] #need to fix this 
    languages = []
    motivation = "<Motivations>"
    fear = "<Fears>"
    alive = True


    #starts getting iffy in pysical description and attack
    prompt = f"""
    Create an NPC with the following details:
    - Name: {name}
    - Race: {race}
    - Class: {npc_class}
    - Gender: {gender}
    - Alignment: {alignment}
    - Stats: {stats}
    - Skills: {skills}
    - Saving Throws: {saving_throws}
    - Backstory: {backstory}
    - Personality Traits: {personality_traits}
    - Physical Description: {size}, {eye_color} eyes, {hair_color} hair, {features}.
    - Equipment: {equipment}
    - Gameplay Stats: HP: {hp}, AC: {ac}, Speed: {speed}, Attacks: {attacks}.
    - Languages: {languages}
    - Motivation: {motivation}
    - Fear: {fear}
    - Alive: {alive}
    """

    chat_with_genai(prompt)

layout()
#chat_with_genai("can you make a dnd adventure")