import sqlite3
import models
import leerplanparser
import os

db_filename = 'leerplandoelen_db.sqlite3'

def create_db():
    conn = sqlite3.connect(db_filename)
    
    c = conn.cursor()
    
    # parsed data

    c.execute("CREATE TABLE Competenties(nummer text primary key, omschrijving text)")
    c.execute("CREATE TABLE Deelcompetenties(nummer text primary key, omschrijving text, competentie text)")
    c.execute("CREATE TABLE Leerplandoelen(nummer text primary key, omschrijving text, competentie text, deelcompetentie text)")
    
    leerplanonderdelen = leerplanparser.parse_leerplandoelentekst()

    for lpo in leerplanonderdelen:
        print(lpo.getInsertCommand())
        c.execute(lpo.getInsertCommand())

    # user data

    c.execute("CREATE TABLE User(id int primary key, achternaam text, voornaam text)")
    c.execute("CREATE TABLE Antwoorden(id int primary key, user_id int, leerplandoel text, inhoud text, tijdstip datetime)")

    # user test data

    c.execute("INSERT INTO User VALUES(1, 'Janssens', 'Jos')")
    c.execute("INSERT INTO Antwoorden VALUES(1, 1, '7.3.7', 'We hebben een les gegeven met de IT-Tapa.', '2019-02-06')")

    conn.commit()
    c.close()
    

if __name__ == '__main__':
    if os.path.isfile(db_filename):
        os.remove(db_filename)
    create_db()
    