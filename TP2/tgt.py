# coding: utf8
import argparse
import re
from utils import fileToDict, decryption,normalizeString,decryption
import sys
parser = argparse.ArgumentParser()

parser.add_argument("-tgt","--ticket-granting-service")
args = parser.parse_args()
print(args)
string = args.ticket_granting_service
print(type(string))
reg = re.findall("(.?.*?(?=#|$))",string)
print(reg)
identificationClient = reg[0]
adresseClient = reg[1]
identificationServeur = reg[2]
identificationServeur = normalizeString(identificationServeur)
ticketTGS = normalizeString(reg[3]) + reg[4]+ reg[5]+ reg[6]+ reg[7]
print(ticketTGS)
dictionnaire = fileToDict("cles.txt")
if(dictionnaire[identificationServeur]!= ""):
    print("Trouver")
else:
    print("Non")
    sys.exit(0)
keyClient = dictionnaire[identificationClient]
print(keyClient)
ticketdecryption = decryption(keyClient,str(ticketTGS))
print(ticketdecryption)
