#!python3
intromsg = '''
Copyright (C) 2022-(present) CalcScript Authors.
CalcScript is a programming language based on Python and calculation.
Much will be introduced in later versions of CalcScript.
'''
print(intromsg)
cmdlist = ["help","add","mult","sub","div"] # How CalcScript's command list works
interpreter = "CALCSCRIPT>"
def runCmd(command):
  if command in cmdlist:
    if command == "help":
      import mhelp
    elif command == "add":
      import add
    elif command == "mult":
      import mult
    elif command == "sub":
      import sub
    elif command == "div":
      import div

def getc():
  cmd = input(interpreter)
  if cmd in cmdlist:
    runCmd(cmd)
    getc()
  else:
    raise CommandError("Not a command.")
    getc()
