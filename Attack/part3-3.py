import datetime
import string
from time import time

password = input("Veuillez entrer votre mot de passe : \n")
i = str()
trouve=False
print("Commençons les tests ! \n")
debut =datetime.datetime.now()
test=5

def verify(i,password):
    
    if password == i:
        global trouve
        trouve = True
        print('Mot de passe trouvé ! le voici : '+i )
        fin = datetime.datetime.now()
        print('Le temps de traitement est :')
        traitement =fin-debut
        # print(
        #     str(traitement.seconds) +' seconds')
        # print (debut)
        # print (fin)
        print (traitement)
        exit()

        # print(trouve)  

while len(password)!=5:
    password = input("Mot de passe invalide ! veuillez entrer un nouveau mot de passe qui comporte 5caractères\n")
for ch1 in string.printable:
    # if not trouve: 
        for ch2 in string.printable:
            # if not trouve:
                for ch3 in string.printable:
                    # if not trouve:
                        for ch4 in string.printable:
                            # if not trouve:
                                for ch5 in string.printable:
                                    if not trouve :
                                        i= ch1+ch2+ch3+ch4+ch5
                                        print (i)
                                        verify(i,password)
                                        if trouve:
                                            break



