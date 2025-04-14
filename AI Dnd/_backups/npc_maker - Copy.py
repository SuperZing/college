import os
import google.
#from openai import OpenAI
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






def generate_player(name=None, race=None, char_class=None, background=None):
    pass

def generate_npc(name=None, race=None, char_class=None, background=None):#could make buttons that change a if statment parameter to add levels of creatvity
    #Prompt 
    prompt = "Create a detailed description of a of a Dungeons & Dragons NPC with the following details: "
    prompt += "Give the NPC a Name, Race, Class, Background, and include appearance, personality, notable items if any, a backstory, and motivations."

    #Get the NPC details from ChatGPT
    npc_details = chat_with_gpt(prompt)
    print(npc_details)
    #return npc_details


####### OS/Local ######

#current path of file
dir_path = os.path.dirname(os.path.realpath(__file__))

def _directory_check(directory): #name of directory is folder name
    #Ensures the directory exists (creates folder)
    if not os.path.exists(dir_path+'\\'+directory):
        os.makedirs(dir_path+'\\'+directory)


def save_npc_to_file(npc_details, directory='npc_file'):

    _directory_check(directory)

    npc_name = 0



###### MAIN PROGRAM #######
def main():
    generate_npc()

main()