import cherrypy
import sys
import numpy as np
from random import choice

class Server:
        
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()



    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        if cherrypy.request.method == "OPTIONS":
            return ''
        
        self.identification_joueur()
        return {"move":self.IA(),"message": "I'm Smart"  }



    def coup_existant(self):
        liste_coup_existant=[]
        liste_coup_possible=[0,1,2,3,4,5,9,10,14,15,19,20,24]
        body = cherrypy.request.json

        for i in range(0, len(body["game"])):
            value =body["game"][i]
            if value == self.joueur and i in liste_coup_possible:
                	liste_coup_existant.append([i])
            if value == None and i in liste_coup_possible :
                liste_coup_existant.append([i])
            if value == self.adversaire and i in liste_coup_existant:
                liste_coup_existant.remove(i)
        return liste_coup_existant


    def identification_joueur(self):
        body = cherrypy.request.json
        if body["players"][0] == body["you"]:
            self.joueur=0
            self.adversaire=1
        else:
            self.joueur=1  
            self.adversaire=0
        return self.joueur
        return self.adversaire


    def Random(self):
        print('random####')
        liste=choice(self.coup_existant())
        a=liste[0]
        direc_haut_gauche={"orientation":["S","E"]}
        direc_haut_milieu={"orientation":["S","E","W"]}
        direc_haut_droit={"orientation":["S","W"]}
        direc_gauche_milieu={"orientation":["S","E","N"]}
        direc_bas_gauche={"orientation":["N","E"]}
        direc_droit_milieu={"orientation":["S","N","W"]}
        direc_bas_milieu={"orientation":["N","E","W"]}
        direc_bas_droit={"orientation":["N","W"]}

        if a == 0:
            direction_choisie= choice(direc_haut_gauche["orientation"])
        elif a ==1  or a == 2 or a == 3:
            direction_choisie= choice(direc_haut_milieu["orientation"])
        elif a == 4:
            direction_choisie= choice(direc_haut_droit["orientation"])
        elif a ==5 or a == 10 or a == 15:
            direction_choisie= choice(direc_gauche_milieu["orientation"])
        elif a == 20:
            direction_choisie= choice(direc_bas_gauche["orientation"])
        elif a ==9 or a == 14 or a == 19:
            direction_choisie= choice(direc_droit_milieu["orientation"])
        elif a ==21 or a == 22 or a == 23:
            direction_choisie= choice(direc_bas_milieu["orientation"])
        elif a == 24:
            direction_choisie= choice(direc_bas_droit["orientation"])

        return {"cube":int(a),"direction":str(direction_choisie)}

        
    
    def IA(self):
        self.identification_joueur()
        liste= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        move_mat= np.array(liste).reshape(5,5)  # matrice avec les cubes

        body = cherrypy.request.json  # récuperation des donnés du jeu
        li=body["game"]
        matrice=np.array(li).reshape(5,5) # matrice lecture du jeu
        
        #initialisation des variables (pour tout)
       
        joueur=self.joueur 
        adversaire=self.adversaire
        print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
        print(joueur,adversaire)
        s_o=[]
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
        # #Variables attaque colones
        o_xc=[]
        s_xc=[]
        lis_xc=[]

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
        print(s_xl)
        for q,s in enumerate(s_xl): # p , cest l'increment de la liste des tuples et l le tuple ( on parcourt la liste s contenant en tuples les colonnes ayant la valeur x)
                print(q)
                if s.count(joueur) ==4:
                        for n,c in enumerate(s):
                                if c!=joueur:
                                        if matrice[-1,n] != adversaire:   #le cas ou nous on est x  cad 1
                                                print("ICII ligne")
                                                return {"cube":int(move_mat[-1,n]),"direction":"N"}  
                                        elif matrice[q,n]!= adversaire:
                                                return {"cube":int(move_mat[q,n]),"direction":"E"}  
                                        else:
                                                self.Random()

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
                                        elif matrice[n,a]!=adversaire:
                                                return {"cube":int(move_mat[n,a]),"direction":"S"}   
                                        else:
                                                self.Random()
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
                                                
                                                        self.Random()
                                        

                                if matrice[o_c[p][0],0] !=adversaire and move_mat[o_c[p][0]+1,-1] <=24:
                                        return {"cube":int(move_mat[o_c[p][0]-1,-1]),"direction":"E"}
                
                                else:
                                        self.Random()

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
                                                        self.Random()
                                        

                                        if matrice[0,o_l[p][1]] !=adversaire and move_mat[-1,o_l[p][1]+1] <=24:
                                                return {"cube":int(move_mat[-1,o_l[p][1]-1]),"direction":"S"}

                                        else:
                                                self.Random()



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
                self.Random()
        
                                




if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8080

    cherrypy.config.update({'server.socket_host':'0.0.0.0','server.socket_port':port})
    cherrypy.quickstart(Server())