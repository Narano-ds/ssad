def decalageDroiteDecrypt(text):
    liste_car=[]
    liste_car_double=[]
    resultat=""
    text_pour_util=""
    decalage=""
    i = len(text)-1
    while text[i] not in ('m','a','c','g','d'):
        i=i-1
    i=i+1
    decalage = int(text[i:len(text)])
    text_pour_util = text[0:i-1]
    text=text_pour_util
    for i in text:

        for k in liste_car:
            if(i==k):
                s=True  
                break
        else:
            s=False

        if(s==True):
            continue
        else:
            liste_car.append(i)
        
    liste_car.sort()

    for i in range(2):
        for j in liste_car :
            liste_car_double.append(j)
   
    decalage_mod= decalage % len(liste_car)
    dec=decalage
    if(decalage<len(liste_car)):

        resultat_decal=""
        for i in text:
            for j in range(len(liste_car_double)):
                if(i==liste_car_double[j]):
                    resultat_decal=resultat_decal+liste_car_double[j+decalage]
                    break
                else:
                    continue

        resultat=resultat_decal
        

    if(decalage>len(liste_car)):
        decalage=decalage_mod
        if(decalage==0):
            decalage=decalage-1
            resultat_decal=""
            for i in text:
                for j in range(len(liste_car_double)):
                    if(i==liste_car_double[j]):
                        resultat_decal=resultat_decal+liste_car_double[j+decalage]
                        break
                    else:
                        continue

            resultat=resultat_decal
            
        else:
            
            resultat_decal=""
            for i in text:
                for j in range(len(liste_car_double)):
                    if(i==liste_car_double[j]):
                        resultat_decal=resultat_decal+liste_car_double[j+decalage]
                        break
                    else:
                        continue

            resultat=resultat_decal
            

    if(decalage==len(liste_car)):
        decalage=decalage-1

        resultat_decal=""
        for i in text:
            for j in range(len(liste_car_double)):
                if(i==liste_car_double[j]):
                    resultat_decal=resultat_decal+liste_car_double[j+decalage]
                    break
                else:
                    continue

        resultat=resultat_decal

    
    return resultat


