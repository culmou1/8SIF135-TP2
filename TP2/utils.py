# pour s'assurer que le \# ne sois pas prit
intervalle = 89
ascii_number_diese = 35

def encryption(key,string):
	keyLenght = len(key)-1
	print(keyLenght)
	keyCount = 0
	encryptionList = []
	for x in range(0,len(string)):
		print("Range :" + str(x))
		if (ord(string[x]) != ascii_number_diese):
			print("KeyCountRange :" +str(keyCount))
			print(string[x])
			print(key[keyCount])
			encryp = ord(string[x])+ ord(key[keyCount])	
			encryp = check_intervalle(encryp)
			encryptionList.append(chr(encryp))
			print(encryptionList)
			if(keyCount >= keyLenght):
				keyCount = 0
			else:
				keyCount+=1		
	
	return encryptionList
def valid_carac(string):
	pass
def check_intervalle(entier):
	# Regarde si l'entier est plus grand que l'intervalle 
	if(entier > 122):
		newEntier = (entier - 89) + 33
		return newEntier
	else: 
		return entier

def check_intervalle_minimum(entier):
    # Regarde si la String est plus petite que 33
    if(entier < 33):
        newEntier = (entier+89) - 33
        return newEntier
    else:
        return entier

def decryption(key,string):
    keyLenght = len(key)-1
    keyCount = 0
    decryptionList = []
    for x in range(0,len(string)):
        if(ord(string[x]) != ascii_number_diese):
            decrypt = ord(string[x])-ord(key[Keycount])
            decrypt = check_intervalle_minimum(decrypt)
            decryptionList.append(chr(decrypt))
            if(keyCount>= keyLenght):
                keyCount = 0
            else: 
                keyCount+=1 
key = "bonjour"
string1 = "daehli#1.1.1.127#1234"
encryption(key,string1)

