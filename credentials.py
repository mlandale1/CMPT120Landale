# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Matt Landale
# Created: 2019/10/4

def main():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    uname = first + "." + last

    passwd = input("Create a new password: ")
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
        

    print("Account configured. Your new email address is",
    uname + "@marist.edu")

main()





