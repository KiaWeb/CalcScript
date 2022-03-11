import os
import platform
welcomemsg = '''
Copyright (C) 2022-(present) CalcScript Authors.
CalcScript is a programming language based on Python and calculation.
Much will be introduced in later versions of CalcScript.
You are in the EVAL interpreter, meaning you can run Python commands.
'''
exitypes = ["exit","exit()"]
clrtypes = ["clr","cls","clear"]
def lClear():
    os.system("clear")

def wClear():
    os.system("cls")

print(welcomemsg)
interpreter = "EVAL>"
def runCmd(command):
    if command in exitypes:
        import index
    elif command in clrtypes:
        if platform.system() == "Linux" or platform.system() == "Darwin":
            lClear()
        else:
            wClear()
    else:
        try:
            command = compile(command,"COMPILED","exec")
            exec(command)
        except Exception as e:
            print(e)
            getc()

def getc():
    cmd = input(interpreter)
    runCmd(cmd)
    getc()

getc()