#!python3
intromsg = '''
Copyright (C) 2022-(present) CalcScript Authors.
CalcScript is a programming language based on Python and calculation.
Much will be introduced in later versions of CalcScript.
'''
print(intromsg)
cmdlist = ["help","add","mult","sub","div"] # How CalcScript's command list works
interpreter = "CALCSCRIPT>"
def getc():
  cmd = input(interpreter)
  if cmd in cmdlist:
    runCmd(cmd)
   else:
    raise CommandError("Not a command.")
