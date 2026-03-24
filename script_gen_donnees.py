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

Grades_possibles = ['Affilié', 'Sympathisant', 'Adhérent', 'Chevalier', 'Dame', 'Grand Chevalier', 'HauteDame', 'Commandeur', "Grand’Croix"] 
Rang_possibles = ['Novice','Compagnon']
Titres_possibles = ['Philantrope','Protecteur','Honorable']
Dignités_possibles = ['Maître','Grand chancelier','Grand Maître']

for i in range(1,10):
        numero = i
        refOrganisme = fake.random_digit()+1
        Code_membre = fake.unique.random_int(1000,9999,1)
        Nom = nom()
        Prenom = prenom()
        courriel = fake.company_email()
        numeroTel = fake.phone_number()
        adresse_postale = fake.address()
        grade = fake.random_element(elements=Grades_possibles)
        dignite = fake.random_element(elements=Dignités_possibles)
        titre = fake.random_element(elements=Titres_possibles)
        rang = fake.random_element(elements=Rang_possibles)
        with open("resultat.txt","a") as file:
            file.write("INSERT INTO Tenrac(numero,refOrganisme,codeMembre,nom,prenom,courriel,numeroTel,adressePostale,grade,dignite,titre,rang) VALUES (" 
                       + str(numero) + ',' + str(refOrganisme) + ',' + str(Code_membre) + ',' 
                       + "'" + Nom + "'" + ',' + "'" + Prenom + "'" + ',' + "'" + courriel + "'" + ',' + "'" + numeroTel + "'" 
                       + ',' + "'" + adresse_postale + "'" + ',' + "'" + grade + "'" + ',' 
                       + "'" + dignite + "'" + ',' + "'" + titre + "'" + ',' + "'" + rang + "'" 
                       + ")" + "\n")
                       
#-----------------------Organisme-----------------------------------------------


Type_org_possible = ["Entreprise","Association","Organisme de formation"]
mots = ["raclette","poulet","pouletFrit","tenders","legume","sauce","kebab","pizza","quiche","saumon","ananas","beurre"]

def raisons_soc():
    fin = ''
    nb_alet = random.randint(1, 3)
    for i in range(nb_alet):
        fin += fake.random_element(elements=mots) + '_'
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
    with open("resultat.txt","a") as file:
        file.write("INSERT INTO Organisme(refOrganisme,typeOrganisme,raisonSociale,numeroSIRET) VALUES (" 
                   + str(RefOrganisme) + ',' + "'" + TypeOrganisme + "'" + ',' + "'" 
                   + Raisons_sociale + "'" + ',' + str(numero_SIRET) + ")" + "\n")
    

#--------------------------Date------------------------------------------------
Date = []
for i in range(10):
    dat = [
        fake.date()
        ]
    Date.append(dat)

print('fichier édité')
    
    
    
    
    
    
    
    
    
    
    
    
