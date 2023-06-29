import os
from subprocess import call
codeO = "!69!69!"
def open_py_file():
    call(["python", "gui.py"])
print("Unlock\nEnter a unlock code")
pass_enter = input("Code ")
if pass_enter == codeO:
    print("Code correct and how did you get code HACKER")
    os.remove('gui.py')
else:
    print("Please enter a valid code next time")
    open_py_file()

