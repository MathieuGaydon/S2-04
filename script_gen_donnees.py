from faker import Faker
import csv
fake = Faker()
import random

#On s'assure de vider le fichier d'insertion des données
with open("result.csv","w", newline='' ,encoding='utf-8') as file:
    file.write("--Insertion des données dans la base : " + "\n")
    writer = csv.writer(file, delimiter=',')
    
    #--------------------------------Tenrac----------------------------------------
    file.write("Tenrac"+ "\n")
    writer.writerow(['numero','refOrganisme','codeMembre','nom','prenom','courriel','numeroTel','adressePostale','gradeSup','grade','dignite','titre','rang'])
    
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
        Code_membre = fake.unique.random_int(11000,99999,1)
        list_cod.append(Code_membre)
        Nom = nom()
        Prenom = prenom()
        courriel = fake.company_email()
        numeroTel = fake.phone_number()                                                                                                                                                                                                                                                                                                                                                                                                                          
        adresse_postale = fake.address().replace("\n", ", ")
        grade = ''
        gradeSup = ''
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
    
    #-----------------------Organisme-----------------------------------------------
    file.write("Organisme"+ "\n")
    
    Type_org_possible = ["Entreprise","Association","Organisme de formation"]
    mots = ["Raclette","Poulet","PouletFrit","Tenders","Legume","Sauce","Kebab","Pizza","Quiche","Saumon","Ananas","Beurre"]
    writer.writerow(['refOrganisme','typeOrganisme','raisonSociale','numeroSIRET'])
    
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
        writer.writerow([RefOrganisme,TypeOrganisme,Raisons_sociale,numero_SIRET])
    
    #--------------------------Date------------------------------------------------
    file.write("Date"+ "\n")
    Date=[]
    writer.writerow(['date_'])
    for i in range(10):
        dat = fake.date()
        Date.append(dat)
        writer.writerow([dat])
    Date = tuple(Date)
    
    #------------------------Organisation------------------------------------------
    file.write("Organisation"+ "\n")
    list_num = []
    writer.writerow(['numero'])
    for i in range(15):
        num = fake.unique.random_int(1,1200,1)
        list_num.append(num)
        writer.writerow([num])
    nv_list_num = tuple(list_num)
    
    #-------------------------Entretien--------------------------------------------
    file.write("Entretien"+ "\n")
    
    Entretients_possibles = ["mécanique","désinfectant","dégraissant","détergent","à l'eau"]
    list_E = []
    writer.writerow(['idEntretient','periodeEntretient','typeEntretient','numero'])
    for i in range(10):
        idEntretient = i
        list_E.append(idEntretient)
        periodeEntretien = fake.date()
        typeEntretien = fake.random_element(elements=Entretients_possibles)
        numero = fake.random_element(elements=nv_list_num)
        writer.writerow([idEntretient,periodeEntretien,typeEntretien,numero])
    list_E = tuple(list_E)
    
    #------------------------------Ordre-------------------------------------------
    file.write("Ordre"+ "\n")
    
    nom_Ordre = ["Enjoyers","Amateurs de ","Apprécieurs de ","Kiffeurs de "]
    list_num_Ordre = []
    writer.writerow(['numero','nomOrdre'])
    for i in range(10):
        numero = fake.unique.random_element(elements=nv_list_num)
        list_num_Ordre.append(numero)
        nomOrdre = fake.random_element(elements=nom_Ordre) + fake.random_element(elements=mots)
        writer.writerow([numero,nomOrdre])
    
    #------------------------------Club--------------------------------------------
    file.write("Club"+ "\n")
    
    mots_en_plus = ["Raclette","Poulet","Tenders","Legume","Sauce","Kebab","Pizza","Quiche","Saumon","Ananas","Beurre","Divin","Goutu","Délicieux","A se damner"]
    list_numer1 = []
    writer.writerow(['numero_1','nomClub','numero'])
    def nomclub():
        fin = ''
        nb_alet = random.randint(1, 3)
        for i in range(nb_alet):
            fin += fake.random_element(elements=mots_en_plus)
        return fin   
    
    for i in range(5):
        numero1 = fake.unique.random_element(elements=nv_list_num)
        list_numer1.append(numero1)
        nomClub = nomclub()
        numero = fake.random_element(elements=list_num_Ordre)
        writer.writerow([numero1,nomClub,numero])
    
    #-------------------------------Partenaire-------------------------------------
    file.write("Partenaire"+ "\n")
    adresses = []
    writer.writerow(['adresse','numero'])
    for i in range(10):
        adresse = fake.address().replace("\n", ", ")
        adresses.append(adresse)
        numero = fake.random_element(elements=nv_list_num)
        writer.writerow([adresse,numero])
    
    #--------------------------------Modele----------------------------------------
    file.write("Modele"+ "\n")
    num_modele_list = []
    writer.writerow(['idModele','nomModele','idEntretient'])
    for i in range(10):
        idModele = fake.random_int(1,100,1)
        num_modele_list.append(idModele)
        nomModele = fake.random_letter() + fake.random_letter() + ' ' + str(fake.random_digit()) + str(fake.random_digit()) + str(fake.random_digit())
        idEntretient = fake.random_element(elements=list_E)
        writer.writerow([idModele,nomModele,idEntretient])
    
    #--------------------------------Reunion---------------------------------------
    file.write("Reunion"+ "\n")
    num_reunion_list=[]
    writer.writerow(['idReunion'])
    for i in range(10):
        idReunion = fake.unique.random_int(1,2100,1)
        num_reunion_list.append(idReunion)
        writer.writerow([idReunion])
    num_reunion_list = tuple(num_reunion_list)
    
    #--------------Repas----------
    file.write("Repas"+ "\n")
    nom_repas_possible=["Petit-Déjeuner","Déjeuner","Goûter","Dîner", "Encas"]
    num_repas_list=[]
    writer.writerow(['idRepas','nomRepas'])
    for i in range(10):
        idRepas = fake.unique.random_int(1,5100,1)
        nomRepas = fake.random_element(elements=nom_repas_possible)
        num_repas_list.append(idRepas)
        writer.writerow([idRepas,nomRepas])
        
    #--------------Legume----------
    file.write("Legume"+ "\n")
    nom_legume_possible=["Ail", "Brocoli", "Carotte", "Chou Rouge", "Epinard", "Maïs", "Melon", "Oignon", "Pomme de terre", "Radis", "Tomate", "Topinambour"]
    num_legume_list=[]
    writer.writerow(['idLegume','nomLegume'])
    for i in range(10):
        idLegume = fake.unique.random_int(1,1000,1)
        nomLegume = fake.random_element(elements=nom_legume_possible)
        num_legume_list.append(idLegume)
        writer.writerow([idLegume,nomLegume])
    num_legume_list = tuple(num_legume_list)
    
    #--------------Plat----------
    file.write("Plat"+ "\n")
    nom_plat_possible=["Tenders", "Kebab", "Pizza", "Quiche", "Saumon", "Ananas", "Beurre", "Raclette", "Pasta Carbonara", "Poulet", "Fondue savoyarde", "Choucroute", "Foie gras"]
    num_plat_list=[]
    writer.writerow(['idPlat','nomPlat','idLegume'])
    for i in range(10):
        idPlat = fake.unique.random_int(1,1000,1)
        nomPlat = fake.random_element(elements=nom_plat_possible)
        idLegume = fake.random_element(elements=num_legume_list)
        num_plat_list.append(idPlat)
        writer.writerow([idPlat,nomPlat,idLegume])
    
    #--------------------------------Sauce-------------------------------------
    file.write("Sauce"+ "\n")
    nom_sauce_possible=["Mayonnaise", "Blanche", "Moutarde", "Sauce du chef", "Ketchup", "Beurre", "BBQ", "Tartare", "Poivre", "Pesto", "Sauce Fromagère"]
    num_sauce_list=[]
    writer.writerow(['idSauce','nomSauce'])
    for i in range(10):
        idSauce = fake.unique.random_int(1,1000,1)
        nomSauce = fake.random_element(elements=nom_sauce_possible)
        num_sauce_list.append(idSauce)
        writer.writerow([idSauce,nomSauce])
    
    #---------------------------------------Ingredient-------------------------
    file.write("Ingredient"+ "\n")
    nom_ingredient_possible=["Poulet pané", "Fromage à raclette", "Reblochon", "Lardons", "Bacon", "Guanciale", "Pâtes", "Boeuf", "Poisson", "Saucisse"]
    num_ingredient_list=[]
    writer.writerow(['idIngredient','nomIngredient'])
    for i in range(10):
        idIngredient = fake.unique.random_int(1,1000,1)
        nomIngredient = fake.random_element(elements=nom_ingredient_possible)
        num_ingredient_list.append(idIngredient)
        writer.writerow([idIngredient,nomIngredient])
    
    #------------------------------------------Aliment-------------------------
    file.write("Aliment"+ "\n")
    nom_aliment_possible=["Pain", "Tenders", "Frites", "Cheddar", "Sel", "Huile", "Lait"]
    num_aliment_list=[]
    writer.writerow(['idAliment','nomAliment'])
    for i in range(10):
        idAliment = fake.unique.random_int(1,1000,1)
        nomAliment = fake.random_element(elements=nom_aliment_possible)
        num_aliment_list.append(idAliment)
        writer.writerow([idAliment,nomAliment])
    
    #------------------------------------Compose------------------------------
    file.write("Compose"+ "\n")
    writer.writerow(['idRepas','idPlat'])
    for i in range(10):
        idRepas = fake.random_element(elements=num_repas_list)
        idPlat = fake.random_element(elements=num_plat_list)
        writer.writerow([idRepas,idPlat])
    
    #------------------------------------Constitue----------------------------
    file.write("Constitue"+ "\n")
    writer.writerow(['idPlat','idAliment'])
    for i in range(10):
        idPlat = fake.random_element(elements=num_plat_list)
        idAliment = fake.random_element(elements=num_aliment_list)
        writer.writerow([idPlat,idAliment])
    
    #------------------------------------Accompagne----------------------------
    file.write("Accompagne"+ "\n")
    writer.writerow(['idPlat','idSauce'])
    for i in range(10):
        idPlat = fake.random_element(elements=num_plat_list)
        idSauce = fake.random_element(elements=num_sauce_list)
        writer.writerow([idPlat,idSauce])
    
    #---------------------------------------forme------------------------------
    file.write("forme"+ "\n")
    writer.writerow(['idSauce','idIngredient'])
    for i in range(10):
        idSauce = fake.random_element(elements=num_sauce_list)
        idIngredient = fake.random_element(elements=num_ingredient_list)
        writer.writerow([idSauce,idIngredient])
    
    #--------------Mange----------
    file.write("Mange"+ "\n")
    writer.writerow(['date_','idReunion','idRepas'])
    for i in range(10):
        date = fake.random_element(elements=Date)
        idReunion = fake.random_element(elements=num_reunion_list)
        idRepas = fake.random_element(elements=num_repas_list)
        writer.writerow([date,idReunion,idRepas])
        
    #------------------Machine-------------------------------------------------
    Machines_possibles = ["familiale","individuelle","multifonction","combinée","mini raclette","de table","electrique","bon marché","traditionnelle","pierrade-fondue"]
    num_machine_list = []
    file.write("Machine"+ "\n")
    writer.writerow(['idMachine','nomMachine'])
    for i in range(10):
        idMachine = i
        num_machine_list.append(idMachine)
        nomMachine = fake.random_element(elements=Machines_possibles)
        writer.writerow([idMachine,nomMachine])
        
    #--------------------------------Utilisation Officielle----------------------
    file.write("Utilisation Officielle"+ "\n")
    writer.writerow(['idRepas','idMachine'])
    for i in range(10):
        idRepas = fake.random_element(elements=num_repas_list)
        idMachine = fake.random_element(elements=num_machine_list)
        writer.writerow([idRepas,idMachine])
    
    #-----------------------------Intolerance----------------------------------
    file.write("Intolerance"+ "\n")
    writer.writerow(['numero','refOrganisme','codeMembre','idLegume'])
    for i in range(10):
        numero = fake.unique.random_int(1,2000)
        refOrganisme = fake.random_element(elements=list_numer)
        codeMembre = fake.random_element(elements=list_cod)
        idLegume = fake.random_element(elements=num_legume_list)
        writer.writerow([numero,refOrganisme,codeMembre,idLegume])
    
    #-------------------------------------Dirige-------------------------------
    file.write("Dirige"+ "\n")
    writer.writerow(['numero','refOrganisme','codeMembre','idReunion'])
    for i in range(10):
        numero = fake.random_element(elements = list_numer)
        refOrganisme = fake.random_element(elements=list_numer)
        codeMembre = fake.random_element(elements=list_cod)
        idReunion = fake.random_element(elements=num_reunion_list)
        writer.writerow([numero,refOrganisme,codeMembre,idReunion])
        
    #-----------------------------------Enregistre1----------------------------
    file.write("Enregistre1"+ "\n")
    writer.writerow(['numero','idEntretien'])
    for i in range(10):
        numero = fake.random_element(elements=list_numer1)
        idEntretient = fake.random_element(elements=list_E)
        writer.writerow([numero,idEntretient])
        
    #------------------SeGroupe-------------------------------------------------
    file.write("SeGroupe"+ "\n")
    writer.writerow(['adresse','date_','idReunion'])
    for i in range(10):
        adresse=fake.random_element(elements=adresses)
        date=fake.random_element(elements=Date)
        idReunion=fake.random_element(elements=num_reunion_list)
        writer.writerow([adresse,date,idReunion])
    
    #------------------Rejoint-------------------------------------------------
    file.write("Rejoint"+ "\n")
    writer.writerow(['numero','refOrganisme','codeMembre','idReunion'])
    for i in range(10):
        numero=fake.random_element(elements=list_numer)
        refOrganisme=fake.random_element(elements=list_ref)
        codeMembre=fake.random_element(elements=list_cod)
        idReunion=fake.random_element(elements=num_reunion_list)
        writer.writerow([numero,refOrganisme,codeMembre,idReunion])
        
    #------------------Caracterise-------------------------------------------------
    file.write("Caracterise"+ "\n")
    writer.writerow(['idMachine','idModele'])
    for i in range(10):
        idMachine=fake.random_element(elements=num_machine_list)
        idModele=fake.random_element(elements=num_modele_list)
        writer.writerow([idMachine,idModele])
    
    #------------------Realise-------------------------------------------------
    file.write("Realise"+ "\n")
    writer.writerow(['numero','refOrganisme','codeMembre','idMachine','idEntretient'])
    for i in range(10):
        numero=fake.random_element(elements=list_numer)
        refOrganisme=fake.random_element(elements=list_ref)
        codeMembre=fake.random_element(elements=list_cod)
        idMachine=fake.random_element(elements=num_machine_list)
        id_Entretient=fake.random_element(elements=list_E)
        writer.writerow([numero,refOrganisme,codeMembre,idMachine,id_Entretient])
        
print("Script exécuté")