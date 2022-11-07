#!/usr/bin/python
#-*-coding:utf8-*-

import sys
import os

#Construction de la table utilisée pour le cryptage et décryptage
def table_cesar():
    tab=[]
    for i in range(32,127):
        tab.append(chr(i))

    for i in range(161,256):
        tab.append(chr(i))
    return tab

#elle donne la position de la lettre dans la table prédéfinie table_cesar
def position(tab,x):
    return tab.index(x)

# """ 
#     Décale de n place(s) dans la table cesar 
# """    
def letterShift(letter, n, tab):
    return tab[(position(tab,letter) + n) % 190]

# """ 
#     Décale de n place(s) en arrière dans la table cesar  
# """ 
def letterShiftMoins(letter,n, tab):
    n = n % 190
    return tab[((position(tab,letter) - n) + 190)% 190] 
    

# """ 
#     Crypte un texte avec une clé saisie par l'utilisateur 
# """
def encryptTextKey(text, key):
    tab =table_cesar()
    encryptText = "" 
    
    for i in range(0, len(text)):
        character = text[i]
        
        if character != " ":
            encryptText = encryptText + letterShift(character, key, tab) 
        else:
            encryptText = encryptText + " "
    
    return encryptText + "c" + str(key)


# """ 
#    Décrypte le texte avec la clé saisie par l'utilisateur 
# """    
def decryptTextKey(text, key):
    tab =table_cesar()
    decryptText = ''
    
    for i in range(0, len(text)):
        character = text[i]
        
        if character != " ":
            decryptText = decryptText + letterShiftMoins(character,key,tab)
        else:
            decryptText = decryptText + " "
    
    return decryptText

# """
#     Crypte le contenu d'un fichier texte
# """
def encryptFile(file, key):
    file = open(file, 'r')
    text = file.read()
    file.close()
    encryptFile = encryptTextKey(text, key)
    file = open('texte_crypte', 'w')
    file.write(encryptFile)
    file.close()
   

# """
#     Décrypte le contenu d'un fichier
# """
def decryptFile(file, key):
    file = open(file, 'r')
    encryptText = file.read()
    file.close()
    decryptText = decryptTextKey(encryptText, key)
    file = open('texte_decrypte', 'w')
    file.write(decryptText)
    file.close()

# test
# encryptFile("ces.txt",18)
# decryptFile("texte_crypte",18)


