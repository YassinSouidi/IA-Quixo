import cherrypy
import sys
import numpy as np
from random import choice

def Random():
        print('random')


def IA():

        liste= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        move_mat= np.array(liste).reshape(5,5)  # matrice avec les cubes

        jeu=[1,None,1,None,1,
        1,0,None, None ,1,
        None ,0,None ,None ,1,
        1,0, None ,None ,1,
        0 ,1 ,None ,None, 0]
        matrice=np.array(jeu).reshape(5,5) # matrice lecture du jeu
        #initialisation des variables (pour tout)
        s_o=[]
        var=0
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
                                return {"cube":move_mat[o_c[p][0],-1],"direction":"W"}
                                
                        elif matrice[o_c[p][0],-1] == adversaire and matrice[o_c[p][0],0] !=adversaire:
                                return {"cube":move_mat[o_c[p][0],0],"direction":"E"}
                                
                        elif matrice[o_c[p][0],-1] == adversaire and matrice[o_c[p][0],0] ==adversaire: 
                                try:
                                        matrice[o_c[p][0]+1,-1]
                                except :
                                        if matrice[o_c[p][0]-1,-1] !=adversaire:
                                                return {"cube":move_mat[o_c[p][0]-1,-1],"direction":"W"}
                                                
                                                
                                        else:
                                                if matrice[o_c[p][0]-1,0] !=adversaire:
                                                        return {"cube":move_mat[o_c[p][0]-1,0],"direction":"E"}
                                                        

                                                else :
                                                        Random()
                                        

                                if matrice[o_c[p][0],0] !=adversaire and move_mat[o_c[p][0]+1,-1] <=24:
                                        return {"cube":move_mat[o_c[p][0]-1,-1],"direction":"E"}
                
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
        print(s_l)
        for p,l in enumerate(s_l):  # p , cest l'increment de la liste des tuples et l le tuple ( on parcourt la liste s contenant en tuples les colonnes ayant la valeur x)
                print('etape2')
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
                                        
    





print(IA())