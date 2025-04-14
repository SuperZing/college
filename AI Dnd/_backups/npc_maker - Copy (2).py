import os
import google.generativeai as genai
import prompts 
from random import randint
from my_key import key
 
###### AI/Chatgpt ######
#Key
#client = OpenAI(api_key=key)
#ai_role = 'system' #Dnd dugenon master/Dnd tabletop dm

#Ai-prompt 
#def chat_with_gpt(prompt):
#    response = client.chat.completions.create(
#    model="gpt-3.5-turbo",
#    messages=[
#        {"role": ai_role, "content": "hello"},
#        {"role": "user", "content": prompt}])
#    return response.choices[0].message.content
##########################

###### Google Ai ########
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")
def _chat_with_genai(prompt):
    response = model.generate_content(prompt)
    #return response.text
    print(response.text)
#########################



####### OS/Local ###### (and helper functions)

#current path of file
dir_path = os.path.dirname(os.path.realpath(__file__))

def _directory_check(directory): #name of directory is folder name (check if directory exist)
    #Ensures the directory exists (creates folder)
    if not os.path.exists(dir_path+'\\'+directory):
        os.makedirs(dir_path+'\\'+directory)


###def to create foilder by name of var
def _create_directory(directory):
    pass

### def to write summary to file (rember to sumarize the info to save data space/ and maybe hace a normal one as option)
def _summaries_prompt(prompt): #idk like I need npc and background and player, maybe like a format that gets edited for npc and player with story info in the bottom like cvs
    pass


###def to write into to file
def _write_file(file): #would be hard like summaries prompt
    pass

###def to get contents of a file as a prompt
def _read_file(file): #file path should be inside
    pass


### Program Itself ###

def dice_roll(dice_num): #for dices
    return randint(1,dice_num)


#vars

#npc cvs

#monster cvs

#locations cvs

#relations cvs #{friend:bob, bob1, bob3}



def save_npc_to_file(npc_details, directory='npc_file'):

    _directory_check(directory)




def generate_player(name=None, race=None, char_class=None, background=None):
    pass

#going to need stats
def generate_npc(name=None, race=None, char_class=None, background=None, class_level=None, sub_class=None, spells=None):#could make buttons that change a if statment parameter to add levels of creatvity
    #Prompt 
    prompt = "Create a detailed description of a of a Dungeons & Dragons NPC with the following details: " #In cvs format
    prompt += "Give the NPC a Name, Race, Class, Background, and include appearance, personality, notable items if any, a backstory, and motivations."

    #Get the NPC details from AI
    #npc_details = chat_with_gpt(prompt)
    print(npc_details)
    #return npc_details




###### MAIN PROGRAM #######
#def main():
#    generate_npc()

#main()