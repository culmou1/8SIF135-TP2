import argparse
import re
parser = argparse.ArgumentParser()

# Ajout des arguments
parser.add_argument("-as","--authentification",type=str)
parser.add_argument("-tgt","--ticket-granting-service",type=str)
args = parser.parse_args()
print(args.authentification)
string = args.authentification
# Construction d'un regex divise en 7 groupes 1: ID client 2: AC avec le \# 3: Juste le\ # du AC
# 4: Juste AC 5: TGS avec le \# 6: Juste \# du TGS 7: Juste le Tgs  
matchGroupRegex = re.search("(.+?(?=#))((#)(.+?(?=#)))((#)(.*))",string)
identificationClient = matchGroupRegex.group(1)
adresseClient = matchGroupRegex.group(4)
tgs = matchGroupRegex.group(7)
print(identificationClient)
print(adresseClient)
print(tgs)
