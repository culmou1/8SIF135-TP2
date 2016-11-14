# coding: utf8
from datetime import timedelta, datetime
import time
# pour s'assurer que le \# ne sois pas prit
intervalle = 89
ascii_number_diese = 35
def simple_encryption(key,string): 
    keyLenght = len(key)-1
    keyCount = 0
    encryptionList = []
    for x in range(0,len(string)):
        if (ord(string[x]) != ascii_number_diese):
            print("String Ordonnance : {0} \n Key Ordonnance: {1} ".format(ord(string[x]),ord(key[keyCount])))
            encryp = ord(string[x])+ ord(key[keyCount])	
            print("Numbers : " + str(encryp))
            encryp = check_intervalle(encryp)
            print("Apres l\'intervalle : "+ str(encryp))
            if(encryp==35):
                encryptionList.append(chr(encryp+1))
            else:
                encryptionList.append(chr(encryp))
            if(keyCount >= keyLenght):
                keyCount = 0
            else:
                keyCount+=1		
        else:
            encryptionList.append(chr(ord(string[x])))
    return ''.join(encryptionList)
    
def encryption(key,string):
    timestamp1 = int(time.time())
    stringTimeStamp = "#"+str(timestamp1)
    print(stringTimeStamp)
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
        if (ord(string[x]) != ascii_number_diese):
            print("String Ordonnance : {0} \n Key Ordonnance: {1} ".format(ord(string[x]),ord(key[keyCount])))
            encryp = ord(string[x])+ ord(key[keyCount])	
            print("Numbers : " + str(encryp))
            encryp = check_intervalle(encryp)
            print("Apres l\'intervalle : "+ str(encryp))
            if(encryp==35):
                encryptionList.append(chr(encryp+1))
            else:
                encryptionList.append(chr(encryp))
            if(keyCount >= keyLenght):
                keyCount = 0
            else:
                keyCount+=1		
        else:
            encryptionList.append(chr(ord(string[x])))
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
    keyLenght = len(key)-1
    keyCount = 0
    decryptionList = []
    for x in range(0,len(string)):
        if(ord(string[x]) != ascii_number_diese):
            decrypt = ord(string[x])-ord(key[keyCount])
            decrypt = check_intervalle_minimum(decrypt)
            if(decrypt==35):
                decryptionList.append(chr(decrypt-1))
            else:
                decryptionList.append(chr(decrypt))
            if(keyCount>= keyLenght):
                keyCount = 0
            else: 
                keyCount+=1 
        else:
            decryptionList.append(chr(ord(string[x])))
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
decrypt =decryption("123456789","DCt_cV#'$rh?$'w,#I.<>#&)\"-$xqM-&#v)$n")
print(decrypt)
print(type(decrypt))
