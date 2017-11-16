import os

def myfunction(event, context):
  myvar = os.environ['Environment']
  print myvar
