# coding: utf8
import argparse
import re
from utils import fileToDict, decryption,normalizeString,encryption
import sys
import time
parser = argparse.ArgumentParser()
parser.add_argument("-tgs","--ticket-granting-service")
args = parser.parse_args()
print(args)
string = args.ticket_granting_service
reg = re.findall("(.?.*?(?=#|$))",string)
identificationClient = reg[0]
adresseClient = reg[1]
identificationServeur = reg[2]
identificationServeur = normalizeString(identificationServeur)
ticketTGS = ''.join(reg[3:])
ticketTGS = normalizeString(ticketTGS)
print("Ticket TGS \"{}\"\n".format(ticketTGS))
dictionnaire = fileToDict("cles.txt")
if(dictionnaire[identificationServeur]!= ""):
    print("Trouver")
else:
    print("Non")
    sys.exit(0)
keyClient = dictionnaire[identificationClient]
print("Clé Client {}\n".format(keyClient))
ticketdecryption = decryption(keyClient,ticketTGS)
print("Premiere Decryption avec la cle Client {} \n".format(ticketdecryption))

#Cle du Serveur

ticketdecryption = decryption(dictionnaire["TGS1"],ticketdecryption)
serverKey = dictionnaire[identificationServeur]
print("Deuxieme decryption avec la cle du TGS1 {}\n".format(ticketdecryption))
reg = re.findall("(.?.*?(?=#|$))",ticketdecryption)
print("Ticket Decryption : {}\n".format(reg))
timestampTGS = reg[3]
dureeTGS = reg[4]
timestampTGS = normalizeString(timestampTGS)
dureeTGS = normalizeString(dureeTGS)

# Le message n\'est pas encore crypté
messageNotCrypt = identificationClient + adresseClient + "#"+identificationServeur
# On va chercher les parametres du ticket
print("Le timeStamp {} et la duree {} \n".format(timestampTGS,dureeTGS))

now = time.time()
session = float(timestampTGS)+float(dureeTGS)

print("Now : {} Session : {} \n".format(now,session))

if(float(session) < now):
    print("Le ticket est expire\n")
    sys.exit(0)
else:
    print("Le message n'est pas encore crypter : {0} \n".format(messageNotCrypt))
    identificationClientTicketTGS = reg[1]

    print("Identification Client Normal {}\nIdentification Client Ticket {}\n".format(adresseClient,identificationClientTicketTGS))
    if(identificationClientTicketTGS == adresseClient):
        encryp = encryption(serverKey,messageNotCrypt)
        print("L\'encryption client avec la cle serveur {}\n".format(encryp))
    else:
        print("L\'adresse client est différente entre le ticket et l'adresse reçu en ligne de commande\n")
        sys.exit(0)
