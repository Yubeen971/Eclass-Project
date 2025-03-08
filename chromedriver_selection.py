import os
import platform 
import sys
import subprocess

def chromeselect() -> str:
    match platform.architecture()[0]:
        case "32bit":
           print("Bruh who even supports 32bit? Its 2025 for flips sake!")
           sys.exit()
        case "64bit":
           match platform.machine():
               case "arm64":
                   subprocess.Popen(["./chromedriver-mac-arm64/chromedriver"])
                   return "./chromedriver-mac-arm64/chromedriver"
               case "x86_64":
                      match platform.system():
                       case "Linux":
                           subprocess.Popen(["./chromedriver-linux64/chromedriver"])
                           return "./chromedriver-linux64/chromedriver"
                       case "Windows":
                           subprocess.Popen([r".\chromedriver-win64\chromedriver.exe"])
                           return r".\chromedriver-win64\chromedriver.exe"
                       case "Darwin":
                           subprocess.Popen(["./chromedriver-mac-x64/chromedriver"])
                           return "./chromedriver-mac-x64/chromedriver"
                       case "FreeBSD":
                           print("Ah jeez.\n I really wanted to support you. But we just couldn't. Sorry mate.")
                           sys.exit()
                       case _:
                           print("WE. DON'T. SUPPORT. YOU.")
                           sys.exit()
               case _:
                   print("What even are you?")
                   sys.exit()
        case _:
           print("What are you even using? We didn't even program this in!")
           sys.exit()
