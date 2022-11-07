import math
def chiffrementAffine(a,b,L):
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if ( L in alphabet): 
        x=alphabet.index(L)
        y=(a*x+b)%26
        if x>25:
            if y<26:
                y=y+26
        return alphabet[y]
    else :
        return  chr(ord(L)-1)
        
# Calcul de l'inverse d'un nombre modulo 26
def inverse(a):
    x=0
    while (a*x%26!=1):
        x=x+1
    return x
# Fonction de déchiffrement
def dechiffrementAffine(a,b,L):
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if ( L in alphabet):
        x=alphabet.index(L)
        if x<26:
            y=(inverse(a)*(x-b))%26
        if x>25:
            y=(inverse(a)*(x-b))%26
            if y<26:
                y=y+26    
        return alphabet[y]
    else :
            return chr(ord(L)+1)
# Affichage du mot chiffré
def crypt(M,a,b):
    if (math.gcd(a,26)==1):
        mot = []
        resultat= ""
        for i in range(0,len(M)):
                mot.append(chiffrementAffine(a,b,M[i]))
        resultat= resultat.join(mot)
        resultat= resultat+"A"+str(a)+","+str(b)
        return resultat
    else:
        while (math.gcd (a,26) !=1):
            a+=1
        mot = []
        resultat= ""
        
        for i in range(0,len(M)):
                mot.append(chiffrementAffine(a,b,M[i]))
        resultat= resultat.join(mot)
        resultat= resultat= resultat+"A"+str(a)+","+str(b)
        
        return  resultat

       
       
# Affichage du mot déchiffré
def decrypt(message,parametre):
    i=0
    a=''
    while(parametre[i]!=","):
        a+=parametre[i]
        i+=1
    b=''
    i+=1
    while(i<len(parametre)):
        b+=parametre[i]
        i+=1
    
    if (math.gcd(int(a),26)==1):
        mot = []
        for i in range(0,len(message)):
                mot.append(dechiffrementAffine(int(a),int(b),message[i]))
        return "".join(mot)
    else:
        while (math.gcd (int(a),26) !=1):
                a+=1
        mot = []
        for i in range(0,len(message)):
                mot.append(dechiffrementAffine(int(a),(b),message[i]))
        return "".join(mot)
