def palindrome(mot):
    mot = mot.lower()
    if mot == mot [::-1] and len(mot) > 1 :
        return 1
    else:
        return 0 

def exist(x):
    Vect_separateur = ["\n","&","#","{","}","(",")","|","_","-","[","]","@",",",".","?","!","*","$","/",'%',";"," "]
    if(Vect_separateur.count(x)==0):
        return 0
    else:
        return 1

def Position_Mot_pal(text) :
    pos=[]
    i=0
    while i<len(text):
        word=""
        if exist(text[i])==1   :
            i=i+1       
        while i<len(text)  and exist(text[i])==0   :
            word=word+text[i]
            i=i+1   
        if palindrome(word) :
            pos.append (i-len(word))
    return pos

def Mir_Pl(mot):
    length= len(mot)
    le= int (length/2)
    
    if (length % 2) == 0 :
        p = "p"
        sh = mot[0:le]       
        ch = mot[le:length]               
    else:
        p = "i"
        sh = mot[:le+1] 
        ch = mot[le+1:length]
         
    
    sh = sh [::-1]
    sh = sh + p 
    #print(le,le)
    #print(ch)
    i=0
    Nbr_Majiscule=0
    while i <= (le-1 ) :
            x = ch[i]
            #print(x)
            if x.isupper() :
                Nbr_Majiscule = Nbr_Majiscule +1 
                sh = sh + str(i)
            i=i+1

    decalage = Nbr_Majiscule - len(ch) + 1    
    return sh,decalage #,Nbr_Majiscule
     


def cryptage_Miroire(text) :
    text = text [::-1]
    i=0
    P=Position_Mot_pal(text)
    while i<len(text):
        word=""
        if exist(text[i])==1   :
            i=i+1       
        while i<len(text)  and exist(text[i])==0   :
            word=word+text[i]
            i=i+1   
        if palindrome(word) :
                (a,b)=Mir_Pl(word)
                text=text.replace(word,a,1)
    print(P)
    text=text+"m"  
    for x in P :
        text=text+str(x)+","
    return text



def decryptage_miroire (msg_crypted,position_palaindrome):

    lentgth = 0
    text = msg_crypted
    
    L = list(position_palaindrome.split(","))
    w=L.pop()
    P=[int(x) for x in L]
    print(P)
    
    
    for Pos_Deb_Pal in P:
        i=Pos_Deb_Pal
        word=""  
        lentgth=0
        print(text)
        while i<len(text)  and exist(text[i]) == 0   :
            word=word+text[i]
            print("a",i,word,"e")
            i=i+1
            lentgth=lentgth+1 

        p1 = word.rfind("i")
        p2 = word.rfind("p")

        if p1<p2 :
            Position_Parity_bit=p2
        else:
            Position_Parity_bit=p1
        inv_word=word[:Position_Parity_bit][::-1]

        if word[Position_Parity_bit]=="p":
            ch=inv_word[:Position_Parity_bit]
        else:
            ch=inv_word[:Position_Parity_bit-1]

        ch=ch.lower()
        ch=ch[::-1]
        nbr_maj=0
        
        if Position_Parity_bit!=(lentgth-1): #il existe des char en majiscule
            k= Position_Parity_bit+1
        
            while k <lentgth : #parcourir la partie apres parity bit
                ch= ch[:int(word[k])] + ch[int(word[k])].upper() + ch[int(word[k]) + 1:]
                k= k+1
                nbr_maj=nbr_maj+1
                
        p=Position_Parity_bit+Pos_Deb_Pal
        diff=len(ch)-nbr_maj
        sh=""
        for n in range(diff):
            sh=sh+" "

        text = text[:p] +sh+ text[p+1:]
        
        for m in ch :
            text=text[:p] + m + text[p+1  :]
            p=p+1
        part_1=word[0:Position_Parity_bit][::-1]
        
        f=Pos_Deb_Pal
        for t in part_1 :
            text=text[:f] + t + text[f+1:]
            f=f+1
            
    text= text[::-1]       
    return text
    
#************************************TEST********************************************    
# try:
#         fhand = open('miroire.txt')
# except:
#         print('File cannot be opened:', 'miroire.txt')
#         exit()

# msg = fhand.read()  

# fhand.close()

# fhand1 = open('miroire1.txt','w')
# c_msg = cryptage_Miroire(msg) 
# i = len(c_msg)-1
# while c_msg[i] not in ('m','a','g','d'):
#     i=i-1
# method = c_msg[i] 		# la variable "méthode" prend la valeur 'g'
# i=i+1
# dec = c_msg[i:len(c_msg)] 	# la variable "dec" prend la valeur '3'
# c_msg = c_msg[0:i-1] 


# affich_msg="le message crypté est:\n"+c_msg+"\n\nle message decrypté est:\n"+decryptage_miroire(c_msg,dec)

# fhand1.write(affich_msg)
# fhand1.close()