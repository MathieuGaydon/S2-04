from faker import Faker
fake = Faker()
import random
import csv

#On s'assure de vider le fichier d'insertion des données
with open("resultat.txt","w") as file, open("resultat.csv","w", newline='' ,encoding='utf-8') as file2:
    file.write("--Insertion des données dans la base : " + "\n")
    writer = csv.writer(file2, delimiter=',')

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
   
    Grades_possibles = ['Affilié', 'Sympathisant', 'Adhérent']
    Grades_Supérieurs = ['Chevalier / Dame', 'Grand Chevalier / HauteDame', 'Commandeur', "Grand’Croix"]
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
           grade = ''
           gradesup = ''
           if(i%2 == 0):
               gradeSup = fake.random_element(elements=Grades_Supérieurs)
               grade = 'NULL'
           else : 
               grade = fake.random_element(elements=Grades_possibles)
               gradeSup = 'NULL'
           dignite = fake.random_element(elements=Dignités_possibles)
           titre = fake.random_element(elements=Titres_possibles)
           rang = fake.random_element(elements=Rang_possibles)
           text = f"INSERT INTO Tenrac(numero,refOrganisme,codeMembre,nom,prenom,courriel,numeroTel,adressePostale,gradeSuperieur,grade,dignite,titre,rang) VALUES \n({numero},{refOrganisme},{Code_membre},'{Nom}','{Prenom}','{courriel}','{numeroTel}','{adresse_postale}','{gradeSup}','{grade}','{dignite}','{titre}','{rang}');\n"
           file.write(text)
           writer.writerow([numero,refOrganisme,Code_membre,Nom,Prenom,courriel,numeroTel,adresse_postale,gradeSup,grade,dignite,titre,rang])
           
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
       textOrg = f"INSERT INTO Organisme(refOrganisme,typeOrganisme,raisonSociale,numeroSIRET) VALUES ({RefOrganisme},'{TypeOrganisme},'{Raisons_sociale}','{numero_SIRET}');\n"
       file.write(textOrg)
       writer.writerow([RefOrganisme,TypeOrganisme,Raisons_sociale,numero_SIRET])
   
    #--------------------------Date------------------------------------------------
    Date=[]
    for i in range(10):
       dat = fake.date()
       Date.append(dat)
       textDate = f"INSERT INTO Date_(date) VALUES (TO_DATE('{dat}','YYYY-MM-DD'));\n"
       file.write(textDate)
       writer.writerow([dat])
    Date = tuple(Date)
   
    #------------------------Organisation------------------------------------------
    list_num = []
    for i in range(50):
       num = fake.unique.random_int(1,1000,1);
       list_num.append(num)
       textOrga = f"INSERT INTO Organisation(numero) VALUES ({num});\n"
       file.write(textOrga)
       writer.writerow([num])
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
       textEntre = f"INSERT INTO Entretien(idEntretient,periodeEntretient,typeEntretient,numero) VALUES ({idEntretient},TO_DATE('{periodeEntretien}''YYYY-MM-DD'),'{typeEntretien}',{numero});\n"
       file.write(textEntre)
       writer.writerow([idEntretient,periodeEntretien,typeEntretien,numero])
    list_E = tuple(list_E)
   
    #------------------------------Club--------------------------------------------
   
    mots_en_plus = ["Raclette","Poulet","Tenders","Legume","Sauce","Kebab","Pizza","Quiche","Saumon","Ananas","Beurre","Divin","Goutu","Délicieux","A se damner"]
    list_numer1 = []
    def nomclub():
       fin = ''
       nb_alet = random.randint(1, 3)
       for i in range(nb_alet):
           fin += fake.random_element(elements=mots_en_plus)
       return fin   
   
    for i in range(10):
       numero1 = fake.unique.random_element(elements=nv_list_num)
       list_numer1.append(numero1)
       nomClub = nomclub()
       numero = fake.random_element(elements=nv_list_num)
       textClub = f"INSERT INTO Club(numero_1,nomClub,numero) VALUES ({numero1},'{nomClub}',{numero});\n"
       file.write(textClub)
       writer.writerow([numero1,nomClub,numero])
   
    #------------------------------Ordre-------------------------------------------
   
    nom_Ordre = ["Enjoyers","Amateurs de ","Apprécieurs de ","Kiffeurs de "]
   
    for i in range(10):
       numero = fake.unique.random_element(elements=nv_list_num)
       nomOrdre = fake.random_element(elements=nom_Ordre) + fake.random_element(elements=mots)
       textOrdre = f"INSERT INTO Ordre(numero,nomOrdre) VALUES ({numero},'{nomOrdre}');\n"
       writer.writerow([numero,nomOrdre])
   
    #-------------------------------Partenaire-------------------------------------
   
    adresses = []
    for i in range(10):
       adresse = fake.address().replace("\n", ", ")
       adresses.append(adresse)
       numero = fake.random_element(elements=nv_list_num)
       textPart = f"INSERT INTO Partenaire(adresse,numero) VALUES ('{adresse}',{numero});\n"
       file.write(textPart)
       writer.writerow([adresse,numero])
   
    #--------------------------------Modele----------------------------------------
    num_modele_list = []
    for i in range(10):
       idModele = fake.random_int(1,100,1)
       num_modele_list.append(idModele)
       nomModele = fake.random_letter() + fake.random_letter() + ' ' + str(fake.random_digit()) + str(fake.random_digit()) + str(fake.random_digit())
       idEntretient = fake.random_element(elements=list_E)
       textModele = f"INSERT INTO Modele(idModele,nomModele,idEntretient) VALUES ({idModele},'{nomModele}',{idEntretient});\n"
       file.write(textModele)
       writer.writerow([idModele,nomModele,idEntretient])
   
    #--------------------------------Reunion---------------------------------------
    num_reunion_list=[]
    for i in range(10):
       idReunion = fake.unique.random_int(1,100,1)
       numero = fake.random_element(elements=list_numer)
       refOrganisme = fake.random_element(elements=list_ref)
       codeMembre = fake.random_element(elements=list_cod)
       num_reunion_list.append(idReunion)
       textReu = f"INSERT INTO Reunion(idReunion,numero,refOrganisme,codeMembre) VALUES ({idReunion},{numero},{refOrganisme},{codeMembre});\n"
       file.write(textReu)
       writer.writerow([idReunion])
    num_reunion_list = tuple(num_reunion_list)
   
    #--------------Repas----------
    nom_repas_possible=["Petit-Déjeuner","Déjeuner","Goûter","Dîner", "Encas"]
    num_repas_list=[]
    for i in range(10):
       idRepas = fake.unique.random_int(1,1000,1)
       nomRepas = fake.random_element(elements=nom_repas_possible)
       num_repas_list.append(idRepas)
       #On met les Insert into dans un fichier 
       textRepas = f"INSERT INTO Repas(idRepas,nomRepas) VALUES ({idRepas},'{nomRepas}');\n"
       file.write(textRepas)
       writer.writerow([idRepas,nomRepas])
   
    #--------------Legume----------
    nom_legume_possible=["Ail", "Brocoli", "Carotte", "Chou Rouge", "Epinard", "Maïs", "Melon", "Oignon", "Pomme de terre", "Radis", "Tomate", "Topinambour"]
    num_legume_list=[]
    for i in range(10):
       idLegume = fake.unique.random_int(1,1000,1)
       nomLegume = fake.random_element(elements=nom_legume_possible)
       num_legume_list.append(idLegume)
       #On met les Insert into dans un fichier 
       textLegume = f"INSERT INTO Legume(idLegume,nomLegume) VALUES ({idLegume},'{nomLegume}');\n"
       file.write(textLegume)
       writer.writerow([idLegume,nomLegume])
    num_legume_list = tuple(num_legume_list)
   
    #--------------Plat----------
    nom_plat_possible=["Tenders", "Kebab", "Pizza", "Quiche", "Saumon", "Ananas", "Beurre", "Raclette", "Pasta Carbonara", "Poulet", "Fondue savoyarde", "Choucroute", "Foie gras"]
    num_plat_list=[]
    for i in range(10):
       idPlat = fake.unique.random_int(1,1000,1)
       nomPlat = fake.random_element(elements=nom_plat_possible)
       idLegume = fake.random_element(elements=num_legume_list)
       num_plat_list.append(idPlat)
       #On met les Insert into dans un fichier 
       textPlat = f"INSERT INTO Plat(idPlat,nomPlat,idLegume) VALUES ({idPlat},'{nomPlat}',{idLegume});\n"
       file.write(textPlat)
       writer.writerow([idPlat,nomPlat,idLegume])
   
    #--------------------------------Sauce-------------------------------------
    nom_sauce_possible=["Mayonnaise", "Blanche", "Moutarde", "Sauce du chef", "Ketchup", "Beurre", "BBQ", "Tartare", "Poivre", "Pesto", "Sauce Fromagère"]
    num_sauce_list=[]
    for i in range(10):
       idSauce = fake.unique.random_int(1,1000,1)
       nomSauce = fake.random_element(elements=nom_sauce_possible)
       num_sauce_list.append(idSauce)
       #On met les Insert into dans un fichier 
       textSauce = f"INSERT INTO Sauce(idSauce,nomSauce) VALUES ({idSauce},'{nomSauce}');\n"
       file.write(textSauce)
       writer.writerow([idSauce,nomSauce])
   
    #---------------------------------------Ingredient-------------------------
    nom_ingredient_possible=["Poulet pané", "Fromage à raclette", "Reblochon", "Lardons", "Bacon", "Guanciale", "Pâtes", "Boeuf", "Poisson", "Saucisse"]
    num_ingredient_list=[]
    for i in range(10):
       idIngredient = fake.unique.random_int(1,1000,1)
       nomIngredient = fake.random_element(elements=nom_ingredient_possible)
       num_ingredient_list.append(idIngredient)
       #On met les Insert into dans un fichier 
       textIngredient = f"INSERT INTO Ingredient(idIngredient,nomIngredient) VALUES ({idIngredient},'{nomIngredient}');\n"
       file.write(textIngredient)
       writer.writerow([idIngredient,nomIngredient])
   
    #------------------------------------------Aliment-------------------------
    nom_aliment_possible=["Pain", "Tenders", "Frites", "Cheddar", "Sel", "Huile", "Lait"]
    num_aliment_list=[]
    for i in range(10):
       idAliment = fake.unique.random_int(1,1000,1)
       nomAliment = fake.random_element(elements=nom_aliment_possible)
       num_aliment_list.append(idAliment)
       #On met les Insert into dans un fichier 
       textAliment = f"INSERT INTO Aliment(idAliment,nomAliment) VALUES ({idAliment},'{nomAliment}');\n"
       file.write(textAliment)
       writer.writerow([idAliment,nomAliment])
   
    #------------------------------------Compose------------------------------
    for i in range(10):
       idRepas = fake.random_element(elements=num_repas_list)
       idPlat = fake.random_element(elements=num_plat_list)
       #On met les Insert into dans un fichier 
       textCompo = f"INSERT INTO Compose(idRepas,idPlat) VALUES ({idRepas},{idPlat});\n"
       file.write(textCompo)
       writer.writerow([idRepas,idPlat])
   
    #------------------------------------Constitue----------------------------
    for i in range(10):
       idPlat = fake.random_element(elements=num_plat_list)
       idAliment = fake.random_element(elements=num_aliment_list)
       #On met les Insert into dans un fichier 
       textConstitue = f"INSERT INTO Constitue(idPlat,idAliment) VALUES ({idPlat},{idAliment});\n"
       file.write(textConstitue)
       writer.writerow([idPlat,idAliment])
   
    #------------------------------------Accompagne----------------------------
    for i in range(10):
       idPlat = fake.random_element(elements=num_plat_list)
       idSauce = fake.random_element(elements=num_sauce_list)
       #On met les Insert into dans un fichier 
       textAcc = f"INSERT INTO Accompagne(idPlat,idSauce) VALUES ({idPlat},{idSauce});\n"
       file.write(textAcc)
       writer.writerow([idPlat,idSauce])
       
    #---------------------------------------forme------------------------------
    for i in range(10):
       idSauce = fake.random_element(elements=num_sauce_list)
       idIngredient = fake.random_element(elements=num_ingredient_list)
       #On met les Insert into dans un fichier 
       textForme = f"INSERT INTO forme(idSauce,idIngredient) VALUES ({idSauce},{idIngredient});\n"
       file.write(textForme)
       writer.writerow([idSauce,idIngredient])
   
    #--------------Mange----------
    for i in range(10):
       date = fake.random_element(elements=Date)
       idReunion = fake.random_element(elements=num_reunion_list)
       idRepas = fake.random_element(elements=num_repas_list)
       #On met les Insert into dans un fichier 
       textMange = f"INSERT INTO Mange(date_,idReunion,idRepas) VALUES (TO_DATE('{date}','YYYY-MM-DD'),{idReunion},{idRepas});\n"
       file.write(textMange)
       writer.writerow([date,idReunion,idRepas])
       
    #------------------Machine-------------------------------------------------
    Machines_possibles = ["familiale","individuelle","multifonction","combinée","mini raclette","de table","electrique","bon marché","traditionnelle","pierrade-fondue"]
    num_machine_list = []
    for i in range(10):
       idMachine = i
       num_machine_list.append(idMachine)
       nomMachine = fake.random_element(elements=Machines_possibles)
       textMachine = f"INSERT INTO Machine(idMachine,nomMachine) VALUES ({idMachine},'{nomMachine}');\n"
       file.write(textMachine)
       writer.writerow([idMachine,nomMachine])
       
    #--------------------------------Utilisation Officielle----------------------
    for i in range(10):
       idRepas = fake.random_element(elements=num_repas_list)
       idMachine = fake.random_element(elements=num_machine_list)
       #On met les Insert into dans un fichier 
       textUtil = f"INSERT INTO UtilisationOfficielle(idRepas,idMachine) VALUES ({idRepas},TO_DATE('{date}','YYYY-MM-DD'));\n"
       file.write(textUtil)
       writer.writerow([idRepas,idMachine])
   
    #-----------------------------Intolerance----------------------------------
    for i in range(10):
       numero = fake.random_int(1,100)
       refOrganisme = fake.random_element(elements=list_numer)
       codeMembre = fake.random_element(elements=list_cod)
       idLegume = fake.random_element(elements=num_legume_list)
       textIntolerance = f"INSERT INTO Intolerance(numero,refOrganisme,codeMembre,idLegume) VALUES ({numero},{refOrganisme},{codeMembre},{idLegume});\n"
       file.write(textIntolerance)
       writer.writerow([numero,refOrganisme,codeMembre,idLegume])
   
    #-------------------------------------Dirige-------------------------------
    for i in range(10):
       refOrganisme = fake.random_element(elements=list_numer)
       codeMembre = fake.random_element(elements=list_cod)
       idLegume = fake.random_element(elements=num_legume_list)
       idReunion = fake.random_element(elements=num_reunion_list)
       textDirige = f"INSERT INTO Dirige(numero,refOrganisme,codeMembre,idReunion) VALUES ({refOrganisme},{codeMembre},{idLegume},{idReunion});\n"
       file.write(textDirige)
       writer.writerow([numero,refOrganisme,codeMembre,idReunion])
   
    #-----------------------------------Enregistre1----------------------------
    for i in range(10):
       numero = fake.random_element(elements=list_numer1)
       idEntretient = fake.random_element(elements=list_E)
       textEnr1 = f"INSERT INTO Enregistre1(numero,idEntretient) VALUES ({numero},{idEntretient});\n"
       file.write(textEnr1)
       writer.writerow([numero,idEntretient])
          
    #------------------SeGroupe------------------------------------------------
    for i in range(10):
       adresse=fake.random_element(elements=adresses)
       date=fake.random_element(elements=Date)
       idReunion=fake.random_element(elements=num_reunion_list)
       textSeGroupe=f"INSERT INTO SeGroupe(adresse,date_,idReunion) VALUES ({adresse}, {date}, {idReunion});\n"
       file.write(textSeGroupe)
       writer.writerow([adresse,date,idReunion])
              
    #------------------Rejoint--------------------------------------------------
    for i in range(10):
       numero=fake.random_element(elements=list_numer)
       refOrganisme=fake.random_element(elements=list_ref)
       codeMembre=fake.random_element(elements=list_cod)
       idReunion=fake.random_element(elements=num_reunion_list)
       textRejoint=f"INSERT INTO Rejoint(numero,refOrganisme,codeMembre,idReunion) VALUES ({numero}, {refOrganisme}, {codeMembre}, {idReunion});\n"
       file.write(textRejoint)
       writer.writerow([numero,refOrganisme,codeMembre,idReunion])
     	 
    #------------------Caracterise--------------------------------------------
    for i in range(10):
       idMachine=fake.random_element(elements=num_machine_list)
       idModele=fake.random_element(elements=num_modele_list)
       textCaracterise=f"INSERT INTO Caracterise(idMachine,idModele) VALUES ({idMachine}, {idModele});\n"
       file.write(textCaracterise) 
       writer.writerow([idMachine,idModele])
  	 
    #-----------------Realise-------------------------------------------------
    for i in range(10):
       numero=fake.random_element(elements=list_numer)
       refOrganisme=fake.random_element(elements=list_ref)
       codeMembre=fake.random_element(elements=list_cod)
       idMachine=fake.random_element(elements=num_machine_list)
       id_Entretient=fake.random_element(elements=list_E)
       textRealise=f"INSERT INTO Realise(numero,refOrganisme,codeMembre,idMachine,idEntretient) VALUES ({numero}, {refOrganisme}, {codeMembre}, {idMachine}, {id_Entretient});\n"
       file.write(textRealise)
       writer.writerow([numero,refOrganisme,codeMembre,idMachine,id_Entretient])
   
        
print("Script éxécuté")