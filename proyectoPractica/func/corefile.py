import os
import json

MY_DATABASE=''

def newFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def addData(*param):
    if len(param) > 1:
        json.dump(param[])