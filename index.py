#!python3
intromsg = '''
Copyright (C) 2022-(present) CalcScript Authors.
CalcScript is a programming language based on Python and calculation.
Much will be introduced in later versions of CalcScript.
'''
print(intromsg)
cmdlist = {"help":"help.py"} # How CalcScript's command list works (Whatever command name, returns module import name.
interpreter = "CalcScript>"
def getc():
  cmd = input(interpreter)
  if cmd in cmdlist:
    
