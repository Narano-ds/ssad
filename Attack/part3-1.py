list=["0","1"]
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


for ch1 in list:
    # i=ch1
    if not trouve :
        #verify(i,password)
    
        for ch2 in list: 
            # i=ch1+ch2
            # print(i)
            #verify(i,password)
            if not trouve : 
                for ch3 in list : 
                    i = ch1+ch2+ch3
                    print (i)
                    verify (i,password)     
                    if trouve : 
                        break
                    
                