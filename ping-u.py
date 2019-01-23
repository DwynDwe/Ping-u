import subprocess as sp
import os

print("-----Ping-u-----")
print("Warning! This script must be run under administrator (Windows) to work properly!")

domain = input("Enter domain name (without top-level domain): ")

topDomains = []
exist = []
basicTopDomains = input("Do you want to test basic top-level domains like .com, .org, .cz, etc...? (yes/no):")
if basicTopDomains == "yes" or basicTopDomains == "y":
    sourceBasic = open("basic-domains.txt","r") #opening file with top level domains
    for line in sourceBasic:
        topDomains.append(line)
    sourceBasic.close()

geoTopDomains = input("Do you want to test geo top-level domains like .paris, .asia, .cologne, etc...? (yes/no):")
if geoTopDomains == "yes" or geoTopDomains == "y":
    sourceGeo = open("geo-domains.txt","r") #opening file with geo domains
    for line in sourceGeo:
        topDomains.append(line)
    sourceGeo.close()

extendedTopDomains = input("Do you want to test top-level domains like .click, .eat, .name, etc...? This option will add over 550 top-level domains - it can prolong testing time (yes/no):")
if extendedTopDomains == "yes" or extendedTopDomains == "y":
    sourceExtended = open("extended-domains.txt","r") #opening file with ICANN domains
    for line in sourceExtended:
        topDomains.append(line)
    sourceExtended.close()
topDomains = [n.replace("\n","") for n in topDomains]
listLenght = str(len(topDomains))

counterExisting = counterNonExisting = domainsCounter = howManyExist = 0
print("{} domains will be tested.".format(listLenght))
for i in topDomains:
    domainsCounter += 1
    address = domain + i
    status,result = sp.getstatusoutput("ping -c1 -w2 " + address)
    if status == 0:
        counterExisting += 1
        exist.append(address)
        print("[{}/{}] Website {} EXIST!".format(domainsCounter,listLenght,address))
    else:
        counterNonExisting += 1
        print("[{}/{}] Website {} DOES NOT EXIST!".format(domainsCounter,listLenght,address))
print("The page {} exists in {} variants. {} variants were tested.".format(domain,counterExisting,listLenght))

printExist = input("Do you want to show existing domain variants (yes/no):")
if printExist == "yes" or printExist == "y":
    if not exist:
        print("[!] Don't panic, but no variant exists. Did you run the program as an administrator?")
    else:
        for i in exist:
            howManyExist += 1
            print("[{}] {}".format(howManyExist,i))

exportLogfile = input("Do you want to export txt file with existing tested domains? (yes/no):")
if exportLogfile == "yes" or exportLogfile == "y":
    exportTxt = open("logfile-{}.txt".format(domain),"w")
    for i in exist:
        exportTxt.write(i)
        exportTxt.write("\n")
    exportTxt.close()

topDomains.clear()
exist.clear()
input("Press ENTER to exit")
