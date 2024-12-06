### SYSC 4810 - Assignment 1 - justInvest app

#### Author: Jason Zhang
#### Student Number: 101191526

##### Language / Tools/ Dependencies
- Python3: 3.11.0 (Python >3.10.0 should work)
- bcrypt

##### HOW TO RUN
1. After downloading the zipped source code labelled "SYSC-4810-Assignment1.zip", unzip the folder
2. Open a terminal and verify the tools and dependencies are installed with the correct version
3. Type "python3 --version" to verify that python3 is installed
4. Optional: if bcrypt is not found, install bcrypt by typing "pip3 install bcrypt" in the terminal
5. Locate to the path of the unzipped folder in the terminal
6. Run the command "python3 main.py" to run the program
7. Run the command "python3 -m unittest discover -s tests -p "*_test.py" -v" to run all the tests at Once, or
    run each individual test using the command ex: "python3 -m unittest -v test_module/problem1_test.py"

#### justInvest app
This app will be displayed as a CLI interface, displaying the app homepage as well as all the possible operations
The user may decide to Login, register, or Quit depending on the command they select (A, B, C). Upon selecting Login,
and given valid credentials, the User will be granted access into the system, and have all their avaiable operations, 
in which they can perform. Once they want to exit, they can logout using the "X" button. Upon selecting the Register option, 
Users will be prompted to create a username, and secure password based off the system criteria, and a role in which they represent.
This system assumes that the role is their valid role without any external security mechanism. Users will be prompted 3 consecutive
registration attempts, in which if they fail, they will be prompted back to the home page, where they can select their desired option again.
Once registered successfully, the user credentials are added to the password file, and can login to perform their operations. If the User
decides to Quit the program, the program will exit.