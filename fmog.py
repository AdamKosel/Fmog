# This script will take a list of /32 IP addresses and create address objects with the same name.

redc= "\033[1;31m" #Red Color
bluec= "\033[1;36m" #Blue Color
ubluec= "\033[4;34;40m" #Underbline Blue
endc= "\033[0;0m" #End Color

#Address Object Function
def addrobj(a):
    for a in a:
        print(bluec +"edit " + a + endc)
        print("set subnet " + a + "/32")
        print("next")

#Address group function
def addrgrp(a):
    seperator = ", "
    print()
    print (bluec + "append " + endc  + (seperator.join(a)))
    
    
    
print()

print(" "*27 +"__")
print(" "*26 +"/ _|")
print(" "*25 +"| |_   _ __ ___" + " "*14 +"__ _")
print(" "*25 +"|  _| | '_ ` _ \    "+ redc +"_/_/_/"+ endc +"  / _` |")
print(" "*25 +"| |   | | | | | |  "+ redc +"_/  _/"+ endc +"  | (_| |")
print(" "*25 +"|_|   |_| |_| |_| "+ redc +"_/_/_/"+ endc +"    \__, |")
print(" "*53 +"__/ /")
print(" "*52 +"|___/")
print(redc +"                       Fortinet Mass Address Object Generator" + endc)
print("                              -Written by Adam Kosel")
print()
print("-This script will take a list of IP addresses and create address objects with the same name.")
print("-It will also add them to a group using the append function.")
print()
print("Enter list of IPs followed by a blank carriage return (aka hit the ENTER key when done).")
print()





#Input IP addresses and add to list
a = []
prompt = "Enter an IP: "
line = input(prompt)
while line:
   a.append(str(line))
   line = input(prompt)


print()
print()
print()
print()

## Address Object config output
print(ubluec + "<<<<<<<<  COPY to create address objects  >>>>>>>>"+ endc)
print()
print("conf firewall address")
addrobj(a)
print("end")
print()

## Address Group config output
print(ubluec + "<<<<<<<<  COPY to add to an address group  >>>>>>>"+ endc)
addrgrp(a)
print("next")
print("end")
