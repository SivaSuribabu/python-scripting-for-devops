#This script takes input from the user and lists all files in the specified folders.

#Algorithm:
#1. Take input from the user for folder names.
#2. use the for loop 
#3.decide which module to use
#4. print the files in the folder
#5. handle any known errors

import os

folders = input("Enter folder names separated by commas: ").split()
for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f"Error: The folder '{folder}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{folder}'.")
        break
    
    for file in files:
        print(file)

