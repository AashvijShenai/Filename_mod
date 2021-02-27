import os
import re

APPLY_TO_DIR_FLAG = 0

path = "D:\\Music\\Rammstein"
keys_rem = ["rammstein", "Rammstein", "doh", "ner", "esc"]
keys_space = ["-","_"]

os.chdir(path)

#Modify this function for specific use
def modify(old_file, path):
    new_file = old_file
    for i in keys_rem:
        new_file = new_file.replace(i, "")
    for i in keys_space:
        new_file = new_file.replace(i, " ")

    new_file = " ".join(new_file.strip().capitalize().split())
    
    #print("Old file: ", old_file)
    #print("new file: ", new_file,"\n")
    #t = input("Proceed?")
    return new_file



for (root_path, dirs, files) in os.walk(os.getcwd()):
    #print("1:: ", root_path)
    #print("2:: ", dirs)
    for file in files:
        os.rename(root_path+"\\"+file, root_path+"\\"+modify(file, root_path))