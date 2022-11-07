import string


#list=["0","1","2","3","4","5","6","7","8","9"]
password = input("Veuillez entrer votre mot de passe : \n")
i = str()
trouve=False
print("Commençons les tests ! \n")


def verify(i,password):
    if password == i:
        global trouve
        trouve = True
        print('Mot de passe trouvé ! le voici : '+i)

        # print(trouve)  

for ch1 in string.digits:
    # if not trouve: 
        for ch2 in string.digits:
            # if not trouve:
                for ch3 in string.digits:
                    # if not trouve:
                        for ch4 in string.digits:
                            #if not trouve:
                                for ch5 in string.digits:
                                    if not trouve :
                                        i= ch1+ch2+ch3+ch4+ch5
                                        print (i)
                                        verify(i,password)
                                        if trouve:
                                            break
