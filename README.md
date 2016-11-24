# 8SIF135-TP2
authentification et gestion des clés

## Dépendance
Vous devez avoir python3 d'installé sur l'ordinateur

## Exemple d'éxécution

### AS

````python

python3 as.py -as daehli#1.1.1.127#TGS1

```

### TGS

```python
python3 tgt.py -tgt daehli#1.1.1.127#V1#TicketTGT

```
### Serveur

```python
python3 serveur.py -serveur daehli#1.1.1.127#V1#TICKETSERVEUR
```


## Information

Nous avons mis une durée de 3600 secondes par sessions

Vous devez faire attention avec les tickets envoyée en paramètre.

Vous devez mettre des `\` devant les `"`,`$`et `'`

### Exemple

```python
"Je suis un \$"

"Je suis un \" dans une string"

"Je suis un \' dans une string"
```
