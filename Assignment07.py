# ------------------------------------------------- #
# Title: Assignment 07,
# Description: A simple example of storing data in a binary file for Intro To Python, RRoot
# ChangeLog: (Who, When, What)
# RRoot, ?, Created Script
# Chani,8.22.21,created functions for script
# Chani,8.23.21, created second yes_or_no function
# Chani,8.24.21, edited for spelling and weak warnings
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
file_name = 'AppData.dat'
objFile = ''
lstCustomer = []
ID_num = ""
name = ""

# -----------------------Processing ------------------------------ #
def save_data_to_file(file_name, lstCustomer):
    '''
    Saves string data to a file

    :param file_name: (string) with name of file
    :param list_of_data: (list) with data to save
    :return: nothing
    '''
    objFile = open(file_name, "wb")  #opens and designates 'write-binary'
    pickle.dump(lstCustomer, objFile) #.dump tosses the objects as binary into the file
    objFile.close()  #closing the file is good practice

def read_data_from_file(file_name):
    '''
    Reads data from a text file
    :param file_name: (string) with name of file
    :return: (dictionary) with ID_num and name
    '''
    objFile = open(file_name, "rb")  #opens and designates 'read-binary'
    cust = pickle.load(objFile)  #.load is for text files
    objFile.close()

    return print(cust) #print ID and name in file

def add_ID_to_List(lstCustomer, ID_num, name):
    '''
    Add data to a list of dictionary rows
    :param lstCustomer: (string) with name of list data is being added to
    :param ID_num: (int) with customer's ID number
    :param name: (string) with customer's name
    :return: nothing
    '''
    customer = {"ID_num": str(ID_num).strip(), "Name": str(name).strip()}
    lstCustomer.append(customer)

# ----------------------Presentation --------------------------- #
def input_ID():
    '''
    Get data for dictionary
    :return: (tuple) ID_num, name
    '''
    ID_num = input("What is the customer's ID?: ")  #take ID
    name = input("What is the customer's name?: ")  #take name
    return ID_num, name  #and save them to variables

def yes_or_no(question):
    answer = input(question + "(y/n): ").lower().strip()  #takes the answer to custom question
    print("")
    while not(answer == "y" or answer == "yes" or answer == "yee" or answer == "yess" or answer == "n"
              or answer == "no" or answer == "na" or answer == "nope" or answer == "noo"):
        print("Input yes or no")  #people be clowns
        answer = input(question + "(y/n):").lower().strip()
    if 'y' in answer:
        return True
    else:
        return False

'''
def yes_or_no(question):
    try:
        answer = input(question + "(y/n): ").lower().strip()
 
        if 'y' or 'n' not in answer:
            raise exception ("Answer must be form of yes or no")
        if 'y' in answer:
            return True
        if 'n' in answer:
            return False
    except exception as wrong:
        print("There was a logic error: " + wrong)
'''

# -------------------------Main Body --------------------------------#

try:
    # TODO: Get ID and NAME From user, then store it in a list object
    (ID_num, name) = input_ID()
    add_ID_to_List(lstCustomer, ID_num, name)

    # TODO: store the list object into a binary file
    if yes_or_no("Would you like to save?") is True:
        save_data_to_file(file_name, lstCustomer)

    # TODO: Read the data from the file into a new list object and display the contents
    read_data_from_file(file_name)
except exception as e: print("There was an error. Shutting down the program now :) ")