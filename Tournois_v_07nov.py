#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class Checkbar(Frame):
    
    def __init__(self, parent=None, picks=[]):
        Frame.__init__(self, parent)
        self.grid()
        self.vars = []
        j=0
        k=0
        l=(len(picks)-1)
        col=0
        
        while col < (nbCol+1):
            while j< (nb/nbCol) and k<l:
                
                var = StringVar()
                pick = picks[k]
                chk = Checkbutton(self, text=pick, variable=var,fg="blue", activebackground="red", onvalue=pick, offvalue='')
                 
                chk.grid(row=j+1,column= col+2, padx = 10, pady = 0, sticky = W)
                
                self.vars.append(var)
                                    
                k = k+1
                j = j+1  # permet de placer les textes les uns en dessous des autres. Faire varier la valeur de +4 pour voir l'effet'
                
            j = 0
            col = col+1
            
          
    def state(self):
        return map((lambda var: var.get()), self.vars)
      
def case_vide(ligne,colonne):
    label=Label(fen, text='').grid(row = ligne, column = colonne)


     
 # listeDept est la liste des departements avec le numéro et la région


Dept = ['Ain', '1', 'Rhône-Alpes',
'Aisne', '2', 'Picardie',
'Allier', '3', 'Auvergne',
'Alpes de Hautes-Provence', '4', 'Provence-Alpes-Côte d Azur',
'Hautes-Alpes', '5', 'Provence-Alpes-Côte d Azur',
'Alpes-Maritimes', '6', 'Provence-Alpes-Côte d Azur',
'Ardèche', '7', 'Rhône-Alpes',
'Ardennes', '8', 'Champagne-Ardenne',
'Ariège', '9', 'Midi-Pyrénées',
'Aube', '10', 'Champagne-Ardenne',
'Aude', '11', 'Languedoc-Roussillon',
'Aveyron', '12', 'Midi-Pyrénées',
'Bouches-du-Rhône', '13', 'Provence-Alpes-Côte d Azur',
'Calvados', '14', 'Basse-Normandie',
'Cantal', '15', 'Auvergne',
'Charente', '16', 'Poitou-Charentes',
'Charente-Maritime', '17', 'Poitou-Charentes',
'Cher', '18', 'Centre',
'Corrèze', '19', 'Limousin',
'Corse-du-Sud', '2A', 'Corse',
'Haute-Corse', '2B', 'Corse',
'Côte-d Or', '21', 'Bourgogne',
'Côtes d Armor', '22', 'Bretagne',
'Creuse', '23', 'Limousin',
'Dordogne', '24', 'Aquitaine',
'Doubs', '25', 'Franche-Comté',
'Drôme', '26', 'Rhône-Alpes',
'Eure', '27', 'Haute-Normandie',
'Eure-et-Loir', '28', 'Centre',
'Finistère', '29', 'Bretagne',
'Gard', '30', 'Languedoc-Roussillon',
'Haute-Garonne', '31', 'Midi-Pyrénées',
'Gers', '32', 'Midi-Pyrénées',
'Gironde','33', 'Aquitaine',
'Hérault', '34', 'Languedoc-Roussillon',
'Ille-et-Vilaine', '35', 'Bretagne',
'Indre', '36', 'Centre',
'Indre-et-Loire', '37', 'Centre',
'Isère', '38', 'Rhône-Alpes',
'Jura', '39', 'Franche-Comté',
'Landes', '40', 'Aquitaine',
'Loir-et-Cher', '41', 'Centre',
'Loire', '42', 'Rhône-Alpes',
'Haute-Loire', '43', 'Auvergne',
'Loire-Atlantique', '44', 'Pays de la Loire',
'Loiret', '45', 'Centre',
'Lot', '46', 'Midi-Pyrénées',
'Lot-et-Garonne', '47', 'Aquitaine',
'Lozère', '48', 'Languedoc-Roussillon',
' Maine-et-Loire','49', 'Pays de la Loire',
'Manche', '50', 'Basse-Normandie',
'Marne', '51', 'Champagne-Ardenne',
'Haute-Marne', '52', 'Champagne-Ardenne',
'Mayenne', '53', 'Pays de la Loire',
'Meurthe-et-Moselle', '54', 'Lorraine',
'Meuse', '55', 'Lorraine',
'Morbihan', '56', 'Bretagne',
'Moselle', '57', 'Lorraine',
'Nièvre',' 58', 'Bourgogne',
'Nord', '59', 'Nord-Pas-de-Calais',
'Oise', '60', 'Picardie',
'Orne', '61', 'Basse-Normandie',
'Pas-de-Calais', '62', 'Nord-Pas-de-Calais',
'Puy-de-Dôme', '63', 'Auvergne',
'Pyrénées-Atlantiques', '64', 'Aquitaine',
'Hautes-Pyrénées', '65', 'Midi-Pyrénées',
'Pyrénées-Orientales', '66', 'Languedoc-Roussillon',
'Bas-Rhin',' 67', 'Alsace',
'Haut-Rhin', '68', 'Alsace',
'Rhône', '69', 'Rhône-Alpes',
'Haute-Saône', '70', 'Franche-Comté',
'Saône-et-Loire', '71', 'Bourgogne',
'Sarthe', '72', 'Pays de la Loire',
'Savoie',' 73', 'Rhône-Alpes',
'Haute-Savoie', '74', 'Rhône-Alpes',
'Paris', '75', 'Ile-de-France',
'Seine-Maritime', '76', 'Haute-Normandie',
'Seine-et-Marne', '77', 'Ile-de-France',
'Yvelines', '78', 'Ile-de-France',
'Deux-Sèvres', '79', 'Poitou-Charentes',
'Somme', '80', 'Picardie',
'Tarn', '81', 'Midi-Pyrénées',
'Tarn-et-Garonne', '82', 'Midi-Pyrénées',
'Var', '83', 'Provence-Alpes-Côte d Azur',
'Vaucluse', '84', 'Provence-Alpes-Côte d Azur',
'Vendée', '85', 'Pays de la Loire',
'Vienne', '86', 'Poitou-Charentes',
'Haute-Vienne', '87', 'Limousin',
'Vosges', '88', 'Lorraine',
'Yonne', '89', 'Bourgogne',
'Territoire-de-Belfort', '90', 'Franche-Comté',
'Essonne', '91', 'Ile-de-France',
'Hauts-de-Seine', '92', 'Ile-de-France',
'Seine-Saint-Denis', '93', 'Ile-de-France',
'Val-de-Marne', '94', 'Ile-de-France',
'Val-d Oise','95','Ile-de-France']

DeptNumero=[ ]
DeptNom=[ ]
DeptNomRegion=[ ]
DeptPresence = [ ] #liste presence departement
i=0
j=0
k=0
col = 0
nb = int((len(Dept)/3)) #comptage du nb de departement
nbCol =5  #nombre de colonne pour affichage
ligne=0
colonne=0
    #création liste  numero departement
i=1
while i < len(Dept):
    DeptNumero.append(Dept[i])
    i = i + 3
   ##print (DeptNumero)

    
#création liste nom des departements
i=0
while i < len(Dept):
    DeptNom.append(Dept[i])
    i = i + 3
   ##print (DeptNom)

#création liste nom des regions
i=2
while i < len(Dept)/3:
    DeptNomRegion.append(Dept[i])
    i = i + 3
    ##print (DeptNomRegion)


  
if __name__ == '__main__':
    fen = Tk()

    fen.title('liste des '+str(nb)+' départements') #titre de la fenetre avec le nombre de département
    fen.geometry("900x600")
    fen.config(bg="white")

    tgl = Checkbar(fen, DeptNom)    
    tgl.config(relief=GROOVE, bd=2)
    tgl.grid(row=5,column=0)
    
    def allstates():
        print(list(tgl.state()))
               
        
    
    
    label_info = Label(fen, text="Cocher les cases pour valider la présence des départements",foreground="#000000",
          background="#FFFFFF",font="Courier 15 bold italic underline", padx="20", pady="4").grid(row=1,column=0)
    
    label_dept = Label(fen, text="Départements").grid(row=3,column=0, rowspan=1)
    case_vide(5,0)
              
   
    Button(fen, text='Suivant', command=fen.destroy).grid(row = 8, column = 0,  padx =300, pady =0, sticky =W)
    Button(fen, text='valider présences', command=allstates).grid(row = 8, column = 0,  padx =10, pady =0, sticky =W)
    
    fen.mainloop()


#fen2=Tk()
#fen2.title('list des'+str(nb)+' départements sélectionnés')
#fen2.geometry("900x600")
#fen2.config(bg="grey")

SelectDept=[]
i = 0
while i < 96:
    if DeptNom[i] in list(tgl.state()):
        print (DeptNom[i])
        SelectDept.append(DeptNom[i])
        #SelectDept.append(DeptNumero[i])
        #SelectDept.append(DeptNomRegion[i])
    i=i+1
    
#Label(fen2, text='Les sélectionnés et la répartissions dans les stades').pack()


class Application:
    def __init__(self, ligne, colonne):
        fen2=Tk()
        fen2.title('Répartition stade avec les '+str(len(SelectDept))+' équipes sélectionnées')
        fen2.geometry("600x300")
        fen2.config(bg="white")
        Dept=SelectDept
        for k in range(colonne):
            b=Button(fen2, text='Stade'+str(k+1), width=10) # titre des colonnes + taille
            b.grid(row=0,column=k+1,sticky=NSEW) # tête de colonne
        fen2.grid_rowconfigure(10, weight=1)
        #for m in range(ligne): # inutile
            #b=Button(self.root, text=str(m+1), width=10) #titre lignes + taille
            #b.grid(row=m+1,column=0,sticky=NSEW)
        #self.root.grid_rowconfigure(0, weight=1)
        #self.root.grid_columnconfigure(1, weight=1)
        
        rows = []
        s=0 #variable pour affichage des dept selectionne
        for i in range(ligne):
            cols = []
            for j in range(colonne):
                e = Entry(fen2, justify=CENTER)
                e.grid(row=i+1, column=j+1, sticky=NSEW) #decalage des lignes et colonnes
                e.insert(END, SelectDept[s]) # affiche chaque dept
                cols.append(e)
                fen2.grid_columnconfigure(j, weight=1)
                print (rows)
                s+=1
            fen2.grid_rowconfigure(i+1, weight=1)
            rows.append(cols)

        for k in range(colonne):
            b=Button(fen2, text='Stade'+str(k+6), width=10) # titre des colonnes + taille
            b.grid(row=10,column=k+1,sticky=NSEW)
        fen2.grid_rowconfigure(10, weight=1)
        for m in range(ligne):
            b=Button(fen2, text=str(m+1), width=10) #titre lignes + taille
            #b.grid(row=m+1,column=0,sticky=NSEW) # enlève les n° des lignes
        fen2.grid_rowconfigure(0, weight=1)
        fen2.grid_columnconfigure(0, weight=1)

        rows = []
        
        for i in range(ligne):
            cols = []
            for j in range(colonne):
                e = Entry(fen2, justify=CENTER)
                e.grid(row=i+11, column=j+1, sticky=NSEW) #decalage des lignes et colonnes ici on repart sur la 11 ème ligne
                e.insert(END, SelectDept[s]) # i egale premier chiffre et j deuxième chiffre
                cols.append(e)
                fen2.grid_columnconfigure(j, weight=1)
                print (rows)
                s+=1 
            fen2.grid_rowconfigure(i+1, weight=1)
            rows.append(cols)

        Button(fen2, text='Suivant', command=fen2.destroy).grid(row = 20, column = 1,  padx =0, pady =0, sticky =W)
        fen2.mainloop()
 
 
# départ de l'affichage des listes par stade :
if __name__ == "__main__":
    f = Application(2,2) # défini le nombre de lignes et de colonnes par stade ! il faut en tout 25 stade !!!!


fen3 = Tk()

fen3.title('liste des '+str(len(SelectDept))+' départements') #titre de la fenetre avec le nombre de département
fen3.geometry("900x600")
fen3.config(bg="white")

tgl2 = Checkbar(fen3, SelectDept)    
tgl2.config(relief=GROOVE, bd=2)
tgl2.grid(row=15,column=2)



Resultat = Label(fen3, text='bonjou', fg='red')
Resultat.pack()

fen3.mainloop()

#print (SelectDept)
#i=0
#total = (len(SelectDept)*2)
#while i < total:
 #   point = input("Quel est le résultat de l équipe "+SelectDept[i])
  #  SelectDept.insert(i+1, point)
  #  i+=2
#print (SelectDept)

