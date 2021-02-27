import os
import re

#Apply name modifiers to sub directories as well?
APPLY_TO_DIR_FLAG = 1

#Root path
path = "D:\\Music\\Rammstein"
#Keywords to remove from name
keys_rem = ["rammstein", "Rammstein", "doh", "ner", "esc"]
#Keywords to replace with a space
keys_space = ["_","-"]

#Modify this function for specific use
def modify(old_file):
    ext_flag = 1
    #No file extension/directory
    if(old_file.rfind(".") == -1):
        new_file = old_file
        ext_flag = 0
    else:    
        ext = old_file[old_file.rfind("."):len(old_file)]   #Saving file extension separately
        new_file = old_file.replace(ext,"")

    for i in keys_rem:
        new_file = new_file.replace(i, "")
    for i in keys_space:
        new_file = new_file.replace(i, " ")

    #Capitalise the first word and leave the rest as is and trim spaces.
    new_file = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), new_file, 1)
    new_file = " ".join(new_file.strip().split())
    if(ext_flag):
        new_file = new_file + ext

    return new_file

os.chdir(path)

for (root_path, dirs, files) in os.walk(os.getcwd()):
    for file in files:
        os.rename(root_path+"\\"+file, root_path+"\\"+modify(file))

if(APPLY_TO_DIR_FLAG):
    for (root_path, dirs, files) in os.walk(os.getcwd()):
        for dire in dirs:
            os.rename(root_path+"\\"+dire, root_path+"\\"+modify(dire))