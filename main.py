from subprocess import call
admin_password = "MidRosNot"
def open_py_file():
    call (["python", "gui.py"])

#Welcomes the user
print("Welcome to Flumbo Docs\nEnter admin password\n\nHint first 3 letters of your dogs and cats names\n")
pass_enter = input("Admin Password ")
if pass_enter == admin_password:
    print("Password correct")
    open_py_file()
else:
    print("Try again")
    #Welcomes the user
    print("Welcome to FloppaThon\nEnter admin password\n\nHint first 3 letters of your dogs and cats names\n")
    #Gives User a hint
    pass_enter = input("Admin Password ")
    if pass_enter == admin_password:
        print("Password correct")
        open_py_file()
    else:
        print("Try again")
        #Welcomes the user
        print("Welcome to FloppaThon\nEnter admin password\n\nHint first 3 letters of your dogs and cats names\n")
        #Gives User a hint
        pass_enter = input("Admin Password")
        if pass_enter == admin_password:
            print("Password correct")
            open_py_file()
        else:
            print("Restart and try again")
