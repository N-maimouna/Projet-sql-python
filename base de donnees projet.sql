#Création de la base de données Etudiants
CREATE DATABASE Etudiants;
#Utilisation de la table Etudiants
USE Etudiants;

#Création de la table Informations personnelles
CREATE TABLE InformationsPersonnelles(
    Prénom VARCHAR(50) ,
    Nom VARCHAR(20) ,
    Nationalité VARCHAR(20) ,
    Adresse VARCHAR(20) ,
    Id BIGINT NOT NULL,
    Niveau_d_études VARCHAR(20) ,
    Genre VARCHAR(5) ,
    Situation_matrimoniale VARCHAR(15) ,
    Email VARCHAR(100) ,
    Mot_de_passe VARCHAR(20) ,
    Date_de_naissance DATE , 
    PRIMARY KEY(Id));

#Création de la table Parcours
CREATE TABLE Parcours(
    Niveau_d_études VARCHAR(20) ,
    Spécialité VARCHAR(100) ,
    UFR VARCHAR(10) ,
    Année_de_validation YEAR ,
    Année_scolaire VARCHAR(10) NOT NULL ,
    Id BIGINT NOT NULL,
    PRIMARY KEY(Id,Année_scolaire));

#Insertion de données dans la table Informations personnelles
INSERT INTO InformationsPersonnelles
    (Prénom,Nom,Nationalité,Adresse,Id,Niveau_d_études,Genre,Situation_matrimoniale,Email,Mot_de_passe,Date_de_naissance)
VALUES
    ('Eden','Diop','Sénégalaise','Pikine',21020298123,'Master 1','Homme','Célibataire','edendiop@gmail.com','edenpoid001','1995-10-3'),
    ('Fatou','Diouf','Sénégalaise','Rufisque',21010100432,'Licence 3','Femme','Mariée','fatoudiouf@gmail.com','1997diouf','1997-3-24'),
    ('Babacar','Faye','Sénégalaise','Grand Standing',2102021182,'Master 1','Homme','Célibataire','babacarfaye@gmail.com','151005','1994-1-13');

#Insertion de données dans la table Parcours
INSERT INTO Parcours
    (Niveau_d_études,Spécialité,UFR,Année_de_validation,Année_scolaire,Id)
VALUES
    ('Licence 1','Mathématiques et Informatique','SET',2015,'2014-2015',21020298123),
    ('Licence 1','Mathématiques et Informatique','SET',2016,'2015-2016',21010100432),
    ('Licence 1','Management Informatisé des Organisations','SES',2015,'2014-2015',2102021182),
    ('Licence 2','Mathématiques et Informatique','SET',2016,'2015-2016',21020298123),
    ('Licence 2','Informatique','SET',2017,'2016-2017',21010100432),
    ('Licence 2','Management Informatisé des Organisations','SES',2016,'2015-2016',2102021182),
    ('Licence 3','Mathématiques et Informatique','SET',2017,'2016-2017',21020298123),
    ('Licence 3','Informatique','UFR SET',NULL,'2017-2018',21010100432),
    ('Licence 3','Management Informatisé des Organisations','SES',2017,'2016-2017',2102021182),
    ('Master 1','Statistique,économétrie et modélisation','SES',NULL,'2017-2018',21020298123),
    ('Master 1','Statistique,économétrie et modélisation','SES',NULL,'2017-2018',2102021182);