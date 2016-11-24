# coding: utf8
import argparse
import re
from utils import fileToDict, decryption,normalizeString,encryption
import sys
import time
parser = argparse.ArgumentParser()
parser.add_argument("-serveur","--serveur")
args = parser.parse_args()
print(args)
string = args.serveur
reg = re.findall("(.?.*?(?=#|$))",string)
identificationClient = reg[0]
adresseClient = reg[1]
identificationServeur = reg[2]
identificationServeur = normalizeString(identificationServeur)
ticketServeur = ''.join(reg[3:])
ticketServeur = normalizeString(ticketServeur)
print("Ticket TGS \"{}\"\n".format(ticketServeur))
dictionnaire = fileToDict("cles.txt")
if(dictionnaire[identificationServeur]!= ""):
    print("Trouver")
else:
    print("Non")
    sys.exit(0)
keyServeur = dictionnaire[identificationServeur]
ticketdecryption = decryption(keyServeur,ticketServeur)
print("Clé Serveur {}\n".format(keyServeur))
print("Premiere Decryption avec la cle Serveur {} \n".format(ticketdecryption))

#Cle du Serveur

reg = re.findall("(.?.*?(?=#|$))",ticketdecryption)
print("Ticket Decryption : {}\n".format(reg))
timestampTGS = reg[3]
dureeTGS = reg[4]
timestampTGS = normalizeString(timestampTGS)
dureeTGS = normalizeString(dureeTGS)
print("Le timeStamp {} et la duree {} \n".format(timestampTGS,dureeTGS))

now = time.time()
session = float(timestampTGS)+float(dureeTGS)

print("Now : {} Session : {} \n".format(now,session))

if(float(session) < now):
    print("Le ticket est expire\n")
    sys.exit(0)
else:
    identificationServeurTicket = reg[1]

    print("Identification Client Normal {}\nIdentification Client Ticket {}\n".format(adresseClient,identificationServeurTicket))
    if(identificationServeurTicket == adresseClient):
        print("OK\n")
    else:
        print("NON\n")
        print("L\'adresse client est différente entre le ticket et l'adresse reçu en ligne de commande\n")
        sys.exit(0)


"Cz0x+'D_&iGU>IIXQNi<UDOPT`0oPX3KMQ^"
