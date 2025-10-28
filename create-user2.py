#!/usr/bin/python3

# INET4031
# Dave Cornell
# 10/27/2025
# 10/27/2025

#Import os, is so that we can run bash cmds
#Import re, is a libary that gives us functions that allow us to search for things
#Import sys, gives us functions that allows us to maniupulate the OS
import os
import re
import sys


def main():
    for line in sys.stdin:

	#This line is searching for a pound sign in the file. This let's the code know to skip this line in the file
        match = re.match("^#",line)

        #This line of code put's the information in a list so that it can more easily put it in the cmd prompt
        fields = line.strip().split(':')

        #This IF statment is chaecking for if the line has a pound sign or less then 5 fields in the list
        #If the IF statment evalutes as true then it knows it will skip over the line because it will cause a logic error
        #If there is a pound sign then match will = true which will tell the IF statment to skip that line and if the field list has less than five items in it, it will be true too
        #Those prior two lines just checks the code, without the IF statment, the code would not skip those lines of input.
        if match or len(fields) != 5:
            continue

        #Theses lines of code put the data from the field list into variables, which will make it more readable in the code
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #This line gets ride of the ',' if there is more than one group in the input
        groups = fields[4].split(',')

        #This let's the sysadmin know that the code is working and that it's make this specific user
        print("==> Creating account for %s..." % (username))
	#This line is storing the bash command into a variable. The "cmd" variable will contain a bash command that will add this specific user
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

	#The first time I run the code I should check for any bugs, since we are dealing with Bash, we don't want to cause any bugs that will make it harder to remove.
	#Once uncommented, the os.system(cmd) will run what's stored in the cmd variable, which will make a new user with all the info from input file.
        #print cmd
        os.system(cmd)

        #This print statment let's use know that the password is being set for this specific user
        print("==> Setting the password for %s..." % (username))
	#This line is changing what is stored in the cmd variable to a new linux cmd. 'echo' prints to the command line, -n means no extra newline at the end, the -e tells us to interpret escape like charaters like. The '|' command puts in the next command after the first one.Finally the other linux commands sets and confirms the password for the new user.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

	#The first time I run the code I should understand what is happening so that I know when I run it, it won't cause any errors. Once uncommented the os.system(cmd) will add the passwords for the new user.
        #print cmd
        os.system(cmd)

        for group in groups:
            #The if statment is looking for this '-'. This lets the if statement know that the user is not apart of any groups.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()

#Unfortunatly, the dry run does not work, but if it did, it would prompt the user if they would like to enter 'dry-run' mode by entering Y or N
#If dry run mode is turned on it would not run any of the os.cmd commands, it would print what does commands would have ran
#It would also let the user know if any fields were not completed.
#It would also print out a message if a line was skipped.
