import csv
from functools import reduce

#prosjecni rezultat na kolokviju1, kolokviju 2 i prvom ispitnom roku
lista1=[]
lista2=[]
lista3ispit=[]
brojac=0
with open('evidencija.csv') as f: #otvaranje
    reader=csv.reader(f, delimiter=',')
    
    for x in reader: 
        lista1.append(x[4]) #u listu dodaj 4.element redka(liste)
        lista2.append(x[5])
        lista3ispit.append(x[6])

    lista1.remove('K1') #ukloni k1 iz liste jer trebaju samo brojevi
    lista2.remove('K2') #ukloni k2 iz liste
    lista3ispit.remove('1.rok') #ukloni 1.rok iz liste


    for x in lista1[:]: #shallow copy (ako se ne stavi lista se poremeti i kad se ukloni odredeni element poremeti se lista i neki se preskoce elementi)
        if(x==''):
            lista1.remove('') #ukloni iz liste one koji nisu izasi iz nje
    
    for x in lista2[:]: #shallow copy (ako se ne stavi lista se poremeti i kad se ukloni odredeni element poremeti se lista i neki se preskoce elementi)
        if(x==''):
            lista2.remove('')
    
    for x in lista3ispit[:]: #shallow copy (ako se ne stavi lista se poremeti i kad se ukloni odredeni element poremeti se lista i neki se preskoce elementi)
        if(x==''):
            lista3ispit.remove('')
    
    novabrojevi=[]
    novakolokvij2=[] #prazna lista u kojoj ce se pretvoriti u int
    novaispit=[]
    print(lista1)
    for x in lista1:
        novabrojevi.append(int(x)) #pretvoreno u int
    print(novabrojevi)

    for x in lista2:
        novakolokvij2.append(int(x))
    
    for x in lista3ispit:
        novaispit.append(int(x))


    duljina=len(novabrojevi)
    duljina2=len(novakolokvij2) #da znamo koliko je studenata izaslo, s koliko cemo djeliti zbroj
    duljinaispit=len(novaispit)

    rjesenje=reduce(lambda x,y: x+y,novabrojevi) #zbroji prva dva iz liste pa onda taj zbroj s trecin brojen u listi
    rjkolokvij2=reduce(lambda x,y:x+y, novakolokvij2)
    rjispit=reduce(lambda x,y:x+y, novaispit)

    print("Prosjek prvog kolokvija je: " +str(rjesenje/duljina))
    print("Prosjek drugog kolokvija je: " +str(rjkolokvij2/duljina2))
    print("Prosjek 1.ispita ispita je: " +str(rjispit/duljinaispit))
        
   

   
    
        


        

    