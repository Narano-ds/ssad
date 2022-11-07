import random
def randomText():
    c="when we least expect it, life sets us a challenge to test our courage and willingness to change; at such a moment, there is no point in pretending that nothing has happened or in saying that we are not yet ready. the challenge will not wait. life does not look back. A week is more than enough time for us to decide whether or not to accept our destiny"
    b="Here's to the crazy ones. The misfits. The rebels. The troublemakers. The round pegs in the square holes. The ones who see things differently. They're not fond of rules. And they have no respect for the status quo. You can quote them, disagree with them, glorify or vilify them. About the only thing you can't do is ignore them. Because they change things. They push the human race forward. And while some may see them as the crazy ones, we see genius. Because the people who are crazy enough to think they can change the world, are the ones who do."
    a="Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do. So throw off the bowlines. Sail away from the safe harbor. Catch the trade winds in your sails. Explore. Dream. Discover."
    Text=[]
    Text.append(a.lower())
    Text.append(b.lower())
    Text.append(c.lower())
    return Text[random.choice([2,0,1])]
    

def string2bin(message): #exemple string="se" bin(s)=01110011 et bin(e)=01100101
    #strr= ''.join(bin(ord(c)) for c in string).replace('b','')#le texte en binaire 0111001101100101
    
    strr=''.join(format(ord(i), '08b') for i in message) #message en binaire 

    l = [strr[i:i+8] for i in range(0, len(strr), 8)]
    #chaque element est le code binaire de chaque carctere du message ['01110011', '01100101']

    strr = ""
    for ele in l:
        strr += ele[::-1] 
     #str contient les codes binaires de chaque caractere inversé, le tout concaténé 1100111010100110
    return strr

def stenographyCryptage(message):
    text= randomText()
    msg=string2bin(message)
    Vect_separateur = ["\n","&","#","{","}","(",")","|","_","-","[","]","@",",",".","?","!","*","$","/",'%',";"," ","'"]
    i=0
    for x in msg:
        while text[i] in Vect_separateur:
            i+=1
        if x=="1":
            text= text[:i] + text[i].upper() + text[i + 1:]
        i+=1
    text=text+"S"
    return text

def stenographyDecryptage(crypted_txt):
    Vect_separateur = ["\n","&","#","{","}","(",")","|","_","-","[","]","@",",",".","?","!","*","$","/",'%',";"," ","'"]
    res = max([idx for idx in range(len(crypted_txt)) if crypted_txt[idx].isupper()]) 
    #position de la derniere lettre en majiscule

    text=crypted_txt[0:res+1]

    strr=''
    for x in text:#transformer les texte en une chaine de binaire strr
        if x not in Vect_separateur:
            if x.isupper(): #1 si majuscule
                strr+="1"
            else:
                strr+="0"
   
    if len(strr) % 8 != 0 : #rajouter les 0 manquants
        mult=((int(len(strr)/8)+1)*8)-len(strr)
        while mult != 0:
            strr+="0"
            mult-=1

    #décortiquer strr en chaines de 8bits
    binary_values = [strr[i:i+8] for i in range(0, len(strr), 8)]
    
    #transformation du binaire en caractere
    decrypted_msg=''
    for binary_value in binary_values:
        an_integer = int(binary_value[::-1], 2) #bin to decimal
        ascii_character = chr(an_integer) #decimal to ascii
        decrypted_msg += ascii_character  #concaténation

    return(decrypted_msg)


 
# try:
#         fhand = open('stenaText.txt')
# except:
#         print('File cannot be opened:', 'stenaText.txt')
#         exit()

#*******************************************TEST********************************************
# msg = fhand.read()  

# fhand.close()

# fhand1 = open('stenaText1.txt','w')
# affich_msg="le message crypté est:\n"+stenographyCryptage(msg)+"\n\nle message decrypté est:\n"+stenographyDecryptage(stenographyCryptage(msg))

# fhand1.write(affich_msg)
# fhand1.close()