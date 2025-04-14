import os
import sys
#import json
import google.generativeai as genai
from my_key import key
#from random import randint
#import prompts

#I think max token size is 2 1/5 books or 388k words



#if text in file reaches token limit or before my word in the ai, have it summaries and condense to its purest elemetn/form (check reddit) and add the non condesnes part to a backup file or logs with a data -------data here, 


###### Google Ai ########
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")
def chat_with_genai(prompt):
    response = model.generate_content(prompt)
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

    #folder check func here
    _folder_check(folder)

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

def _write_to_file(folder, file, prompt): #write data to file by append
    try:
        with open(dir_path+'\\'+folder+'\\'+file, 'a') as f:
            f.write(prompt)
    except (FileNotFoundError, PermissionError, OSError) as e:
        sys.exit(f"Error {e}, happen when writing data to file:{file}, program has stopped.")

def _read_file(folder, file): #read file data and returns it as text ""
    try:
        with open(dir_path+'\\'+folder+'\\'+file, 'r') as f:
            file_data = f.read()
        if not file_data: #if file empty
            #raise ValueError()
            file_data = '' #returns empty text
        return file_data
    except ValueError:
        sys.exit(f"Error ValueError, file:{file} is empty")
    except (FileNotFoundError, PermissionError, OSError) as e:
        sys.exit(f"Error {e}, happen when getting data from file:{file}, program has stopped.")


### Token Functions
def print_token_info(model="gemini-1.5-flash"): #prints token info of model
    #get token information for model
    model_info = genai.get_model("models/"+model)
    print(f"Input Token Limit: {model_info.input_token_limit=}")
    print(f"Output Token Limit: {model_info.output_token_limit=}")

def token_count(prompt, model="gemini-1.5-flash"): #use it as a number #can be use to limit prompt text amount #link https://ai.google.dev/gemini-api/docs/tokens?lang=python
    #get number of tokens
    model = genai.GenerativeModel("models/"+model)
    print(f"Prompt Tokens: {model.count_tokens(prompt)}")

    #print(f"Prompt Tokens: {model.count_tokens(prompt)}, Output Tokens: ") #candidates_token_count
    #print(f"Total Tokens: ")
    pass

def is_token_limit_passed(prompt, model="gemini-1.5-flash"):
    #return a boolean
    #get token limit information for model
    model_info = genai.get_model("models/"+model)
    token_limit = int(model_info.input_token_limit)

    model_info = genai.GenerativeModel("models/"+model)
    current_tokens = str(model_info.count_tokens(prompt))

    nums = ''
    for char in current_tokens:  #total_tokens: 2 >= 10000000 #remove words and keep numbers
        if char.isdigit():
            nums+=char
    current_tokens = int(nums)

    if current_tokens >= token_limit:
        return True
    else:
       return False


##################################



def get_npc_info(): #not done or worked on

    #code to get the info from jason

    ##json to prompt
    #main
    name = "<Name>"
    race = "<Race>"
    npc_class = "<Class>"
    gender = "<Gender>"
    alignment = "<Alignment>"
    stats = {"strength": 0,"dexterity": 0,"constitution": 0,"intelligence": 0,"wisdom": 0,"charisma": 0}
    #attributes
    level = level
    skills = []
    #saving_throws = [] #should I only have this for player
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
    attacks = [] #need to fix this #maybe it could be find all I need is the info and the ai does its thing
    languages = []
    motivation = "<Motivations>"
    fear = "<Fears>"
    alive = True


    prompt = f"""
    Name: {name}
    - Race: {race}
    - Class: {npc_class}
    - Gender: {gender}
    - Alignment: {alignment}
    - Stats: {stats}
    - Level: {level}
    - Skills: {skills}
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
    pass #from the npc file print each character



###############

### vars ###

#monster json #do I really need this, maybe not, or maybe for monsters that are still part of the story

#locations json #for sure need this {name: "text info and summaries of the location"}

#shops #will probly need a shop json of diffrent rating to buy items


### for var I dont think I need location or make a function that gets locations from a genai prompt and builds up on it, like for example "search throughotu this text and get information on locations thier names and what they contain"
#shop should be added along with npcs but not sure yet
#dont need relations I think
#maybe get monsters from a json file or build a function that has a math file that calculates hp and attacks stuff like that                               


######## Program Itself ########

def setup():
    #crate story setup (I can use that file or ask chatgpt to imporce on it)
    
    #get npcs (from file)
    get_npcs_data()

    #add those two to the hostry or whatever file it is called
    #use this as history

    #dont need this part for setup I think
    #if history is 1000 tokens (func to check amount of words or sttring whatever are tokens) I have the func now is_token_limit_passed()
    
    
    ####Summaries I think
    #get text and put it into a backup file with a data log_34343
    #summaries as much as possible the file and put it into the orginal file/text, but before that put in the npc info first (or get it instead like when program loads)
    pass


### def to write summary to file (rember to sumarize the info to save data space/ and maybe hace a normal one as option)
def summaries_prompt(prompt): #idk like I need npc and background and player, maybe like a format that gets edited for npc and player with story info in the bottom like cvs
    pass #maybe summaries importnatn key events from the story/background of the whole sesion


#get npcs, shops, and summary from last file (dont try to sumaries summary, maybe add it as it's on file), move old log file to logs_data in old folder and create new log with all the info gotten

def get_npcs_data(folder='npcs', npc_file='npc_data.txt'): #code to get npcs data from npc file
    return _read_file(folder, npc_file)





######## work in progress

def npc_talk(npc_list, prompt=None): #code to add npc respons to a chat log file #not done yet
    npc_responses = []
    for npc in npc_list: #(one at a time)
        current_npc = f"{npc['Name']} ({npc['Class']}): {npc['Motivation']}"
        npc_response = chat_with_genai(f"Scenario:{prompt}\n") #not sure how to do this part #Would {npc['name']} say or do anything?
        npc_responses.append(f"{npc['Name']}: {npc_response}")
    

    for npc in npc_list: #(all together) #idk anymore
        current_npc = f"{npc['Name']} ({npc['Class']}): {npc['Motivation']}"
        npc_response = chat_with_genai(f"Scenario:{prompt}\n")
        npc_responses.append(f"{npc['Name']}: {npc_response}")

def npc_exist(npc_name, json_data): #return true or false
    return any(npc_dict["name"] == npc_name for npc_dict in json_data)

#def npc_talking(): #advance code to have them talking together
#    pass

def story(folder='logs',file='story_log.txt', prompt=None): #maybe get the dm setup here or have another google genai thing #have story guide in begging for reforcement

    if prompt == None:
        return

    #get history
    history = _read_file(folder, file)
    
    #use genai
    if history == "":
        prompt_results = chat_with_genai(f"User Prompt:{prompt}")
    else:
        prompt_results = chat_with_genai(f"Background Info:{history}\nUser Prompt:{prompt}")

    #write user prompt to story_log.txt file
    _write_to_file(folder, file, f"User Prompt: {prompt}\n")
    #write to story_log.txt file
    _write_to_file(folder, file, f"AI Output: {prompt_results}")

    #print out results
    print(prompt_results)


def generate_npc(folder='npcs', npc_file='npc_data.txt', name=None, race=None, npc_class=None, gender=None, alignment=None, stats=None, level=1):

    #temp_file = 'temp_data.json'

    _file_check(folder, npc_file) #check if folder and file exist
    #_file_check(folder, temp_file) #checks if temp_data file exists, if not then to create it

    history = _read_file(folder, npc_file)

    ##json to prompt
    name = "<Name>"
    race = "<Race>"
    npc_class = "<Class>"
    gender = "<Gender>"
    alignment = "<Alignment>"
    stats = {"strength": 0,"dexterity": 0,"constitution": 0,"intelligence": 0,"wisdom": 0,"charisma": 0}
    #attributes
    level = level
    skills = []
    #saving_throws = [] #should I only have this for player
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
    attacks = [] #need to fix this #maybe it could be find all I need is the info and the ai does its thing
    languages = []
    motivation = "<Motivation>"
    fear = "<Fear>"
    alive = True

    #- Saving Throws: {saving_throws}

    #starts getting iffy in pysical description and attack
    #    Create an NPC with the following details:
    prompt = f"""
    Create an NPC by filling in the following details, without the unnecessary json formatting:
        Name: {name},
        Race: {race},
        Class: {npc_class},
        Gender: {gender},
        Alignment: {alignment},
        Stats: {stats},
        Level: {level},
        Skills: {skills},
        Backstory: {backstory},
        Personality Traits: {personality_traits},
        Size: {size},
        Eye color: {eye_color},
        Hair color: {hair_color},
        Features: {features},
        Equipment: {equipment},
        Gameplay Stats: {{HP: {hp}, AC: {ac}, Speed: {speed}, Attacks: {attacks}}},
        Languages: {languages},
        Motivation: {motivation},
        Fear: {fear},
        Alive: {alive}
    """

    if history == '':
        #generate npc
        npc_results = chat_with_genai(prompt)
    else:
        #generate npc with history
        npc_results = chat_with_genai(f"Background Info:{history}\nUser Prompt:{prompt}")
   

    #add npc to npc_data json file
    #_write_to_file(folder, npc_json_file, '\n{\n'+npc_results+'}') #works if doing json
    _write_to_file(folder, npc_file, '\n'+npc_results+'\n')

    #print npc to cmd
    print(npc_results)



###### MAIN PROGRAM #######
def main():
    generate_npc('npcs', 'npc_data.txt')

#main() #add a while true to keep it running or should I just call the functs with a python gui

####################

#generate_npc(level=5)
#story(prompt='I am good with that')

#chat_with_genai("can you make a dnd adventure") 

