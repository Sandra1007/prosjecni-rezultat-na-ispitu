import csv

ocjene={ #rjecnik u kojem je spremljen omjer bodova i svaki omjer bodova predstavlja ocjenu
    range(0,60):1,
    range(60,70):2,
    range(70,80):3,
    range(80,90):4,
    range(90,101):5
}

def jel_najgori(rok_1, kol_1, kol_2):
    najgori = list(range(0, 6)) #od 0 do 6 bodova
    if rok_1 in najgori or kol_1 in najgori or kol_2 in najgori: 
        return True 
    return False

def studenti(lista):
    izmedu_nula_pet=[]
    with open('evidencija.csv')as f:
        reader=csv.reader(f,delimiter=",")
        next(f)
        for x in reader:
            for i in range(4, 7): 
                if(x[i]==''): #ako student nije izasao pisi nije izasao
                    x[i]='nije izasao'
                else:
                    x[i]=int(x[i]) #inace pretvori u string

            lista.append(x) #dodaj u listu kad izmjenis sve
         
            if (jel_najgori(x[4], x[5], x[6])): #ispisi studente izmedu 0 i 5 pomocu if
                izmedu_nula_pet.append(x)
                    
        
        st=list(filter(lambda x: jel_najgori(x[4], x[5], x[6]), lista))
       
        
        return izmedu_nula_pet, st,lista

def PretvoriuBroj(lista_st):
    for x in lista_st:
        for i in range(4,7):
            if(x[i]=='nije izasao'): #pretvori u 0 za lakse racunanje prosjeka
                x[i]=0
    
    return lista_st

def DodajOcjenu(lista_broj):
    #sve moguce kombinacije
    for x in lista_broj: 
        if(x[4]>=60 and x[5]>=60 and x[6]==0): #prosao oba kolokvija pa nije potrebno na ispit izlazit 
            rez=int(((x[4]+x[5])/2))        
            for key in ocjene: #za key u dictionariju
                if rez in key: #ako je prosjek u rangu od key
                    x.append(ocjene[key]) #u listu dodaj value od dictionarija 
        
        if(x[4]>=60 and x[5]>=60 and (x[6]>=60)): #prosao oba kolokvija, ali hoce popravit kolokvije na ispitu
            rez=x[6]        
            for key in ocjene: #za key u dictionariju
                if rez in key: #ako je prosjek u rangu od key
                    x.append(ocjene[key]) #u listu dodaj value od dictionarija 
                    
   
        if(x[4]<=59 and x[5]<=59 and x[6]>=60): #pao je oba kolokvija, ali prosao na 1.ispitnom roku
            rez=x[6]
            for key in ocjene:
                if rez in key:
                    x.append(ocjene[key]) 
                   
                    
        if(x[4]<=59 and x[5]<=59 and x[6]<=59): #pao sve
            rez=0
            for key in ocjene:
                if rez in key:
                    x.append(ocjene[key])
        
        if((x[4]<=59 and x[5]>=60) or(x[4]>=60 and x[5]<=59) and x[6]>=60): #prvi ili drugi pao, prosao ispit
            rez=x[6]
            for key in ocjene:
                if rez in key:
                    x.append(ocjene[key])
        
        if((x[4]<=59 and x[5]>=60) or(x[4]>=60 and x[5]<=59) and x[6]<=59): #prvi il drugi pao, pao ispit
            rez=0
            for key in ocjene:
                if rez in key:
                    x.append(ocjene[key])
      

    return lista_broj
                    
                    
        
lista=[] #prazna lista koja se salje u funckiju i u nju ce se spremat kada se umjesto '' pise 'nije izasao'
izmedu_nula_pet, st,lista_st = studenti(lista) 


for x in izmedu_nula_pet:
    print("IZMEDU 0 I 5 BEZ FUNKCIJE FILTER:" + str(x)) #s funkcijom filter
            
for x in st:
    print("S FUNKCIJON FILTER IZMEDU 0 I 5" +str(x)) #bez funkcije filter

lista_broj=PretvoriuBroj(lista_st) #one koje nisi izasli ce se pretvorit u 0 bodova da se lakse racuna prosjek
ocj=int(input("Unesi ocjenu: ")) #unos ocjene
ocjenest=DodajOcjenu(lista_broj) #lista koja ima brojeve umjesto 'nije izasao' se salje da se ovisno o prosjeku doda u nju ocjena
for x in ocjenest: #za svakog studenta
    if(x[7]==ocj): #ako je unesena ocjena jednaka x[7] (to je dodana ocjena ovisno o prosjeku studenta
        print(x) #onda se ispise taj student i sve o njemu








    
   
        





   
         