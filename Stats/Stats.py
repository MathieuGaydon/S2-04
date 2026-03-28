from faker import Faker
fake = Faker()
import random
import csv

#On s'assure de vider le fichier d'insertion des données

#-----------------------Organisme-----------------------------------------------
with open("Organisme.csv","w", newline='' ,encoding='utf-8') as Organisme:
    writer = csv.writer(Organisme, delimiter=',')
    Organisme.write("Organisme"+ "\n")
    writer.writerow(['refOrganisme','typeOrganisme','raisonSociale','numeroSIRET'])
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
       
    for i in range(100):
       RefOrganisme = fake.unique.random_int(1,1000,1)
       TypeOrganisme = fake.random_element(elements=Type_org_possible)
       Raisons_sociale = raisons_soc()
       numero_SIRET = num_siret()
       #On met les Insert into dans un fichier 
       writer.writerow([RefOrganisme,TypeOrganisme,Raisons_sociale,numero_SIRET])

#------------------------Organisation------------------------------------------
with open("Organisation.csv","w", newline='' ,encoding='utf-8') as Organisation:
    writer = csv.writer(Organisation, delimiter=',')
    Organisation.write("Organisation"+ "\n")
    writer.writerow(['numero'])
    list_num = []
    for i in range(1000):
       num = fake.unique.random_int(1,1200,1);
       list_num.append(num)
       writer.writerow([num])
    nv_list_num = tuple(list_num)

#--------------------------Date------------------------------------------------
with open("Date.csv","w", newline='' ,encoding='utf-8') as Date:
    writer = csv.writer(Date, delimiter=',')
    Date.write("Date"+ "\n")
    writer.writerow(['date_'])
    Date=[]
    for i in range(500):
       dat = fake.date()
       Date.append(dat)
       writer.writerow([dat])
    Date = tuple(Date)

#--------------Repas----------
with open("Repas.csv","w", newline='' ,encoding='utf-8') as Repas:
    writer = csv.writer(Repas, delimiter=',')
    Repas.write("Repas"+ "\n")
    writer.writerow(['idRepas','nomRepas'])
    nom_repas_possible=["Petit-Déjeuner","Déjeuner","Goûter","Dîner", "Encas"]
    num_repas_list=[]
    for i in range(5000):
       idRepas = fake.unique.random_int(1,5100,1)
       nomRepas = fake.random_element(elements=nom_repas_possible)
       num_repas_list.append(idRepas)
       #On met les Insert into dans un fichier 
       writer.writerow([idRepas,nomRepas])

#------------------------------------------Aliment-------------------------
with open("Aliment.csv","w", newline='' ,encoding='utf-8') as Aliment:
    writer = csv.writer(Aliment, delimiter=',')
    Aliment.write("Aliment"+ "\n")
    writer.writerow(['idAliment','nomAliment'])
    nom_aliment_possible=["Pain", "Tenders", "Frites", "Cheddar", "Sel", "Huile", "Lait"]
    num_aliment_list=[]
    for i in range(125):
       idAliment = fake.unique.random_int(1,1000,1)
       nomAliment = fake.random_element(elements=nom_aliment_possible)
       num_aliment_list.append(idAliment)
       #On met les Insert into dans un fichier 
       writer.writerow([idAliment,nomAliment])
   
#--------------Legume----------
with open("Legume.csv","w", newline='' ,encoding='utf-8') as Legume:
    writer = csv.writer(Legume, delimiter=',')
    Legume.write("Legume"+ "\n")
    writer.writerow(['idLegume','nomLegume'])
    nom_legume_possible=["Ail", "Brocoli", "Carotte", "Chou Rouge", "Epinard", "Maïs", "Melon", "Oignon", "Pomme de terre", "Radis", "Tomate", "Topinambour"]
    num_legume_list=[]
    for i in range(125):
       idLegume = fake.unique.random_int(1,1000,1)
       nomLegume = fake.random_element(elements=nom_legume_possible)
       num_legume_list.append(idLegume)
       #On met les Insert into dans un fichier 
       writer.writerow([idLegume,nomLegume])
    num_legume_list = tuple(num_legume_list)

#--------------------------------Sauce-------------------------------------
with open("Sauce.csv","w", newline='' ,encoding='utf-8') as Sauce:
    writer = csv.writer(Sauce, delimiter=',')
    Sauce.write("Sauce"+ "\n")
    writer.writerow(['idSauce','nomSauce'])
    nom_sauce_possible=["Mayonnaise", "Blanche", "Moutarde", "Sauce du chef", "Ketchup", "Beurre", "BBQ", "Tartare", "Poivre", "Pesto", "Sauce Fromagère"]
    num_sauce_list=[]
    for i in range(125):
       idSauce = fake.unique.random_int(1,1000,1)
       nomSauce = fake.random_element(elements=nom_sauce_possible)
       num_sauce_list.append(idSauce)
       #On met les Insert into dans un fichier 
       writer.writerow([idSauce,nomSauce])
       
#---------------------------------------Ingredient-------------------------
with open("Ingredient.csv","w", newline='' ,encoding='utf-8') as Ingredient:
    writer = csv.writer(Ingredient, delimiter=',')
    Ingredient.write("Ingredient"+ "\n")
    writer.writerow(['idIngredient','nomIngredient'])
    nom_ingredient_possible=["Poulet pané", "Fromage à raclette", "Reblochon", "Lardons", "Bacon", "Guanciale", "Pâtes", "Boeuf", "Poisson", "Saucisse"]
    num_ingredient_list=[]
    for i in range(125):
       idIngredient = fake.unique.random_int(1,1000,1)
       nomIngredient = fake.random_element(elements=nom_ingredient_possible)
       num_ingredient_list.append(idIngredient)
       #On met les Insert into dans un fichier 
       writer.writerow([idIngredient,nomIngredient])
   
#------------------Machine-------------------------------------------------
with open("Machine.csv","w", newline='' ,encoding='utf-8') as Machine:
    writer = csv.writer(Machine, delimiter=',')
    Machine.write("Machine"+ "\n")
    writer.writerow(['idMachine','nomMachine'])
    Machines_possibles = ["familiale","individuelle","multifonction","combinée","mini raclette","de table","electrique","bon marché","traditionnelle","pierrade-fondue"]
    num_machine_list = []
    for i in range(2500):
       idMachine = i
       num_machine_list.append(idMachine)
       nomMachine = fake.random_element(elements=Machines_possibles)
       writer.writerow([idMachine,nomMachine])
   
#--------------------------------Tenrac----------------------------------------
with open("Tenrac.csv","w", newline='' ,encoding='utf-8') as Tenrac:
    writer = csv.writer(Tenrac, delimiter=',')
    Tenrac.write("Tenrac"+ "\n")
    writer.writerow(['numero','refOrganisme','codeMembre','nom','prenom','courriel','numeroTel','adressePostale','gradeSup','grade','dignite','titre','rang'])
       
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
    for i in range(1,50000):
       numero = i
       list_numer.append(numero)
       refOrganisme = fake.random_digit()+1
       list_ref.append(refOrganisme)
       Code_membre = fake.unique.random_int(11000,99999,1)
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
       writer.writerow([numero,refOrganisme,Code_membre,Nom,Prenom,courriel,numeroTel,adresse_postale,gradeSup,grade,dignite,titre,rang])
    
    list_numer = tuple(list_numer)
    list_ref = tuple(list_ref)
    list_cod = tuple(list_cod)

#------------------------------Ordre-------------------------------------------
with open("Ordre.csv","w", newline='' ,encoding='utf-8') as Ordre:
    writer = csv.writer(Ordre, delimiter=',')
    Ordre.write("Ordre"+ "\n")
    writer.writerow(['numero','nomOrdre'])
    nom_Ordre = ["Enjoyers","Amateurs de ","Apprécieurs de ","Kiffeurs de "]
       
    for i in range(250):
       numero = fake.unique.random_element(elements=nv_list_num)
       nomOrdre = fake.random_element(elements=nom_Ordre) + fake.random_element(elements=mots)
       writer.writerow([numero,nomOrdre])
   
#-------------------------------Partenaire-------------------------------------
with open("Partenaire.csv","w", newline='' ,encoding='utf-8') as Partenaire:
    writer = csv.writer(Partenaire, delimiter=',')
    Partenaire.write("Partenaire"+ "\n")
    writer.writerow(['adresse','numero'])
    adresses = []
    for i in range(2000):
       adresse = fake.address().replace("\n", ", ")
       adresses.append(adresse)
       numero = fake.random_element(elements=nv_list_num)
       writer.writerow([adresse,numero])
   
#--------------------------------Reunion---------------------------------------
with open("Reunion.csv","w", newline='' ,encoding='utf-8') as Reunion:
    writer = csv.writer(Reunion, delimiter=',')
    Reunion.write("Reunion"+ "\n")
    writer.writerow(['idReunion'])
    num_reunion_list=[]
    for i in range(2000):
       idReunion = fake.unique.random_int(1,2100,1)
       numero = fake.random_element(elements=list_numer)
       refOrganisme = fake.random_element(elements=list_ref)
       codeMembre = fake.random_element(elements=list_cod)
       num_reunion_list.append(idReunion)
       writer.writerow([idReunion])
    num_reunion_list = tuple(num_reunion_list)

#--------------Plat----------
with open("Plat.csv","w", newline='' ,encoding='utf-8') as Plat:
    writer = csv.writer(Plat, delimiter=',')
    Plat.write("Plat"+ "\n")
    writer.writerow(['idPlat','nomPlat','idLegume'])
    nom_plat_possible=["Tenders", "Kebab", "Pizza", "Quiche", "Saumon", "Ananas", "Beurre", "Raclette", "Pasta Carbonara", "Poulet", "Fondue savoyarde", "Choucroute", "Foie gras"]
    num_plat_list=[]
    for i in range(250):
       idPlat = fake.unique.random_int(1,1000,1)
       nomPlat = fake.random_element(elements=nom_plat_possible)
       idLegume = fake.random_element(elements=num_legume_list)
       num_plat_list.append(idPlat)
       #On met les Insert into dans un fichier 
       writer.writerow([idPlat,nomPlat,idLegume])
   
#-------------------------Entretien--------------------------------------------
with open("Entretien.csv","w", newline='' ,encoding='utf-8') as Entretien:
    writer = csv.writer(Entretien, delimiter=',')
    Entretien.write("Entretien"+ "\n")
    writer.writerow(['idEntretient','periodeEntretient','typeEntretient','numero'])
    Entretients_possibles = ["mécanique","désinfectant","dégraissant","détergent","à l'eau"]
    list_E = []
    for i in range(1000):
       idEntretient = i
       list_E.append(idEntretient)
       periodeEntretien = fake.date()
       typeEntretien = fake.random_element(elements=Entretients_possibles)
       numero = fake.random_element(elements=nv_list_num)
       writer.writerow([idEntretient,periodeEntretien,typeEntretien,numero])
    list_E = tuple(list_E)
   
#------------------------------Club--------------------------------------------
with open("Club.csv","w", newline='' ,encoding='utf-8') as Club:
    writer = csv.writer(Club, delimiter=',')
    Club.write("Club"+ "\n")
    writer.writerow(['numero_1','nomClub','numero'])
    mots_en_plus = ["Raclette","Poulet","Tenders","Legume","Sauce","Kebab","Pizza","Quiche","Saumon","Ananas","Beurre","Divin","Goutu","Délicieux","A se damner"]
    list_numer1 = []
    def nomclub():
       fin = ''
       nb_alet = random.randint(1, 3)
       for i in range(nb_alet):
           fin+= fake.random_element(elements=mots_en_plus)
       return fin   
       
    for i in range(250):
       numero1 = fake.unique.random_element(elements=nv_list_num)
       list_numer1.append(numero1)
       nomClub = nomclub()
       numero = fake.random_element(elements=nv_list_num)
       writer.writerow([numero1,nomClub,numero])
   
#--------------------------------Modele----------------------------------------
with open("Modele.csv","w", newline='' ,encoding='utf-8') as Modele:
    writer = csv.writer(Modele, delimiter=',')
    Modele.write("Modele"+ "\n")
    writer.writerow(['idModele','nomModele','idEntretient'])
    num_modele_list = []
    for i in range(500):
       idModele = fake.random_int(1,100,1)
       num_modele_list.append(idModele)
       nomModele = fake.random_letter() + fake.random_letter() + ' ' + str(fake.random_digit()) + str(fake.random_digit()) + str(fake.random_digit())
       idEntretient = fake.random_element(elements=list_E)
       writer.writerow([idModele,nomModele,idEntretient])
   
#------------------SeGroupe------------------------------------------------
with open("SeGroupe.csv","w", newline='' ,encoding='utf-8') as SeGroupe:
    writer = csv.writer(SeGroupe, delimiter=',')
    SeGroupe.write("SeGroupe"+ "\n")
    writer.writerow(['adresse','date_','idReunion'])
    for i in range(2000):
       adresse=fake.random_element(elements=adresses)
       date=fake.random_element(elements=Date)
       idReunion=fake.random_element(elements=num_reunion_list)
       writer.writerow([adresse,date,idReunion])
   
#------------------Rejoint--------------------------------------------------
with open("Rejoint.csv","w", newline='' ,encoding='utf-8') as Rejoint:
    writer = csv.writer(Rejoint, delimiter=',')
    Rejoint.write("Rejoint"+ "\n")
    writer.writerow(['numero','refOrganisme','codeMembre','idReunion'])
    for i in range(3500):
       numero=fake.random_element(elements=list_numer)
       refOrganisme=fake.random_element(elements=list_ref)
       codeMembre=fake.random_element(elements=list_cod)
       idReunion=fake.random_element(elements=num_reunion_list)
       writer.writerow([numero,refOrganisme,codeMembre,idReunion])

#------------------------------------Compose------------------------------
with open("Compose.csv","w", newline='' ,encoding='utf-8') as Compose:
    writer = csv.writer(Compose, delimiter=',')
    Compose.write("Compose"+ "\n")
    writer.writerow(['idRepas','idPlat'])
    for i in range(2000):
       idRepas = fake.random_element(elements=num_repas_list)
       idPlat = fake.random_element(elements=num_plat_list)
       #On met les Insert into dans un fichier 
       writer.writerow([idRepas,idPlat])
       
#------------------------------------Constitue----------------------------
with open("Constitue.csv","w", newline='' ,encoding='utf-8') as Constitue:
    writer = csv.writer(Constitue, delimiter=',')
    Constitue.write("Constitue"+ "\n")
    writer.writerow(['idPlat','idAliment'])
    for i in range(250):
       idPlat = fake.random_element(elements=num_plat_list)
       idAliment = fake.random_element(elements=num_aliment_list)
       #On met les Insert into dans un fichier 
       writer.writerow([idPlat,idAliment])
   
#------------------------------------Accompagne----------------------------
with open("Accompagne.csv","w", newline='' ,encoding='utf-8') as Accompagne:
    writer = csv.writer(Accompagne, delimiter=',')
    Accompagne.write("Accompagne"+ "\n")
    writer.writerow(['idPlat','idSauce'])
    for i in range(250):
       idPlat = fake.random_element(elements=num_plat_list)
       idSauce = fake.random_element(elements=num_sauce_list)
       #On met les Insert into dans un fichier 
       writer.writerow([idPlat,idSauce])
   
#---------------------------------------forme------------------------------
with open("forme.csv","w", newline='' ,encoding='utf-8') as forme:
    writer = csv.writer(forme, delimiter=',')
    forme.write("forme"+ "\n")
    writer.writerow(['idSauce','idIngredient'])
    for i in range(250):
       idSauce = fake.random_element(elements=num_sauce_list)
       idIngredient = fake.random_element(elements=num_ingredient_list)
       #On met les Insert into dans un fichier 
       writer.writerow([idSauce,idIngredient])
   
#--------------Mange----------
with open("Mange.csv","w", newline='' ,encoding='utf-8') as Mange:
    writer = csv.writer(Mange, delimiter=',')
    Mange.write("Mange"+ "\n")
    writer.writerow(['date_','idReunion','idRepas'])
    for i in range(2500):
       date = fake.random_element(elements=Date)
       idReunion = fake.random_element(elements=num_reunion_list)
       idRepas = fake.random_element(elements=num_repas_list)
       #On met les Insert into dans un fichier 
       writer.writerow([date,idReunion,idRepas])
   
#------------------Caracterise--------------------------------------------
with open("Caracterise.csv","w", newline='' ,encoding='utf-8') as Caracterise:
    writer = csv.writer(Caracterise, delimiter=',')
    Caracterise.write("Caracterise"+ "\n")
    writer.writerow(['idMachine','idModele'])
    for i in range(1000):
       idMachine=fake.random_element(elements=num_machine_list)
       idModele=fake.random_element(elements=num_modele_list) 
       writer.writerow([idMachine,idModele])
   
#-----------------Realise-------------------------------------------------
with open("Realise.csv","w", newline='' ,encoding='utf-8') as Realise:
    writer = csv.writer(Realise, delimiter=',')
    Realise.write("Realise"+ "\n")
    writer.writerow(['numero','refOrganisme','codeMembre','idMachine','idEntretient'])
    for i in range(2500):
       numero=fake.random_element(elements=list_numer)
       refOrganisme=fake.random_element(elements=list_ref)
       codeMembre=fake.random_element(elements=list_cod)
       idMachine=fake.random_element(elements=num_machine_list)
       id_Entretient=fake.random_element(elements=list_E)
       writer.writerow([numero,refOrganisme,codeMembre,idMachine,id_Entretient])
  
   
#--------------------------------Utilisation Officielle----------------------
with open("Utilisation_Officielle.csv","w", newline='' ,encoding='utf-8') as Utilisation_Officielle:
    writer = csv.writer(Utilisation_Officielle, delimiter=',')
    Utilisation_Officielle.write("Utilisation Officielle"+ "\n")
    writer.writerow(['idRepas','idMachine'])
    for i in range(2500):
       idRepas = fake.random_element(elements=num_repas_list)
       idMachine = fake.random_element(elements=num_machine_list)
       writer.writerow([idRepas,idMachine])
   
#-----------------------------Intolerance----------------------------------
with open("Intolerance.csv","w", newline='' ,encoding='utf-8') as Intolerance:
    writer = csv.writer(Intolerance, delimiter=',')
    Intolerance.write("Intolerance"+ "\n")
    writer.writerow(['numero','refOrganisme','codeMembre','idLegume'])
    for i in range(1500):
       numero = fake.random_int(1,100)
       refOrganisme = fake.random_element(elements=list_numer)
       codeMembre = fake.random_element(elements=list_cod)
       idLegume = fake.random_element(elements=num_legume_list)
       writer.writerow([numero,refOrganisme,codeMembre,idLegume])
   
#-----------------------------------Enregistre1----------------------------
with open("Enregistre1.csv","w", newline='' ,encoding='utf-8') as Enregistre1:
    writer = csv.writer(Enregistre1, delimiter=',')
    Enregistre1.write("Enregistre1"+ "\n")
    writer.writerow(['numero','idEntretien'])
    for i in range(2500):
       numero = fake.random_element(elements=list_numer1)
       idEntretient = fake.random_element(elements=list_E)
       writer.writerow([numero,idEntretient])
   
#-------------------------------------Dirige-------------------------------
with open("Dirige.csv","w", newline='' ,encoding='utf-8') as Dirige:
    writer = csv.writer(Dirige, delimiter=',')
    Dirige.write("Dirige"+ "\n")
    writer.writerow(['numero','refOrganisme','codeMembre','idReunion'])
    for i in range(2000):
       refOrganisme = fake.random_element(elements=list_numer)
       codeMembre = fake.random_element(elements=list_cod)
       idLegume = fake.random_element(elements=num_legume_list)
       idReunion = fake.random_element(elements=num_reunion_list)
       writer.writerow([numero,refOrganisme,codeMembre,idReunion])
#-----------------------------Rang----------------------------------
with open("Rang.csv","w", newline='' ,encoding='utf-8') as Rang:
    writer = csv.writer(Rang, delimiter=',')
    Rang.write("Rang"+ "\n")
    writer.writerow(['rang'])
    for i in Rang_possibles:
        writer.writerow([i])
#-----------------------------Titre----------------------------------
with open("Titre.csv","w", newline='' ,encoding='utf-8') as Titre:
    writer = csv.writer(Titre, delimiter=',')
    Titre.write("titre"+ "\n")
    writer.writerow(['titre'])
    for i in Titres_possibles:
        writer.writerow([i])
#-----------------------------Dignite----------------------------------
with open("Dignite.csv","w", newline='' ,encoding='utf-8') as Dignite:
    writer = csv.writer(Dignite, delimiter=',')
    Dignite.write("Dignite"+ "\n")
    writer.writerow(['dignite'])
    for i in Dignités_possibles:
        writer.writerow([i])
#-----------------------------Grade----------------------------------
with open("Grade.csv","w", newline='' ,encoding='utf-8') as Grade:
    writer = csv.writer(Grade, delimiter=',')
    Grade.write("Grade"+ "\n")
    writer.writerow(['grade'])
    for i in Grades_possibles:
        writer.writerow([i])
#-----------------------------GradeSup----------------------------------
with open("GradeSup.csv","w", newline='' ,encoding='utf-8') as GradeSup:
    writer = csv.writer(GradeSup, delimiter=',')
    GradeSup.write("GradeSup"+ "\n")
    writer.writerow(['gradeSup'])
    for i in Grades_Supérieurs:
        writer.writerow([i])
  	 
print("Script éxécuté")