import os
import sys
import json
import uuid
import google.generativeai as genai
from my_key import key
from random import randint
import prompts


###### Google Ai ########
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")
def chat_with_genai(prompt):
    response = model.generate_content(prompt)
    print(response.text)
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
        with open(dir_path+'\\'+folder+'\\'+file, 'w') as f:
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

###############

### vars ###

#npc cvs

#monster cvs

#locations cvs

#relations cvs #{friend:bob, bob1, bob3}


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



def save_npc_to_file(npc_details, folder='npc_file'):

    _folder_check(folder) #should replace this with create_file() eventually




def generate_player(name=None, race=None, char_class=None, background=None):
    pass

#going to need stats
def generate_npc(name=None, race=None, char_class=None, background=None, class_level=None, sub_class=None, spells=None):#could make buttons that change a if statment parameter to add levels of creatvity
    #Prompt 
    prompt = "Create a detailed description of a of a Dungeons & Dragons NPC with the following details: " #In cvs format
    prompt += "Give the NPC a Name, Race, Class, Background, and include appearance, personality, notable items if any, a backstory, and motivations."

    #Get the NPC details from AI
    chat_with_genai(prompt)




###### MAIN PROGRAM #######
#def main():
#    generate_npc()

#main()

#generate_npc()