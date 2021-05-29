import csv

#broj studenata koji nisu izasli ni na jedan od ispita 


        
with open('evidencija.csv') as f:
    reader=csv.reader(f, delimiter=',')
    #konacniBroj=NijeIzasao(reader)
    studenti=list(filter(lambda x:(x[4]=='' and x[5]=='' and x[6]==''), reader)) #ako nisu zasli vrati true i spremi u listu
    brojac=0
    for i in studenti:
        brojac=brojac+1 #broji koliko je clanova u listi da se zna koliko ih nije izaslo
    
    print("Broj studenata koji nisu izasli je: " +str(brojac))

    
   






        

    
