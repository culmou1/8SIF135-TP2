import argparse
import re
from utils import fileToDict,normalizeString,encryption,simple_encryption
parser = argparse.ArgumentParser()

parser.add_argument("-as","--authentification",type=str)
args = parser.parse_args()

# Transforme l'argument en une varible
string = args.authentification

# Retourne toute les matchs de la regex en une liste 
reg = re.findall("(.?.*?(?=#|$))",string)
identificationClient = reg[0] 
adresseClient = reg[1] 
tgs = reg[2] 
dictionnaire = fileToDict("cles.txt")
tgs = normalizeString(tgs)
print(tgs)

# Cle secrete du K TGS
key = dictionnaire[tgs]
tgsEncryption = encryption(key,string)
print("TGS ENCRYPTION \n")
print(tgsEncryption+ "\n")
# Encryption avec la cle du client 
keyClient = dictionnaire[identificationClient]
clientEncryption =simple_encryption(keyClient,tgsEncryption)
print("CLIENT ENCRYPTION \n")
print(clientEncryption+"\n")
