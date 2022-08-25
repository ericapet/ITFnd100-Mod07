# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickling and Structured Error Handling
# ChangeLog (Who,When,What):
# EricaPeterson,8/23/22,created script to complete assignment 07
# EricaPeterson,8/24/22, Finished script
# ---------------------------------------------------------------------------- #
# Get User Input Data
import pickle
UserMath = []
try:
    f = input("Enter the name of the file you want to make: ")
    if f.isnumeric():
        raise Exception('Please do not use numbers for the file\'s name')
except Exception as e:
    print("There was an error!")
    print(e)
a= "Enter a first number:"
fltN1=input(a)
b="Enter a second number:"
fltN2= input(b)
#Process the Data
try:
    fltsum= float(fltN1) + float(fltN2)
    fltdif= float(fltN1) - float(fltN2)
    fltpro= float(fltN1) * float(fltN2)
    fltquo= float(fltN1) / float(fltN2)
    UserMath = [fltsum,fltdif,fltpro,fltquo]
except ZeroDivisionError as e:
    print("There was an error!")
    print("Please do not put 0 as your second number")
except OverflowError as e:
    print("There was an error!")
    print("Your number was too large, please input a smaller number")
    if fltN1.isalpha() or fltN2.isalpha():
        raise Exception("Do not use characters")
except Exception as e:
    print("There was an error!")
    print("Please do not use characters, only numbers are allowed")
# Functions for Binary Files
def SaveDataToFile(f,UserMath):
    file = open(f,"ab")
    pickle.dump(UserMath,file)
    file.close()
def ReadDataFromFile(f):
    file = open(f, "rb")
    UserMath = pickle.load(file)
    file.close()
    return (UserMath)
# Save Data to Binary File
SaveDataToFile(f,UserMath)
# Unpickle file to read normally for user
print(ReadDataFromFile(f))
input("press 0 to exit program: ")