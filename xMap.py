import sys
from os import system, name
from googlesearch import search
import colorama
from colorama import Fore, Back, Style
import crayons
import requests
from bs4 import BeautifulSoup
def example():
    print(Fore.CYAN+"Example:")
    print(Fore.GREEN+"xMap.py --dork UrDorkHere --res 100(uCanChangeThis) --lang en(OrWrite\"all\"ForNothing)")
def usage():
    logo()
    print("""
    --example  :  Look How Its Make
    --help     :  Come This Page
    --dork     :  Set Dork
    --res      :  Set How Many WebSite
    --lang     :  Search SQL In This Lang (write all for nothing)
    --txt      :  Write Founded SQL To txt File
    """)
def logo():

    print(Fore.BLACK +"        Made by KaanKny")
    print(Style.RESET_ALL)
def clear():
   if name == 'nt':
       _ = system('cls')
   else:
       _ = system('clear')

def check(ber):
    founded = 0
    kaan = str(ber)
    notfound = 0
    error1 = 0
    while ber != 0:
        error = "false"
        print(Fore.BLACK + "--------------------------------------------------")
        print(Fore.BLACK+"|"+Fore.YELLOW+"Site: "+Fore.BLUE+""+site[ber-1])
        print(Fore.BLACK + "--------------------------------------------------")
        web = site[ber-1] + "%27"
        try:
            r = requests.get(web)
            source = BeautifulSoup(r.content, "html.parser").text
        except:
            print(Fore.RED+"ERROR")
            error = "true"
            error1 = error1 + 1
        if "error" in source:
            print(Fore.GREEN+"FOUNDED")
            founded = founded+1
            f.write(web+"\n")
        else:
            if error == "false":
                print(Fore.RED+"NOT FOUNDED")
                notfound = notfound + 1
        print(Fore.BLACK + "--------------------------------------------------")
        print("\n\n")
        ber = ber -1
    print("\n\n")
    print(Fore.BLUE+"Total Website  : "+""+Fore.YELLOW+""+kaan)
    print(Fore.BLACK+"----------------------------------------------")
    print(Fore.BLUE+"Total NotFound : "+""+Fore.RED+""+str(notfound))
    print(Fore.BLUE+"Total Error    : "+""+Fore.LIGHTRED_EX+""+str(error1))
    print(Fore.BLUE+"Total Found    : "+""+Fore.GREEN+""+str(founded))
    f.close()

if __name__ == '__main__':
    usage()
    if len(sys.argv) == 7 or len(sys.argv) == 9:
        if (sys.argv[1] == "--dork"):
            dork = sys.argv[2]
            if sys.argv[3] == "--res":
                res = int(sys.argv[4]) - 1
                if sys.argv[5] == "--lang":
                    lang = sys.argv[6]
                    if len(sys.argv) == 9:
                        if sys.argv[7] == "--txt":
                            txt = sys.argv[8]
                            f = open(txt, "a")
                    if lang == "all":
                        clear()
                        logo()
                        print("\n")
                        print(Fore.MAGENTA+"Scarping Link..")
                        print(Fore.LIGHTMAGENTA_EX + "(waiting time may vary depending on the time you enter)")
                        print(Style.RESET_ALL)
                        site = search(dork,int(res))
                        clear()
                        check(len(site))
                    else:
                        clear()
                        logo()
                        print("\n")
                        print(Fore.MAGENTA + "Scarping Link..")
                        print(Fore.LIGHTMAGENTA_EX+"(waiting time may vary depending on the time you enter)")
                        print(Style.RESET_ALL)
                        site = search(dork,int(res),lang=lang)
                        clear()
                        check(len(site))
                else:
                    print(Fore.RED+"U Forget To Set --lang")
            else:
                print(Fore.RED+"U Forget To Set --res")
        else:
            print(Fore.RED+"U Forget To Set --dork")
            print(Fore.BLUE+"Write \"xMap.py --example\" For Look How Its Make")
    elif (len(sys.argv) == 2):

        if sys.argv[1] == "--example":
            example()
        elif sys.argv[1] == "--help":
            usage()
    else:
        print(Fore.RED+"ERROR..!")

