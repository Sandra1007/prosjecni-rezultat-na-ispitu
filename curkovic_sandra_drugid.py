#vraća prosječni rezultat onih studenata koji su položili ispit

import csv
with open('evidencija.csv') as file: #otvori i citaj csv
     reader=csv.reader(file)
     lista=[]
     next(reader) #preskoci prvu liniju
     for x in reader: #ako nije izasao, stavi da su 0 bodova imali i pretvori u integer da se moze racunat prosjek

        if(x[4]==''):
             x[4]=0
        else:
             x[4]=int(x[4])

        if(x[5]==''):
             x[5]=0
        else:
             x[5]=int(x[5])
         
        if(x[6]==''):
             x[6]=0
        else:
             x[6]=int(x[6])
        
        

        if(x[4]>=40 and x[5]>=40 and x[6]==0): #izracunaj prosjek ako je prosao oba kolokvija pa nije potrebno na ispit izlazit
            print(x, (x[4]+x[5])/2)
        
        if(x[4]<=39 and x[5]<=39 and x[6]>=40): #pao je oba kolokvija, ali prosao na 1.ispitnom roku
            print(x,x[6]) 
        
        if((x[4]<=39 or x[4]==0) and (x[5]<=39 or x[5]==0) and x[6]<=39): #prvi kolokvij ili 0 il manje od 40
            # i drugi kolokvij mora ili 0 ili manje od 40
            #i ispit manje od 40 znaci da je pao 
            print(x,0)
            

     
          
           
     
        
     
    
    
        
    
   

            
        
   
    
    
    





    
     