import csv
#lista studenata koji nisu izasli na prvi kolokvij


with open('evidencija.csv') as f: #otvaranje datoteke
    reader=csv.reader(f, delimiter=',') #procitaj je
    studenti=list(filter(lambda x: x[4]=='', reader)) #ako je kolokvij jedan ='', vrati true ili false
    #studenti koji su true spremi u studenti 
    for i in studenti: #ispisi svakog studenta u listi
        print(i)



