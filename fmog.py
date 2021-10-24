# This script will take a list of /32 IP addresses and create address objects with the same name.

print()

print(" "*27 +"__")
print(" "*26 +"/ _|")
print(" "*25 +"| |_   _ __ ___  		      __ _")
print(" "*25 +"|  _| | '_ ` _ \    \033[1;31m_/_/_/\033[0;0m  / _` |")
print(" "*25 +"| |   | | | | | |  \033[1;31m_/  _/\033[0;0m  | (_| |")
print(" "*25 +"|_|   |_| |_| |_| \033[1;31m_/_/_/\033[0;0m    \__, |")
print(" "*53 +"__/ /")
print(" "*52 +"|___/")
print("\033[1;31m                       Fortinet Mass Address Object Generator \033[0;0m")
print("                              -Written by Adam Kosel")
print()
print("-This script will take a list of IP addresses and create address objects with the same name.")
print("-It will also add them to a group using the append function.")
print()
print("Enter list of IPs followed by a blank carriage return (aka hit the ENTER key when done).")
print()


#Address Object Function
def addrobj(a):
    for a in a:
        print("\033[1;36medit " + a + "\033[0;0m")
        print("set subnet " + a + "/32")
        print("next")

#Address group function
def addrgrp(a):
    seperator = ", "
    print()
    print ("\033[1;36mappend\033[0;0m " + (seperator.join(a)))
   # for a in a:
   #     print("\033[1;36mappend " + a + "\033[0;0m")
  #      print("next")


#Input IP addresses and add to list
a = []
prompt = "Enter an IP: "
line = input(prompt)
while line:
   a.append(str(line))
   line = input(prompt)
   #The above will add strings to a list

print()
print()
print()
print()

## Address Object config output
print("\033[4;34;40m<<<<<<<<  COPY to create address objects  >>>>>>>>\033[0;0m")
print()
print("conf firewall address")
addrobj(a)
print("end")
print()

## Address Group config output
print("\033[4;34;40m<<<<<<<<  COPY to add to an address group  >>>>>>>\033[0;0m")
addrgrp(a)
print("end")


