# coding: utf8
from datetime import timedelta, datetime
import time
# pour s'assurer que le \# ne sois pas prit
intervalle = 89
ascii_number_diese = 35
def simple_encryption(key,string):
    print("Clé : \"{}\" \n et la string : \"{}\"".format(key,string))
    keyLenght = len(key)-1
    keyCount = 0
    encryptionList = []
    for x in range(0,len(string)):
        #print("\n--------------------------------\n")
        #print("\nLa String à être convertie {} \nLa clé qui sert a convertire {} \n".format(string[x],key[keyCount]))
        #print("\nString : {0} \nKey Ordonnance: {1}\n".format(ord(string[x]),ord(key[keyCount])))
        encryp = ord(string[x])+ ord(key[keyCount])
        #print("Numbers : " + str(encryp))
        encryp = check_intervalle(encryp)
        encryptionList.append(chr(encryp))
        #print("Apres l\'intervalle : "+ str(encryp))
        if(keyCount >= keyLenght):
            keyCount = 0
        else:
            keyCount+=1
    return ''.join(encryptionList)

def encryption(key,string):
    print("Clé : \"{}\" \net la string : \"{}\"".format(key,string))
    timestamp1 = int(time.time())
    stringTimeStamp = "#"+str(timestamp1)
    # Convertion du temps en Epoch (Seconde) dans un format pour les humains
    # convert = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp1))
    # Duree en seconde 3600 = 1 heures
    duree = 3600
    stringDuree = "#"+str(duree)
    string = string+stringTimeStamp+stringDuree
    keyLenght = len(key)-1
    keyCount = 0
    encryptionList = []
    for x in range(0,len(string)):
        #print("\n--------------------------------\n")
        #print("\nLa String à être convertie {} \nLa clé qui sert a convertire {} \n".format(string[x],key[keyCount]))
        #print("\nString : {0} \nKey Ordonnance: {1}\n".format(ord(string[x]),ord(key[keyCount])))
        encryp = ord(string[x])+ ord(key[keyCount])
        #print("Numbers : " + str(encryp))
        encryp = check_intervalle(encryp)
        encryptionList.append(chr(encryp))
        #print("Apres l\'intervalle : "+ str(encryp))
        if(keyCount >= keyLenght):
            keyCount = 0
        else:
            keyCount+=1
    return ''.join(encryptionList)
def valid_carac(string):
    pass
def check_intervalle(entier):
    # Regarde si l'entier est plus grand que l'intervalle
    if(entier > 122):
        while(entier > 122):
            total = entier - 122
            entier = total + 33
        return entier
    else:
        return entier

def check_intervalle_minimum(entier):
    # Regarde si la String est plus petite que 33
    if(entier < 33):
        while(entier < 33):
            total = 33 - entier
            entier = 122-total
        return entier
    else:
        return entier

def decryption(key,string):
    print("Clé : \"{}\" \net la string : \"{}\"".format(key,string))
    keyLenght = len(key)-1
    keyCount = 0
    decryptionList = []
    for x in range(0,len(string)):
        print("\n--------------------------------\n")
        print("\nLa String à être convertie {} \nLa clé qui sert a convertire {} \n".format(string[x],key[keyCount]))
        print("\nString : {0} \nKey Ordonnance: {1}\n".format(ord(string[x]),ord(key[keyCount])))
        decrypt = ord(string[x])-ord(key[keyCount])
        decrypt = check_intervalle_minimum(decrypt)
        print("Numbers : " + str(decrypt))
        decryptionList.append(chr(decrypt))
        print("Apres l\'intervalle : "+ str(decrypt))
        if(keyCount>= keyLenght):
            keyCount = 0
        else:
            keyCount+=1
    return ''.join(decryptionList)

def fileToDict(files):
    newDict = {}
    with open(str(files),'r') as f:
        for line in f:
            splitline = line.split()
            newDict[splitline[0]] ="".join(splitline[1:])

    return newDict

def normalizeString(string):
    if "#" in string:
        newString = string[1:]
        return newString
    else:
        return string
"""

encryptTGT = encryption("123456789","daehli#1.1.1.127#TGS1")

print("Encryption avec la cle tgt {}\n".format(encryptTGT))

encryptClieny = simple_encryption("987654321",encryptTGT)

print("Encryption avec la cle client {} \n".format(encryptClieny))
"""
decryptclient = decryption("8r$iqp!.Q","Cz0x+\'D_&iGU>IIXQNi<UDOPT`1nJT3KMQ^")

print("Decryption avec la cle client {}\n".format(decryptclient))

#decryptTgt = decryption("ab5utiqp",decryptclient)

#print("Decryption avec la cle TGt {}\n".format(decryptTgt))

#"""
