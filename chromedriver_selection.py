import os
import platform 
import sys
import subprocess

def chromeselect() -> str:
    match platform.architecture()[0]:
        case "32bit":
           print("This operating system is not supported")
           sys.exit()
        case "64bit":
           match platform.machine():
               case "arm64":
                   subprocess.Popen(["./chromedriver-mac-arm64/chromedriver"])
                   return ("./chromedriver-mac-arm64/chromedriver", True)
               case "x86_64":
                      match platform.system():
                       case "Linux":
                           subprocess.Popen(["./chromedriver-linux64/chromedriver"])
                           return ("./chromedriver-linux64/chromedriver", False)
                       case "Darwin":
                           subprocess.Popen(["./chromedriver-mac-x64/chromedriver"])
                           return ("./chromedriver-mac-x64/chromedriver", True)
                       case "FreeBSD":
                           print("This operating system is not supported")
                           sys.exit()
                       case _:
                           print("This operating system is not supported")
                           sys.exit()
               case "AMD64":
                    subprocess.Popen([r".\chromedriver-win64\chromedriver.exe"])
                    return (r".\chromedriver-win64\chromedriver.exe", False)
               case _:
                   print("This operating system is not supported")
                   sys.exit()
        case _:
           print("This operating system is not supported")
           sys.exit()
