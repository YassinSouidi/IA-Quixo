import cherrypy
import sys
import numpy as np
from random import choice

def Random():
        print('random')
def IA():

        liste= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        move_mat= np.array(liste).reshape(5,5)  # matrice avec les cubes

        jeu=[0,None,None,None,None,
        0, None ,None, None ,None,
        0 ,None ,None ,None ,None,
        None, None, None ,None ,1,
        0,None,None ,0, 1]

        matrice=np.array(jeu).reshape(5,5) # matrice lecture du jeu
        #initialisation des variables (pour tout)
        s_o=[]
        joueur=0 
        adversaire=1
        #Variables lignes
        o_l=[]
        s_l=[]
        lis_l=[]
        #Variables colones
        o_c=[]
        s_c=[]
        lis_c=[]
        #Variables attaque ligne
        o_xl=[]
        s_xl=[]
        lis_xl= []
        #Variables attaque colones
        o_xc=[]
        s_xc=[]
        lis_xc=[]
        


###DEFENSE COLONNES ##############################################################################################################
        print(matrice)
        for column in range(5):

                for i,e in enumerate(matrice[:,column]):
                        if e==adversaire:
                                o_c.append((i,column)) #la liste o contient les poistions du chiffre 5( sous forme de tuple !! tres important)
                                
        for k in range(len(o_c)):              #la valeur k s'incremente jusqu'au nombres d'elements contenus dans la liste o
                for z in matrice[:,o_c[k][1]]:  #z prend chaque valeur des colonnes ou un 5 est trouvé ( dans l'ordre)
                        lis_c.append(z) # toutes les valeurs sont rajoutés dans une liste 

        s_o=list(zip(*[iter(lis_c)]*5))  # je sépare ces chiffres toutes les 5 pas ( en creant des tuples)     
         
        for r in s_o:                 # on passe par un ensemble pour supprimer les doublons
                if r in s_c: 
                        pass 
                else: 
                        s_c.append(r) 
      
        for p,l in enumerate(s_c):  # p , cest l'increment de la liste des tuples et l le tuple ( on parcourt la liste s contenant en tuples les colonnes ayant la valeur x)
                
                if l.count(adversaire)>=3:      # si dans la colonne on compte plus de 3 zero on remplace le 5 par un 9 à l'aide de la liste o contenant les position
                      
                        print('colonne lcount')
                        if matrice[o_c[p][0],-1] != adversaire:   #le cas ou nous on est x  cad 1
                                return {"cube":int(move_mat[o_c[p][0],-1]),"direction":"W"}
                                
                        elif matrice[o_c[p][0],-1] == adversaire and matrice[o_c[p][0],0] !=adversaire:
                                return {"cube":int(move_mat[o_c[p][0],0]),"direction":"E"}
                                
                        elif matrice[o_c[p][0],-1] == adversaire and matrice[o_c[p][0],0] ==adversaire: 
                                try:
                                        matrice[o_c[p][0]+1,-1]
                                except :
                                        if matrice[o_c[p][0]-1,-1] !=adversaire:
                                                return {"cube":int(move_mat[o_c[p][0]-1,-1]),"direction":"W"}
                                                
                                                
                                        else:
                                                if matrice[o_c[p][0]-1,0] !=adversaire:
                                                        return {"cube":int(move_mat[o_c[p][0]-1,0]),"direction":"E"}
                                                        

                                                else : 
                                                
                                                        Random()
                                        

                                if matrice[o_c[p][0],0] !=adversaire and move_mat[o_c[p][0]+1,-1] <=24:
                                        return {"cube":int(move_mat[o_c[p][0]-1,-1]),"direction":"E"}
                
                                else:
                                        Random()

###DEFENSE LIGNES #######################################################################################################################################

        print('else ligne')
        for line in range(5):
                for i,e in enumerate(matrice[line,:]): # e est la valeur et i l'increment
                        if e==adversaire:
                                o_l.append((line,i)) #la liste o contient les poistions du chiffre 5( sous forme de tuple !! tres important)

        for k in range(len(o_l)):     #la valeur k s'incremente jusqu'au nombres d'elements contenus dans la liste o
                for z in matrice[o_l[k][0],:]:  #z prend toutes les ligne des valeurs vallant 'adversaire'
                        lis_l.append(z) # toutes les valeurs sont rajoutés dans une liste 

        s_o=list(zip(*[iter(lis_l)]*5))  # je sépare ces chiffres toutes les 5 pas ( en creant des tuples)
        for r in s_o: 
                if r in s_l: 
                        pass 
                else: 
                        s_l.append(r)          # on passe par un ensemble pour supprimer les doublons
        
        for p,l in enumerate(s_l):  # p , cest l'increment de la liste des tuples et l le tuple ( on parcourt la liste s contenant en tuples les colonnes ayant la valeur x)
                if l.count(adversaire)>=3:
                        print('ligne adv')
                        
                        if matrice[-1,o_l[p][1]] != adversaire:   #le cas ou nous on est x  cad 1
                                return {"cube":int(move_mat[-1,o_l[p][1]]),"direction":"N"}
                                
                        elif matrice[-1,o_l[p][1]] == adversaire and matrice[0,o_l[p][1]] !=adversaire:
                                return {"cube":int(move_mat[0,o_l[p][1]]),"direction":"S"}
                                        
                        elif matrice[-1,o_l[p][1]] == adversaire and matrice[0,o_l[p][1]] ==adversaire: 
                                try:
                                        matrice[-1,o_l[p][1]+1]
                                except :
                                        if matrice[-1,o_l[p][1]-1] !=adversaire:
                                                return {"cube":int(move_mat[-1,o_l[p][1]-1]),"direction":"N"}
                                        

                                        else:
                                                if matrice[0,o_l[p][1]-1] !=adversaire:
                                                        return {"cube":int(move_mat[0,o_l[p][1]-1]),"direction":"S"}
                                                        

                                                else :
                                                        Random()
                                        

                                        if matrice[0,o_l[p][1]] !=adversaire and move_mat[-1,o_l[p][1]+1] <=24:
                                                return {"cube":int(move_mat[-1,o_l[p][1]-1]),"direction":"S"}

                                        else:
                                                Random()


 ###ATTAQUE LIGNES #######################################################################################################################################                                                
        print('attaque lignes')
        for line in range(5):
                for i,e in enumerate(matrice[line,:]): # e est la valeur et i l'increment
                        if e==joueur:
                                o_xl.append((line,i)) #la liste o contient les poistions du chiffre 5( sous forme de tuple !! tres important)
                        
        for k in range(len(o_xl)):     #la valeur k s'incremente jusqu'au nombres d'elements contenus dans la liste o
                for z in matrice[o_xl[k][0],:]:  #z prend toutes les ligne des valeurs vallant 'adversaire'
                        lis_xl.append(z) # toutes les valeurs sont rajoutés dans une liste 
        

        s_o=list(zip(*[iter(lis_xl)]*5))  # je sépare ces chiffres toutes les 5 pas ( en creant des tuples)
        for r in s_o:                 # on passe par un ensemble pour supprimer les doublons
                if r in s_xl: 
                        pass 
                else: 
                        s_xl.append(r) 
        
        for q,s in enumerate(s_xl): # p , cest l'increment de la liste des tuples et l le tuple ( on parcourt la liste s contenant en tuples les colonnes ayant la valeur x)
                print(q)
                if s.count(joueur) ==4:
                        for n,c in enumerate(s):
                                if c!=joueur:
                                        if matrice[-1,n] != adversaire:   #le cas ou nous on est x  cad 1
                                                print("ICII ligne")
                                                return {"cube":int(move_mat[-1,n]),"direction":"N"}    
                                        else:
                                                return {"cube":int(move_mat[q,n]),"direction":"E"}  

# #######ATTAQUE COLONNE #########################################################################################################################  
 
        print('attaque collone')
        for column in range(5):

                for i,e in enumerate(matrice[:,column]):
                        if e==joueur:  
                                o_xc.append((i,column)) #la liste o contient les poistions du chiffre 5( sous forme de tuple !! tres important)
                                
        for k in range(len(o_xc)):     #la valeur k s'incremente jusqu'au nombres d'elements contenus dans la liste o
                for z in matrice[:,o_xc[k][1]]:  #z prend chaque valeur des colonnes ou un 5 est trouvé ( dans l'ordre)
                        lis_xc.append(z) # toutes les valeurs sont rajoutés dans une liste 
        s_o=list(zip(*[iter(lis_xc)]*5))  # je sépare ces chiffres toutes les 5 pas ( en creant des tuples)

        for r in s_o:                 # on passe par un ensemble pour supprimer les doublons
                if r in s_xc: 
                        pass 
                else: 
                        s_xc.append(r) 
      
        for a,z in enumerate(s_xc):  # p , cest l'increment de la liste des tuples et l le tuple ( on parcourt la liste s contenant en tuples les colonnes ayant la valeur x)
                print(a)
                if z.count(joueur) ==4:
                        print("ok")
                        for n,c in enumerate(z):
                                if c!=joueur:
                                        if matrice[n,-1] != adversaire: 
                                                print("ICII colonne")  #le cas ou nous on est x  cad 1
                                                return {"cube":int(move_mat[n,-1]),"direction":"W"}      
                                        else:
                                                return {"cube":int(move_mat[n,a]),"direction":"S"}   


###ATTAQUE COINS #######################################################################################################################################                
        if matrice[0,0]==adversaire and matrice[0,4]==None:
                return {"cube":int(move_mat[0,4]),"direction":"W"}
        elif matrice[0,4]==adversaire and matrice[0,0]==None:
                return {"cube":int(move_mat[0,0]),"direction":"E"}
        elif matrice[0,4]==adversaire and matrice[4,4]==None:
                return {"cube":int(move_mat[4,4]),"direction":"N"}
        elif matrice[0,0]==adversaire and matrice[4,0]==None:
                return {"cube":int(move_mat[4,0]),"direction":"N"}
        elif matrice[4,0]==adversaire and matrice[0,0]==None:
                return {"cube":int(move_mat[0,0]),"direction":"S"}
        elif matrice[4,0]==adversaire and matrice[4,4]==None:
                return {"cube":int(move_mat[4,4]),"direction":"W"}
        elif matrice[4,4]==adversaire and matrice[0,4]==None:
                return {"cube":int(move_mat[0,4]),"direction":"S"}
        elif matrice[4,4]==adversaire and matrice[4,0]==None:
                return {"cube":int(move_mat[4,0]),"direction":"E"}

        elif matrice[0,0]==adversaire and matrice[0,4]==joueur:
                return {"cube":int(move_mat[0,4]),"direction":"W"}
        elif matrice[0,4]==adversaire and matrice[0,0]==joueur:
                return {"cube":int(move_mat[0,0]),"direction":"E"}
        elif matrice[0,4]==adversaire and matrice[4,4]==joueur:
                return {"cube":int(move_mat[4,4]),"direction":"N"}
        elif matrice[0,0]==adversaire and matrice[4,0]==joueur:
                return {"cube":int(move_mat[4,0]),"direction":"N"}
        elif matrice[4,0]==adversaire and matrice[0,0]==joueur:
                return {"cube":int(move_mat[0,0]),"direction":"S"}
        elif matrice[4,0]==adversaire and matrice[4,4]==joueur:
                return {"cube":int(move_mat[4,4]),"direction":"W"}
        elif matrice[4,4]==adversaire and matrice[0,4]==joueur:
                return {"cube":int(move_mat[0,4]),"direction":"S"}
        elif matrice[4,4]==adversaire and matrice[4,0]==joueur:
                return {"cube":int(move_mat[4,0]),"direction":"E"}         
        elif matrice[0,0]!=adversaire :
                return {"cube":int(move_mat[0,0]),"direction":"E"}
        else:
                Random()
        


                                
print(IA())


                                        
#  #########ATTAQUE LIGNE#########################################################################################################################
#                                 else:
#                                         print('attaque ligne')
#                                         for line in range(5):
#                                                 for i,e in enumerate(matrice[line,:]): # e est la valeur et i l'increment
#                                                         if e==joueur:
#                                                                 o_xl.append((line,i)) #la liste o contient les poistions du chiffre 5( sous forme de tuple !! tres important)
                                                    
#                                         for k in range(len(o_xl)):     #la valeur k s'incremente jusqu'au nombres d'elements contenus dans la liste o
#                                                 for z in matrice[o_xl[k][0],:]:  #z prend toutes les ligne des valeurs vallant 'adversaire'
#                                                         lis_xl.append(z) # toutes les valeurs sont rajoutés dans une liste 
                                        

#                                         s_o=list(zip(*[iter(lis_xl)]*5))  # je sépare ces chiffres toutes les 5 pas ( en creant des tuples)
#                                         for r in s_o:                 # on passe par un ensemble pour supprimer les doublons
#                                                 if r in s_xl: 
#                                                         pass 
#                                                 else: 
#                                                         s_xl.append(r) 
                                        
#                                         for q,s in enumerate(s_xl): # p , cest l'increment de la liste des tuples et l le tuple ( on parcourt la liste s contenant en tuples les colonnes ayant la valeur x)
                                               
#                                                 if s.count(joueur) ==4:
#                                                         for n,c in enumerate(s):
#                                                                 if c!=joueur:
#                                                                         if matrice[-1,n] != adversaire:   #le cas ou nous on est x  cad 1
#                                                                                 print("ICII ligne")
#                                                                                 return {"cube":int(move_mat[-1,n]),"direction":"N"}
# #######ATTAQUE COLONNE #########################################################################################################################  

 
#                                                 else:   
#                                                         print('attaque collone')
#                                                         for column in range(5):

#                                                                 for i,e in enumerate(matrice[:,column]):
#                                                                         if e==joueur:  
#                                                                                 o_xc.append((i,column)) #la liste o contient les poistions du chiffre 5( sous forme de tuple !! tres important)
                                                                                
#                                                         for k in range(len(o_xc)):     #la valeur k s'incremente jusqu'au nombres d'elements contenus dans la liste o
#                                                                 for z in matrice[:,o_xc[k][1]]:  #z prend chaque valeur des colonnes ou un 5 est trouvé ( dans l'ordre)
#                                                                         lis_xc.append(z) # toutes les valeurs sont rajoutés dans une liste 
#                                                         s_o=list(zip(*[iter(lis_xc)]*5))  # je sépare ces chiffres toutes les 5 pas ( en creant des tuples)

#                                                         for r in s_o:                 # on passe par un ensemble pour supprimer les doublons
#                                                                 if r in s_xc: 
#                                                                         pass 
#                                                                 else: 
#                                                                         s_xc.append(r) 
                                                        
#                                                         for a,z in enumerate(s_xc):  # p , cest l'increment de la liste des tuples et l le tuple ( on parcourt la liste s contenant en tuples les colonnes ayant la valeur x)
#                                                                 print(a)
#                                                                 if z.count(joueur) ==4:
#                                                                         print("ok")
#                                                                         for n,c in enumerate(z):
#                                                                                 if c!=joueur:
#                                                                                         if matrice[n,-1] != adversaire: 
#                                                                                                 print("ICII colonne")  #le cas ou nous on est x  cad 1
#                                                                                                 return {"cube":int(move_mat[n,-1]),"direction":"W"}



                                                                


