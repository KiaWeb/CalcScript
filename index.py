#!python3
import os
import platform
intromsg = '''
Copyright (C) 2022-(present) CalcScript Authors.
CalcScript is a programming language based on Python and calculation.
Much will be introduced in later versions of CalcScript.
'''
print(intromsg)
exitypes = ["exit","exit()"]
clstypes = ["cls", "clear", "clr"]
cmdlist = ["help","eval", "cls", "clear", "clr","exit","exit()", "pip"] # How CalcScript's command list works
interpreter = "CALCSCRIPT>"
def lClear():
  os.system("clear")
  getc()

def wClear():
  os.system("cls")
  getc()

def runCmd(command):
  command = command.lower()
  if command in cmdlist:
    if command == "eval":
      import eval
    elif command == "help":
      import mhelp
    elif command in clstypes:
      if platform.system() == "Linux" or platform.system() == "Darwin":
        lClear()
      else:
        wClear()
    elif command in exitypes:
      exit()
    elif command == "pip":
      import pipi



def getc():
  cmd = input(interpreter)
  if cmd in cmdlist:
    runCmd(cmd)
    getc()
  else:
    print("Not a command.")
    getc()

getc()