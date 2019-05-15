



#######################################################################################################
########### INTELIGENCE ARTIFICIELLE DANS LE CADRE DU COURS D INFORMATIQUE ############################
########### AUTEURS DU SCRIPT: CALUGAR FINIAS & YASSIN SOUIDI #########################################
########### CE CODE SUIT LA STRATEGIE EXPLIQUE DANS README.md #########################################
########### Il renvoie un move selon le format {"move":{"cube":int(a),"direction":str(direction)}###### 
#######################################################################################################


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
        w=["HAHAHAHAHA tu te crois malin","hmmmm très intéressant ce style de jeu","penses-tu vraiment pouvoir nous battre?","Bien joué pour ce coup","Tu a gagné une bataille mais pas la guerre","J'en étais sur","En vrai t'es pas si fort que ça","Franchement tu me deçois","Pffffff","je ne m'avoue pas vaincu","CLAP CLAP","Seul Chuck Norris peut me vaincre","NANI?!?!?!?!?!?!?!?!","Même yamcha est plus fort que toi"]
        a = choice(w)
        self.identifier_joueur()
        return {"move":self.IA(),"message": a }


 
    def coup_possible(self):                                         
        listepos2=[]                                   # liste qui va contenir la possibilité des coups à jouer                                 
        listeindice=[0,1,2,3,4,5,9,10,14,15,19,20,24]
        body = cherrypy.request.json                                    # recuperation de données de l'état du jeu

        for i in range(0, len(body["game"])):                                                         
            value =body["game"][i]
            if value == self.joueur and i in listeindice:
                	listepos2.append([i])                   #on rajoute tout les coups qui ne sont pas des BAD MOVE dans une liste
            if value == None and i in listeindice :
                listepos2.append([i])                                   
            if value == self.adversaire and i in listepos2:
                listepos2.remove(i)                             
        return listepos2


    def identifier_joueur(self):                        # identification du joueur en recuperant les données du jeu
        body = cherrypy.request.json                   
        if body["players"][0] == body["you"]:  
            self.joueur=0
            self.adversaire=1
        else:
            self.joueur=1  
            self.adversaire=0
        return 

        



    def Random(self):                                         #Definition d'une fonction random à utiliser si aucun coup de la stratégie n'est possible

        liste=choice(self.coup_possible())                    # choix effectué parmi la liste de coups possibles grace a la librairie choice de random
        a=liste[0]      
        direc1={"orientation":["S","E"]}                      # dictionnaires contentant les differentes directions possibles en fonction du cube                
        direc2={"orientation":["S","E","W"]}                  # ex: si cube dans le coin , deux directions sont bloqués
        direc3={"orientation":["S","W"]}                      
        direc4={"orientation":["S","E","N"]}
        direc5={"orientation":["N","E"]}
        direc6={"orientation":["S","N","W"]}
        direc7={"orientation":["N","E","W"]}
        direc8={"orientation":["N","W"]}

        if a == 0:                                                              
            direction= choice(direc1["orientation"])   #en fonction de la valeur du cube on choisis au hasard parmis les directions 
        elif a ==1  or a == 2 or a == 3:
            direction= choice(direc2["orientation"])
        elif a == 4:
            direction= choice(direc3["orientation"])
        elif a ==5 or a == 10 or a == 15:
            direction= choice(direc4["orientation"])
        elif a == 20:
            direction= choice(direc5["orientation"])
        elif a ==9 or a == 14 or a == 19:
            direction= choice(direc6["orientation"])
        elif a ==21 or a == 22 or a == 23:
            direction= choice(direc7["orientation"])
        elif a == 24:
            direction= choice(direc8["orientation"])

        return {"cube":int(a),"direction":str(direction)} # la fonction retourne un move

        
    
    def IA(self):
        self.identifier_joueur()
        liste= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        move_mat= np.array(liste).reshape(5,5)  # matrice avec les cubes

        body = cherrypy.request.json  # récuperation des donnés du jeu
        li=body["game"]
        matrice=np.array(li).reshape(5,5) # matrice lecture du jeu
        
        #initialisation des variables (pour tout)
       
        joueur=self.joueur 
        adversaire=self.adversaire
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
                for i,e in enumerate(matrice[line,:]): # e est la valeur( la ligne) et i l'increment ( entre 0 et 4)
                        if e==joueur:
                                o_xl.append((line,i)) # la liste contient les positions de la variable "joueur" ( sous forme de tuple !! tres important pour qu'il soit callable par la suite)
                        
        for k in range(len(o_xl)):     #la valeur k s'incremente jusqu'au nombres d'elements contenus dans la liste 
                for z in matrice[o_xl[k][0],:]:  #z prend toutes les valeurs contenues dans les ligne sur lesquelles on trouve la variable "joueur"
                        lis_xl.append(z) # toutes ces valeurs sont rajoutés dans une liste 
        

        s_o=list(zip(*[iter(lis_xl)]*5))  # je sépare ces chiffres toutes les 5 pas ( en creant donc des tuples de 5 valeurs)
        for r in s_o:                 # on supprime les (tuples) doublons dans la nouvelle liste s_o
                if r in s_xl: 
                        pass 
                else: 
                        s_xl.append(r) # la nouvelle liste contiens des tuples de 5 elements represantant les lignes sur lesquelles les variables "joueur" a ete trouve
  
        for q,s in enumerate(s_xl): # q cest l'increment de la liste des tuples et s le tuple ( on parcourt la liste s_xl contenant les tuples des lignes conteant la variable "joueur")
                if s.count(joueur) ==4:                         #si on trouve 4 variables "joueur" , on cherche la valeur dans la ligne qui est differente de "joueur"
                        for n,c in enumerate(s):                # ensuite on verifie que le cube à l'opposé suivant la collone corespondante est jouable
                                if c!=joueur:
                                        if matrice[-1,n] != adversaire:    
                                                return {"cube":int(move_mat[-1,n]),"direction":"N"}  
                                        elif matrice[q,n]!= adversaire:
                                                return {"cube":int(move_mat[q,n]),"direction":"E"}  
                                        else:
                                                self.Random()

# #######ATTAQUE COLONNE #########################################################################################################################  
                                                                        ## memes explications que dans ATTAQUE LIGNE 
        print('attaque collone')
        for column in range(5):

                for i,e in enumerate(matrice[:,column]):
                        if e==joueur:  
                                o_xc.append((i,column)) 
                                
        for k in range(len(o_xc)):     
                for z in matrice[:,o_xc[k][1]]:  
                        lis_xc.append(z)
        s_o=list(zip(*[iter(lis_xc)]*5))  

        for r in s_o:                 
                if r in s_xc: 
                        pass 
                else: 
                        s_xc.append(r) 
        
        for a,z in enumerate(s_xc):  
                print(a)
                if z.count(joueur) ==4:
                        print("ok")
                        for n,c in enumerate(z):
                                if c!=joueur:
                                        if matrice[n,-1] != adversaire: 
                                                print("ICII colonne")  
                                                return {"cube":int(move_mat[n,-1]),"direction":"W"}      
                                        elif matrice[n,a]!=adversaire:
                                                return {"cube":int(move_mat[n,a]),"direction":"S"}   
                                        else:
                                                self.Random()
###DEFENSE COLONNES ##############################################################################################################
        print(matrice)
        for column in range(5):

                for i,e in enumerate(matrice[:,column]):  # e est la valeur( la ligne) et i l'increment ( entre 0 et 4)
                        if e==adversaire:
                                o_c.append((i,column))  # la liste contient les positions de la variable "adversire" ( sous forme de tuple !! tres important pour qu'il soit callable par la suite)
                                
        for k in range(len(o_c)):              #la valeur k s'incremente jusqu'au nombres d'elements contenus dans la liste 
                for z in matrice[:,o_c[k][1]]:   #z prend toutes les valeurs contenues dans les ligne sur lesquelles on trouve la variable "adversaire"
                        lis_c.append(z)         # toutes ces valeurs sont rajoutés dans une liste 

        s_o=list(zip(*[iter(lis_c)]*5))       # je sépare ces chiffres toutes les 5 pas ( en creant donc des tuples de 5 valeurs)
         
        for r in s_o:                         # on supprime les(tuples)doublons dans la nouvelle liste s_o
                if r in s_c: 
                        pass 
                else: 
                        s_c.append(r)  # la nouvelle liste contiens des tuples de 5 elements represantant les lignes sur lesquelles les variables "adversaire" a ete trouve
      
        for p,l in enumerate(s_c):  # p cest l'increment de la liste des tuples et l le tuple ( on parcourt la liste s_c contenant les tuples des lignes contenant la variable "adversaire")
                if l.count(adversaire)>=3:     #si on trouve 3 variables "adversaire" ou plus :
                      
                        print('colonne lcount')
                        if matrice[o_c[p][0],0] != adversaire:                                         #on verifie que le cube situé ,en début de ligne de la valeur corespondant à la positions de l'adversaire est jouable
                                return {"cube":int(move_mat[o_c[p][0],0]),"direction":"E"}

                        elif matrice[o_c[p][0],-1] != adversaire:                                    #on verifie que le cube situé ,en fin de ligne de la valeur corespondant à la positions de l'adversaire est jouable
                                 return {"cube":int(move_mat[o_c[p][0],-1]),"direction":"W"}
                                
                        elif matrice[o_c[p][0],-1] == adversaire and matrice[o_c[p][0],0] ==adversaire:  #si le cas precedent est False alors on 
                                try:                                                                     # try si la ligne en dessous dans la matrice existe (si c'est le cas , le code continue sinon except est effectué)
                                        matrice[o_c[p][0]+1,-1]                                         
                                except :
                                        if matrice[o_c[p][0]-1,-1] !=adversaire:                               # on regarde si sur la ligne au dessus dans la matrice ,si la valeur à l'opposé corespondant à la position de l'adversaire est jouable 
                                                return {"cube":int(move_mat[o_c[p][0]-1,-1]),"direction":"W"}
                                                
                                                
                                        else:
                                                if matrice[o_c[p][0]-1,0] !=adversaire:                                  #si les cas precedents sont False on verifie la jouabilite de la premiere valeur de la ligne au dessus dans la matrice
                                                        return {"cube":int(move_mat[o_c[p][0]-1,0]),"direction":"E"}

                                                else:
                                                        self.Random()                                   #en dernier recours on fait appel à la fonction Random
                                        
                                if matrice[o_c[p][0]+1,-1] != adversaire:
                                        return {"cube":int(move_mat[o_c[p][0]+1,-1]),"direction":"W"}   # si la condition dans try est True , on execute ce code
                
                                else:
                                        self.Random()

###DEFENSE LIGNES #######################################################################################################################################
                                        #meme commentaires que pour DEFENSE COLONES
        print('else ligne')
        for line in range(5):
                for i,e in enumerate(matrice[line,:]): 
                        if e==adversaire:
                                o_l.append((line,i)) 

        for k in range(len(o_l)):     
                for z in matrice[o_l[k][0],:]:  
                        lis_l.append(z) 

        s_o=list(zip(*[iter(lis_l)]*5))  
        for r in s_o: 
                if r in s_l: 
                        pass 
                else: 
                        s_l.append(r)         

        for p,l in enumerate(s_l):  
                if l.count(adversaire)>=3:
                        print('ligne adv')

                        if matrice[0,o_l[p][1]] != adversaire:  
                                return {"cube":int(move_mat[0,o_l[p][1]]),"direction":"S"}

                        elif matrice[-1,o_l[p][1]] != adversaire:  
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
                                        

                                if matrice[-1,o_l[p][1]+1] !=adversaire :
                                        return {"cube":int(move_mat[-1,o_l[p][1]+1]),"direction":"N"}

                                else:
                                        self.Random()



###ATTAQUE COINS #######################################################################################################################################                
        if matrice[0,0]==adversaire and matrice[0,4]==None:                     # ce code monopolise les coins 
                return {"cube":int(move_mat[0,4]),"direction":"W"}              # il verifie que le coin est a l'adversaire 
        elif matrice[0,4]==adversaire and matrice[0,0]==None:                   # si c'est le ca alors on verifie que le coin qui lui est aligné mais opposé est jouable 
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