import sys
lista=[1,2,3,4,5,6,7,8,9]


def prvi_unos():
    z=""
    while z!="X" and z!="O":
        z=input("\nМолим вас унесите \"X\" или \"O\": \n")
    return z
    
def naizmenicno(h):
    if h=="X":
        z="O"
    if h=="O":
        z="X"
    return z

def tri_ista(lista, odabrani_element):
    if lista[0] == lista[1] == lista[2]:
        return print(f"Победник је играч који је одабрао ознаку: {odabrani_element}"), sys.exit()
    if lista[3] == lista[4] == lista[5]:
        return print(f"Победник је играч који је одабрао ознаку: {odabrani_element}"), sys.exit()
    if lista[6] == lista[7] == lista[8]:
        return print(f"Победник је играч који је одабрао ознаку: {odabrani_element}"), sys.exit()
    if lista[0] == lista[3] == lista[6]:
        return print(f"Победник је играч који је одабрао ознаку: {odabrani_element}"), sys.exit()
    if lista[1] == lista[4] == lista[7]:
        return print(f"Победник је играч који је одабрао ознаку: {odabrani_element}"), sys.exit()
    if lista[2] == lista[5] == lista[8]:
        return print(f"Победник је играч који је одабрао ознаку: {odabrani_element}"), sys.exit()
    if lista[0] == lista[4] == lista[8]:
        return print(f"Победник је играч који је одабрао ознаку: {odabrani_element}"), sys.exit()
    if lista[2] == lista[4] == lista[6]:
        return print(f"Победник је играч који је одабрао ознаку: {odabrani_element}"), sys.exit()

def pozicija_iscrtavanje(lista, odabrani_element):
        
        odabrani_element=naizmenicno(odabrani_element)
        
        slobodne_pozicije=[]       # слободне позиције на табли
        p=0     # бројач
        k=888   # позиција на табли

        for i in lista:
                 if i!="X" and i!="O":
                    slobodne_pozicije.append(i)  
        while k not in slobodne_pozicije:
            k=input(f"Молим вас унесите слободну позицију на табли {slobodne_pozicije}: ")
            if k.isdigit():
                k=int(k)
 
        if k==1 and lista[k-1]!="X" and lista[k-1]!="O":
                lista[k-1]=odabrani_element          # "X" ili "O"
                for i in lista:
                    p+=1
                    if p%3==0:
                        if i=="X" or i=="O":
                            print(i, end="")  
                            print()                       
                        else:
                            print("#", end="")
                            print()
                    else:
                        if i=="X" or i=="O":
                            print(i, end="|")
                        else:
                            print("#", end="|")
                print()
                tri_ista(lista, odabrani_element)
                return lista, odabrani_element
        elif k==2 and lista[k-1]!="X" and lista[k-1]!="O":
                lista[k-1]=odabrani_element
                for i in lista:
                    p+=1
                    if p%3==0:
                        if i=="X" or i=="O":
                            print(i, end="")  
                            print()                       
                        else:
                            print("#", end="")
                            print()
                    else:
                        if i=="X" or i=="O":
                            print(i, end="|")
                        else:
                            print("#", end="|")
                print()
                tri_ista(lista, odabrani_element)            
                return lista, odabrani_element
        elif k==3 and lista[k-1]!="X" and lista[k-1]!="O":
                lista[k-1]=odabrani_element
                for i in lista:
                    p+=1
                    if p%3==0:
                        if i=="X" or i=="O":
                            print(i, end="")  
                            print()                       
                        else:
                            print("#", end="")
                            print()
                    else:
                        if i=="X" or i=="O":
                            print(i, end="|")
                        else:
                            print("#", end="|")
                print()
                tri_ista(lista, odabrani_element)            
                return lista, odabrani_element
        elif k==4 and lista[k-1]!="X" and lista[k-1]!="O":
                lista[k-1]=odabrani_element
                for i in lista:
                    p+=1
                    if p%3==0:
                        if i=="X" or i=="O":
                            print(i, end="")  
                            print()                       
                        else:
                            print("#", end="")
                            print()
                    else:
                        if i=="X" or i=="O":
                            print(i, end="|")
                        else:
                            print("#", end="|")
                print()
                tri_ista(lista, odabrani_element)            
                return lista, odabrani_element
        elif k==5 and lista[k-1]!="X" and lista[k-1]!="O":
                lista[k-1]=odabrani_element
                for i in lista:
                    p+=1
                    if p%3==0:
                        if i=="X" or i=="O":
                            print(i, end="")  
                            print()                       
                        else:
                            print("#", end="")
                            print()
                    else:
                        if i=="X" or i=="O":
                            print(i, end="|")
                        else:
                            print("#", end="|")
                print()
                tri_ista(lista, odabrani_element)            
                return lista, odabrani_element
        elif k==6 and lista[k-1]!="X" and lista[k-1]!="O":
                lista[k-1]=odabrani_element
                for i in lista:
                    p+=1
                    if p%3==0:
                        if i=="X" or i=="O":
                            print(i, end="")  
                            print()                       
                        else:
                            print("#", end="")
                            print()
                    else:
                        if i=="X" or i=="O":
                            print(i, end="|")
                        else:
                            print("#", end="|")
                print()
                tri_ista(lista, odabrani_element)            
                return lista, odabrani_element
        elif k==7 and lista[k-1]!="X" and lista[k-1]!="O":
                lista[k-1]=odabrani_element
                for i in lista:
                    p+=1
                    if p%3==0:
                        if i=="X" or i=="O":
                            print(i, end="")  
                            print()                       
                        else:
                            print("#", end="")
                            print()
                    else:
                        if i=="X" or i=="O":
                            print(i, end="|")
                        else:
                            print("#", end="|")
                print()
                tri_ista(lista, odabrani_element)            
                return lista, odabrani_element
        elif k==8 and lista[k-1]!="X" and lista[k-1]!="O":
                lista[k-1]=odabrani_element
                for i in lista:
                    p+=1
                    if p%3==0:
                        if i=="X" or i=="O":
                            print(i, end="")  
                            print()                       
                        else:
                            print("#", end="")
                            print()
                    else:
                        if i=="X" or i=="O":
                            print(i, end="|")
                        else:
                            print("#", end="|")
                print()
                tri_ista(lista, odabrani_element)            
                return lista, odabrani_element
        elif k==9 and lista[k-1]!="X" and lista[k-1]!="O":
                lista[k-1]=odabrani_element
                for i in lista:
                    p+=1
                    if p%3==0:
                        if i=="X" or i=="O":
                            print(i, end="")  
                            print()                       
                        else:
                            print("#", end="")
                            print()
                    else:
                        if i=="X" or i=="O":
                            print(i, end="|")
                        else:
                            print("#", end="|")
                print()
                tri_ista(lista, odabrani_element)            
                return lista, odabrani_element
        

    

odabrani_element=prvi_unos()                # нпр. "X" 
print()
print("Молим вас унесите позицију на табли:\n\n1|2|3\n4|5|6\n7|8|9\n")

naiz=naizmenicno(odabrani_element)          # нпр. "O"

lista, naiz=pozicija_iscrtavanje(lista,naiz)
lista, naiz=pozicija_iscrtavanje(lista,naiz)
lista, naiz=pozicija_iscrtavanje(lista,naiz)
lista, naiz=pozicija_iscrtavanje(lista,naiz)
lista, naiz=pozicija_iscrtavanje(lista,naiz)
lista, naiz=pozicija_iscrtavanje(lista,naiz)
lista, naiz=pozicija_iscrtavanje(lista,naiz)
lista, naiz=pozicija_iscrtavanje(lista,naiz)
lista, naiz=pozicija_iscrtavanje(lista,naiz)
