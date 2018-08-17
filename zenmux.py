"""
Author : ./Bazengers
Site   : fhxploit.blogspot.com

Thanks to nmap.org
"""

import os

def ban():
    print "o-----------------------------------0"
    print "| === |=== |\  | |\  /| |  | \\  //  |"
    print "|   / |___ | \ | | \/ | |  |  \\//   |"
    print "|  /  |    |  \| |    | |  |  //\\   |"
    print "| === |=== |   | |    |  \/  //  \\  |"
    print "| Author :./Bazengers               |"
    print "o-----------------------------------o"
    print "Optons :                             "
    print " 1. Regular scan"
    print " 2. ping scan"
    print " 3. intense scan"
    print " 4. intense scan plus UDP"
    print " 5. intense scan, all TCP port"
    print " 6. intense scan, no ping"
    print " 7. Quick scan"
    print " 8. Quick scan plus"
    print " 9. Quick traceroute"
    print " 10.Slow comprehensive scan"
    print " 11. Info"
def info():
    print "Zenmux merupakan tool turunan nmap yang memudahkan pengguna dalam scaning port"
    print "perangkat harus terinstall nmap"
    print "Author : ./Bazengers"
    print "contact : fb.com/cyberly.fa"
ban()

opt = raw_input("Masukan opsinya : ")
tar = raw_input("masukan targetnya : ")

if opt == "1" :
    os.system("nmap "+tar)
elif opt == "2" :
    os.system("nmap -sn "+tar)
elif opt == "3" :
    os.system("nmap T4 -A -v "+tar)
elif opt == "4" :
    os.system("nmap -sS -sU T4 -A -v "+tar)
elif opt == "5" :
    os.system("nmap -p 1-65535 -T4 -A -v "+tar)
elif opt == "6" :
    os.system("nmap T4 -A -v -Pn "+tar)
elif opt == "7" :
    os.system("nmap T4 -F "+tar)
elif opt == "7" :
    os.system("nmap -sV -T4 -O -F --version-light "+tar)
elif opt == "8" :
    os.system("nmap -sn --traceroute "+tar)
elif opt == "10" :
    os.system("nmap -sS -sU T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "+tar)
elif opt == "11" :
    info()
else:
    ban()
opt = raw_input("Masukan opsinya : ")
tar = raw_input("masukan targetnya : ")
