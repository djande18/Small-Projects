import os
import openpyxl

# This program accepts text files that contain a list of people assigned to a certain drive. It check all files contained in the same folder that this script is in. 
# The output will be a list of LANIDs and a list of names that can be pasted in an excel file

def LAN_Name(file):
    
    with open(file, 'r') as file:
        
        LANIDs = []
        names = []
        
        for i,line in enumerate(file):
            if i < 5:
                continue
            else:
                space_index = line.find(" ")

                LANID = line[:space_index]

                mfad_index = line.find("mfad")

                name = line[space_index+1:mfad_index]

            LANIDs.append(LANID)
            names.append(name)

    if len(LANIDs) == len(names):
        print("Confirmed")
    else:
        print("Doesn't match up")

    print(f"*******\nLANIDs \n_________\nCount:\n {len(LANIDs)}\n")

    for i in LANIDs:
        print(i)

    print(f"\nNames \n_________\nCount:\n {len(names)}\n")

    for i in names:
        print(i)

current_directory = os.path.dirname(os.path.abspath(__file__))



file_names = os.listdir(current_directory)

for file_name in file_names:
    index = file_name.find(".")
    if file_name[index:] == ".txt":
        print(f"\n{file_name}")
        LAN_Name(file_name)