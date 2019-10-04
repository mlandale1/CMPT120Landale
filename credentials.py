# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Matt Landale
# Created: 2019/10/4

def username():
    first = input("Enter your first name: ").lower()
    last = input("Enter your last name: ").lower()

    return first, last
    
def marist(first,last):
    uname = (first + "." + last)

    return uname

def password():
    passwd = input("Create a new password: ")

    return passwd

def passcheck(passwd):
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    while False:
        if any(passwd == passwd.upper()):
            print("Password must contain one upper or lower")
            passwd = input("Create a new password: ")
        elif any (passwd == passwd.lower()):
            print("Must contain one lower")
            passwd = input("Create a new password: ")
        else:
            break
    return passwd

    
def main():

    first, last = username()
    uname = marist(first, last)
    passwd = password()
    passwd = passcheck(passwd)
    
    print("Account configured. Your new email address is",
    uname + "@marist.edu")

    

main()
