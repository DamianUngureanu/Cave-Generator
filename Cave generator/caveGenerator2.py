import tkinter as tk
import random
from PIL import Image#pentru a functiona, trebuie sa scri in terminal "pil install Pillow"


map=[]
mapAux=[]
n=int(500);m=int(500)#lungimea si latimea ferestrei
#fiecare patrat are 5*5px
N=n/5#numarul de patrate pe lungime
M=m/5#numarul de patrate pe latime

def creaza(plansa):#scrie in matrice.txt si creeaza fereastracu patrate
    with open("matricea.txt","w") as matrice:
        for i in range(0,int(N)-1):
                for j in range(0,int(M)-1):
                    if(j!=0):matrice.write(",")#conditie sa nu inceapa randurile cu ","
                    if(plansa[i][j]==1):
                        canvas.create_rectangle(i*5,j*5,i*5+5,j*5+5,fill="gray",outline="")
                        matrice.write("1")
                    else:
                        canvas.create_rectangle(i*5,j*5,i*5+5,j*5+5,fill="white",outline="")
                        matrice.write("0")
                matrice.write("\n")

def on_window_click(event):
    map2=[]
    plusLinieAux=[]
    mapAux=[]
    with open("matricea.txt","r") as matrice:#citeste din matrice.txt
        for linii in matrice:
            linieS=linii.split(",")
            linieI=[int(element) for element in linieS]
            mapAux.append(linieI)#salveaz in mapAux, matricea salvat in .txt
        for i in range(1,int(N)-2):
            linieAux=[]
            for j in range(1,int(M)-2):#ia la rand toate patratele fara cele din margine 
                nap=0
                for x in range(-1,2):
                    for y in range(-1,2):#verifica patratele din jurul patratului in cauza
                        if(mapAux[i+x][j+y]==1): nap+=1
                if(nap>=5): linieAux.append(1)#daca in jurul patratului in cauza sunt 5 ziduri, se face si el zid "1"
                else: linieAux.append(0)#daca nu, se face aer "0"
                plusLinieAux.append(1)#asta este pentru zidul de sus si jos. e construit pe parcurs si adaugat la final
            linieAux.append(1)#adauga zidul din dreapta la linia ce se construieste
            linieAux.insert(0,1)#adauga zidul din stanga la linia ce se construieste
            map2.append(linieAux)#urmatoarea matrice se creaza in map2
    map2.append(plusLinieAux)#se adauga zidul de sus si de jos
    map2.insert(0,plusLinieAux)
    creaza(map2)


fereastra=tk.Tk()
canvas=tk.Canvas(fereastra, width=n,height=m)
canvas.pack()
img=Image.new('RGB',(400,400),color='grey')
#asta e crearea efectiva a ferestrei

plusLinie=[]
for i in range(5,n,5):
    linie=[]
    for j in range(5,m,5):
        aux=random.choice([0,1])
        linie.append(aux)
    map.append(linie)
#asta creaza pria matrice random

for i in range(0,int(N-1)):
    map[0][i]=1
    map[i][0]=1
    map[i][int(N)-2]=1
    map[int(N)-2][i]=1
#asta creaza zidurile de la margine
creaza(map)

fereastra.bind("<Button-1>",on_window_click) 

fereastra.mainloop()
