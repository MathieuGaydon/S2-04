from faker import Faker
fake = Faker()
import random

#On s'assure de vider le fichier d'insertion des données
with open("resultat.txt","w") as file:
    file.write("--Insertion des données dans la base : " + "\n")

    #--------------------------------Tenrac----------------------------------------
    
    Tenrac = []
    def prenom():
        fin = ''
        name = fake.name()
        i = 0
        while(name[i] != ' '):
            fin += name[i]
            i += 1
        return fin
    
    def nom():
        fin = ''
        name = fake.name()
        i = 0
        while(name[i] != ' '):
            i += 1    
        for j in range(i+1,len(name)):
            fin += name[j]
        return fin
    
    Grades_possibles = ['Affilié', 'Sympathisant', 'Adhérent', 'Chevalier / Dame', 'Grand Chevalier / HauteDame', 'Commandeur', "Grand’Croix"] 
    Rang_possibles = ['Novice','Compagnon']
    Titres_possibles = ['Philantrope','Protecteur','Honorable']
    Dignités_possibles = ['Maître','Grand chancelier','Grand Maître']
    
    list_numer = []
    list_ref = []
    list_cod = []
    for i in range(1,10):
            numero = i
            list_numer.append(numero)
            refOrganisme = fake.random_digit()+1
            list_ref.append(refOrganisme)
            Code_membre = fake.unique.random_int(1000,9999,1)
            list_cod.append(Code_membre)
            Nom = nom()
            Prenom = prenom()
            courriel = fake.company_email()
            numeroTel = fake.phone_number()                                                                                                                                                                                             
            adresse_postale = fake.address().replace("\n", ", ")
            grade = fake.random_element(elements=Grades_possibles)
            dignite = fake.random_element(elements=Dignités_possibles)
            titre = fake.random_element(elements=Titres_possibles)
            rang = fake.random_element(elements=Rang_possibles)
            file.write("INSERT INTO Tenrac(numero,refOrganisme,codeMembre,nom,prenom,courriel,numeroTel,adressePostale,grade,dignite,titre,rang) VALUES " + "\n" + "(" 
                       + str(numero) + ',' + str(refOrganisme) + ',' + str(Code_membre) + ',' 
                       + "'" + Nom + "'" + ',' + "'" + Prenom + "'" + ',' + "'" + courriel + "'" + ',' + "'" + numeroTel + "'" 
                       + ',' + "'" + adresse_postale + "'" + ',' + "'" + grade + "'" + ',' 
                       + "'" + dignite + "'" + ',' + "'" + titre + "'" + ',' + "'" + rang + "'" 
                       + ")" + "\n")
    list_numer = tuple(list_numer)
    list_ref = tuple(list_ref)
    list_cod = tuple(list_cod)
    #-----------------------Organisme-----------------------------------------------
    
    
    Type_org_possible = ["Entreprise","Association","Organisme de formation"]
    mots = ["Raclette","Poulet","PouletFrit","Tenders","Legume","Sauce","Kebab","Pizza","Quiche","Saumon","Ananas","Beurre"]
    
    def raisons_soc():
        fin = ''
        nb_alet = random.randint(1, 3)
        for i in range(nb_alet):
            fin += fake.random_element(elements=mots)
        return fin    
    
    def num_siret():
        fin = ''
        for i in range(14):
            fin += str(random.randint(1, 9))
        return fin
        
    for i in range(10):
        RefOrganisme = fake.unique.random_int(1,1000,1)
        TypeOrganisme = fake.random_element(elements=Type_org_possible)
        Raisons_sociale = raisons_soc()
        numero_SIRET = num_siret()
        #On met les Insert into dans un fichier 
        file.write("INSERT INTO Organisme(refOrganisme,typeOrganisme,raisonSociale,numeroSIRET) VALUES (" 
                   + str(RefOrganisme) + ',' + "'" + TypeOrganisme + "'" + ',' + "'" 
                   + Raisons_sociale + "'" + ',' + str(numero_SIRET) + ")" + "\n")
        
    
    #--------------------------Date------------------------------------------------
    Date=[]
    for i in range(10):
        dat = fake.date()
        Date.append(dat)
        file.write("INSERT INTO Date(date_) VALUES (" + "TO_DATE('" + dat + "','YYYY-MM-DD' )" +  ")" + "\n")
            
    #------------------------Organisation------------------------------------------
    list_num = []
    for i in range(50):
        num = fake.unique.random_int(1,1000,1);
        list_num.append(num)
        file.write("INSERT INTO Organisation(numero) VALUES (" + str(num) + ")" + "\n")
    nv_list_num = tuple(list_num)
    #-------------------------Entretien--------------------------------------------
    
    Entretients_possibles = ["mécanique","désinfectant","dégraissant","détergent","à l'eau"]
    list_E = []
    for i in range(10):
        idEntretient = i
        list_E.append(idEntretient)
        periodeEntretien = fake.date()
        typeEntretien = fake.random_element(elements=Entretients_possibles)
        numero = fake.random_element(elements=nv_list_num)
        file.write("INSERT INTO Entretien(idEntretient,periodeEntretien,typeEntretien,numero) VALUES (" + str(idEntretient) + "," + "TO_DATE('YYYY-MM-DD', '" 
                   + periodeEntretien + "')" + "," + "'" + typeEntretien + "'" + "," + str(numero) + ")" + "\n")
    list_E = tuple(list_E)
    #------------------------------Club--------------------------------------------
    
    mots_en_plus = ["Raclette","Poulet","Tenders","Legume","Sauce","Kebab","Pizza","Quiche","Saumon","Ananas","Beurre","Divin","Goutu","Délicieux","A se damner"]
    
    def nomclub():
        fin = ''
        nb_alet = random.randint(1, 3)
        for i in range(nb_alet):
            fin += fake.random_element(elements=mots_en_plus)
        return fin   
    
    for i in range(10):
        numero1 = fake.unique.random_element(elements=nv_list_num)
        nomClub = nomclub()
        numero = fake.random_element(elements=nv_list_num)
        file.write("INSERT INTO Club(numero_1,nomClub,numero) VALUES (" + str(numero1) + "," + "'" + nomClub + "'" + "," + str(numero) + ")" + "\n") 
     
    #------------------------------Ordre-------------------------------------------
    
    nom_Ordre = ["Enjoyers","Amateurs de ","Apprécieurs de ","Kiffeurs de "]
    
    for i in range(10):
        numero = fake.unique.random_element(elements=nv_list_num)
        nomOrdre = fake.random_element(elements=nom_Ordre) + fake.random_element(elements=mots)
        file.write("INSERT INTO Ordre(numero,nomOrdre) VALUES (" + str(numero) + "," + "'" + nomOrdre + "'" + ")" + "\n")
    
    #-------------------------------Partenaire-------------------------------------
    
    adresses = []
    for i in range(10):
        adresse = fake.address().replace("\n", ", ")
        adresses.append(adresses)
        numero = fake.random_element(elements=nv_list_num)
        file.write("INSERT INTO Partenaire(adresse, numero) VALUES (" + "'" + adresse + "'" + "," + str(numero) + ")" + "\n")
    
    #--------------------------------Modele----------------------------------------
    
    for i in range(10):
        idModele = fake.random_int(1,100,1)
        nomModele = fake.random_letter() + fake.random_letter() + ' ' + str(fake.random_digit()) + str(fake.random_digit()) + str(fake.random_digit())
        idEntretient = fake.random_element(elements=list_E)
        file.write("INSERT INTO Modele(idModele,nomModele,idEntretient) VALUES (" + str(idModele) + "," + "'" + nomModele + "'" + "," + str(idEntretient) 
                   + ")" + "\n")
      
    #--------------------------------Reunion---------------------------------------
    num_reunion_list=[]
    for i in range(10):
        idReunion = fake.unique.random_int(1,100,1)
        numero = fake.random_element(elements=list_numer)
        refOrganisme = fake.random_element(elements=list_ref)
        codeMembre = fake.random_element(elements=list_cod)
        num_reunion_list.append(idReunion)
        file.write("INSERT INTO Reunion(idReunion,numero,refOrganisme,codeMembre) VALUES (" + str(idReunion) + "," + str(numero) + "," 
                   + str(refOrganisme) + "," + str(codeMembre) + ")" + "\n")
 
    #--------------------------Date------------------------------------------------
    Date = []
    for i in range(10):
        dat = [
            fake.date()
            ]
        Date.append(dat)
        
        
    #--------------Repas----------
    nom_repas_possible=["Petit-Déjeuner","Déjeuner","Goûter","Dîner", "Encas"]
    num_repas_list=[]
    for i in range(10):
        idRepas = fake.unique.random_int(1,1000,1)
        nomRepas = fake.random_element(elements=nom_repas_possible)
        num_repas_list.append(idRepas)
        #On met les Insert into dans un fichier 
        file.write("INSERT INTO Repas(idRepas,nomRepas) VALUES (" 
                   + str(idRepas) + ',' + "'" + nomRepas + "'" + ")" + "\n")
           
    #--------------Legume----------
    nom_legume_possible=["Ail", "Brocoli", "Carotte", "Chou Rouge", "Epinard", "Maïs", "Melon", "Oignon", "Pomme de terre", "Radis", "Tomate", "Topinambour"]
    num_legume_list=[]
    for i in range(10):
        idLegume = fake.unique.random_int(1,1000,1)
        nomLegume = fake.random_element(elements=nom_legume_possible)
        num_legume_list.append(idLegume)
        #On met les Insert into dans un fichier 
        file.write("INSERT INTO Legume(idLegume,nomLegume) VALUES (" 
                   + str(idLegume) + ',' + "'" + nomLegume + "'" + ")" + "\n")
           
    #--------------Plat----------
    nom_plat_possible=["Tenders", "Kebab", "Pizza", "Quiche", "Saumon", "Ananas", "Beurre", "Raclette", "Pasta Carbonara", "Poulet", "Fondue savoyarde", "Choucroute", "Foie gras"]
    num_plat_list=[]
    for i in range(10):
        idPlat = fake.unique.random_int(1,1000,1)
        nomPlat = fake.random_element(elements=nom_plat_possible)
        idLegume = fake.random_element(elements=num_legume_list)
        num_plat_list.append(idPlat)
        #On met les Insert into dans un fichier 
        file.write("INSERT INTO Plat(idPlat,nomPlat,idLegume) VALUES (" 
                   + str(idPlat) + ',' + "'" + nomPlat + "'" + ',' + str(idLegume) + ")" + "\n")
            
    #--------------Sauce----------
    nom_sauce_possible=["Mayonnaise", "Blanche", "Moutarde", "Sauce du chef", "Ketchup", "Beurre", "BBQ", "Tartare", "Poivre", "Pesto", "Sauce Fromagère"]
    num_sauce_list=[]
    for i in range(10):
        idSauce = fake.unique.random_int(1,1000,1)
        nomSauce = fake.random_element(elements=nom_sauce_possible)
        num_sauce_list.append(idSauce)
        #On met les Insert into dans un fichier 
        file.write("INSERT INTO Sauce(idSauce,nomSauce) VALUES (" 
                   + str(idSauce) + ',' + "'" + nomSauce + "'" + ")" + "\n")
            
    #--------------Ingredient----------
    nom_ingredient_possible=["Poulet pané", "Fromage à raclette", "Reblochon", "Lardons", "Bacon", "Guanciale", "Pâtes", "Boeuf", "Poisson", "Saucisse"]
    num_ingredient_list=[]
    for i in range(10):
        idIngredient = fake.unique.random_int(1,1000,1)
        nomIngredient = fake.random_element(elements=nom_ingredient_possible)
        num_ingredient_list.append(idIngredient)
        #On met les Insert into dans un fichier 
        file.write("INSERT INTO Ingredient(idIngredient,nomIngredient) VALUES (" 
                   + str(idIngredient) + ',' + "'" + nomIngredient + "'" + ")" + "\n")
    
    #--------------Aliment----------
    nom_aliment_possible=["Pain", "Tenders", "Frites", "Cheddar", "Sel", "Huile", "Lait"]
    num_aliment_list=[]
    for i in range(10):
        idAliment = fake.unique.random_int(1,1000,1)
        nomAliment = fake.random_element(elements=nom_aliment_possible)
        num_aliment_list.append(idAliment)
        #On met les Insert into dans un fichier 
        file.write("INSERT INTO Aliment(idAliment,nomAliment) VALUES (" 
                   + str(idAliment) + ',' + "'" + nomAliment + "'" + ")" + "\n")
    
    #--------------Compose----------
    for i in range(10):
        idRepas = fake.random_element(elements=num_repas_list)
        idPlat = fake.random_element(elements=num_plat_list)
        #On met les Insert into dans un fichier 
        file.write("INSERT INTO Compose(idRepas,idPlat) VALUES (" 
                   + str(idRepas) + ',' + str(idPlat) + ")" + "\n")
    
    #--------------Constitue----------
    for i in range(10):
        idPlat = fake.random_element(elements=num_plat_list)
        idAliment = fake.random_element(elements=num_aliment_list)
        #On met les Insert into dans un fichier 
        file.write("INSERT INTO Constitue(idPlat,idAliment) VALUES (" 
                   + str(idPlat) + ',' + str(idAliment) + ")" + "\n")
            
    #--------------Accompagne----------
    for i in range(10):
        idPlat = fake.random_element(elements=num_plat_list)
        idSauce = fake.random_element(elements=num_sauce_list)
        #On met les Insert into dans un fichier 
        file.write("INSERT INTO Accompagne(idPlat,idSauce) VALUES (" 
                   + str(idPlat) + ',' + str(idSauce) + ")" + "\n")
    
    #--------------forme----------
    for i in range(10):
        idSauce = fake.random_element(elements=num_sauce_list)
        idIngredient = fake.random_element(elements=num_ingredient_list)
        #On met les Insert into dans un fichier 
        file.write("INSERT INTO forme(idSauce,idIngredient) VALUES (" 
                   + str(idSauce) + ',' + str(idIngredient) + ")" + "\n")
            
    '''#--------------Mange----------
    for i in range(10):
        date = fake.random_element(elements=Date)
        idReunion = fake.random_element(elements=num_reunion_list)
        idRepas = fake.random_element(elements=num_repas_list)
        #On met les Insert into dans un fichier 
        file.write("INSERT INTO Mange(date_,idReunion,idRepas) VALUES ( TO_DATE('" 
                   + date + "','YYYY-MM-DD' )" + ',' + str(idReunion) + ',' + str(idRepas) + ")" + "\n")'''
        
    '''#--------------Utilisation Officielle----------
    for i in range(10):
        idRepas = fake.random_element(elements=num_repas_list)

        #On met les Insert into dans un fichier 
        file.write("INSERT INTO forme(date_,idPlat,idAliment) VALUES (" 
                   + str(date_) + ',' + str(idRepas) + ")" + "\n")'''