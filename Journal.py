import time
import os
done = False

entries = []

def menu():
    print("Choose an option")
    print("1. Load File")
    print("2. Add Entry")
    print("3. Remove Entry")
    print("4. Save File")
    print("5. View Entries")
    print("6. Exit")
    print(' ')
    print("Choose a number between 1-6: ")
    
def YN(choice):
    while choice != "Y" and choice != "N":
        choice = input("Please enter Y or N: ")   
    return choice

def load(entries):
    entries = []
    file = input("Please enter the file name (leave the .txt for us): ") + ".txt"
    if os.path.exists(file):
        print("Loading file...")
        with open(file, 'r') as fileStuff:
            for line in fileStuff:
                line = line.strip('\n')
                entries.append(line)
        print("File Loaded")
    else:
        choice = input("File does not exist would you like to create it (Y/N): ")
        choice = YN(choice)
        if choice == "Y":
            print("Creating File...")
            open(file, 'a')
            print("File created")
    return entries
            
def add(entries):
    entry = input("Enter your entry: ")
    entries.append(entry)
    print("added your entry to the book")
    return entries

def remove(entries):
    rmv = input("Enter the entry you want to remove: ")
    for x in range(len(entries)-1):
        if entries[x] == rmv:
            entries.pop(x)
    return entries

def save(entries):
    file = input("Please enter the file you want to save it to (leave the .txt for us): ") + ".txt"
    if os.path.exists(file):
        print("Saving to File")
        with open(file, 'w') as file:
            for item in entries:
                file.write(item+ "\n")
        print("Saved to File")
        
    else:
        choice = input("File does not exist would you like to create it (Y/N): ")
        choice = YN(choice)
        if choice == "Y":
            print("Creating File...")
            open(file, 'a')
            print("File created")
            print("Saving to file")
            with open(file, 'w') as file:
                for item in entries:
                    file.write(item+ "\n")
            print("Saved to File")

def view():
    print('')
    for item in entries:
        print(item)
    print('')
    input("Press anything to continue: ")

def xit():
    choice = input("Would you like to exit (Y/N): ")
    choice = YN(choice)
    if choice == "Y":
        return True
    else:
        return False
    



while done == False:
    menu()
    choice = int(input())
    done == True
    if choice == 1:
        entries = load(entries)
    elif choice == 2:
        entries = add(entries)
    elif choice == 3:
        entries = remove(entries)
    elif choice == 4:
        save(entries)
    elif choice == 5:
        view()
    elif choice == 6:
        done = xit()
    else:
        print("Please choose a number 1-6")
    print(entries)
        
