# Fmog: Fortinet Mass Object Generator

This script will take a list of IP addresses and create address objects with the same name. It will also add them to a group using the append function.

![Alt text](https://i.imgur.com/itXHd3s.png "Fmog")


**Future updates include:**
* error control
* importing address list from a file
* handling CIDR/subnetmask
    - 10/26 Added function to detect if CIDR was specified for non /32 addresses
* formatting object/group names





**Running in Linux:**

-Make it executable 
* chmod +x fmog.py 

-Run from command line
* python3 fmog.py  

**Usage:**

![Alt text](https://i.imgur.com/yoZYNOm.png "Fmog Usage")
