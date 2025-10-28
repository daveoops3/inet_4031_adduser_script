# INET 4031 Add Users Script and User Lists
## Program Description
This program automates the process of adding users into linux. All the user needs to do is add the information of each user in the create-users.input file. Each line representing a diffrent user. This is much faster than typing each user via the command line. Typically to add a user via the command line the user would do 'addusr', then 'passwd' to set the password, then 'addusr' to add the user to a certain group. All theses commands can be found in the create_user.py file. They are first constructed as a string then saved in the 'cmd' variable, then they are ran through the command line.
## Program User Operation
For this program to work the user will need to create a file with all the user's information they would like to add. Then they will run this file as an input with the executable file in command prompt. 
### Input File Format
The input file will be a .txt file. Each line will represent a seperate user. Each field will be seperated by a ':'. The first field represents the username. The second field represents the password. The third and fourth field represents the last and first name. Finally, the fifth field represents whether the user is in a group. You can put a '-' to represent that the user does not belong in any field. You can also put a '#' if that user should not be added. 
### Command Excution
First you will need to set the file to be executable. To do that you will need to input this command 'chmod +x create-users.py'. This will make the file an executable, then you will enter this command 'sudo ./create-users.py < create-users.input', the 'sudo' will allow this file to be ran with admin rights. We need to be able to do this because the file is adding users to linux. Next the '<' symbol allows us to use this 'create-users.input' file as an input file.
### "Dry Run"
The dry run will allow the user to see if they inputted their information into the create-user.input file correctly without causing error to the system. It will also show the process of how the executable adds to new users to the system without adding new users to the system.
