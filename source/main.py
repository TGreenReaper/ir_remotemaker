import colorama
from colorama import Fore
import random

save = True
filename = True
file_name = None

print("--------- IR_Remote File Gen by GREEN REAPER ---------" + Fore.BLUE)
remote_path = input("REMOTE PATH: ")
up = input("Up button:")
down = input("Down button: ")
left = input("Left Button: ")
right = input("Right button: ")
ok = input("Ok button: ")
back = input("Back button: ")
uph = input("Up button when Held: ")
downh = input("Down button when Held: ")
lefth = input("Left button when Held: ")
righth = input("Right button when Held: ")
okh = input("Ok button when held: ")
if(filename == True):
   file_name = input("File Name: " + Fore.RED)
   

outp = "REMOTE: " + remote_path + "\n" + "UP: " + up + "\n" + "DOWN: " + down + "\n" + "LEFT: " + left + "\n" + "RIGHT: " + right + "\n"  + "OK: " + ok + "\n" + "BACK: " + back + "\n" + "UPHOLD: " + uph + "\n" + "DOWNHOLD: " + downh + "\n" + "LEFTHOLD: " + lefth + "\n"  + "RIGHT: " + righth + "\n"  + "OKHOLD: " + okh + "\n" 



def file():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("--------- Your Complete Infrared Remote File ---------" + Fore.GREEN)
    print("\n")
    print("REMOTE: " + remote_path)
    print("UP: " + up)
    print("DOWN: " + down)
    print("LEFT: " + left)
    print("RIGHT: " + right)
    print("OK: " + ok)
    print("BACK: " + back)
    print("UPHOLD:" + uph)
    print("DOWNHOLD:" + downh)
    print("LEFTHOLD:" + lefth)
    print("RIGHTHOLD:" + righth)
    print("OKHOLD:" + okh)
    print("\n\n\n")
    print(Fore.CYAN)
    if(filename == True):
        
        with open("outputs/" + str(file_name), "w") as file:
         file.write(outp)
        print("Saved " + file_name + ".txt to outputs successfully!"   + Fore.GREEN)

    else:
       with open("outputs/output.txt" , "w") as file:
         file.write(outp)
    print("---------Output has been saved to outputs/output.txt---------")

file()





input("EXIT:")





