print ("Hackathon 2022")
print ("Problema 1: Scramble")
print ("Ingresa la primer cadena")
cadena1 = input()
print ("Ingresa la segunda cadena")
cadena2 = input()
def scramble(s1, s2):
    lista = []
    if len(s1) == len(s2):
        for x in s1:
          lista.append(x)
        
        for y in s2:
            try:
                lista.remove(y)
            except:
                return False
        return True
        
    else:
        return False        
print (scramble(cadena1.upper(), cadena2.upper()))


#problema #2
print ("Problema 2: Justificador de texto")
array = []
lista=[]
palabra = ""
print("Ingrese el tamaño máximo de linea")
maximo = int(input())
while(True):
    print("ingrese palabra (para terminar ingrese 'x')")
    palabra = input()
    if palabra == "x":
        break    
    array.append(palabra)
i=0
while i< len(array):
    cont2,linea=0,0
    while i+cont2<len(array) and (linea+len(array[i+cont2]))<= (maximo-cont2):
        linea+=len(array[i+cont2])
        cont2+=1
    temporal=array[i]
    j=0
    for j in range(cont2-1):
        if i+cont2>=len(array):
            temporal+=' '
        else:
            temporal+=' '*((maximo-linea)//(cont2-1)+(j<(maximo-linea)%(cont2-1)))
        temporal+=array[i+j+1]
        j+=1
    temporal+=' '* (maximo-len(temporal))
    lista.append(temporal)
    i+=cont2

print(*lista, sep = '\n')


#PROBLEMA NUMERO 3
i = 0
print ("Problema 3: Cadenas subsecuentes")
print ("Ingresa la primer cadena")
cadena1 = input().lower()
print ("Ingresa la segunda cadena")
cadena2 = input().lower()
subs = ""
if len(cadena1) > len(cadena2):
    size = len(cadena1)
else:
    size = len(cadena2)
for i in range(size):
    if cadena1[i] == cadena2[i]:
        subs += cadena1[i]
print("La cadena subsecuente es: " + subs)


#PROBLEMA NUMERO 4
print ("Problema 4: Abuela Binaria")
print ("Ingresa N")
n = int(input())
print ("Ingresa X")
x = int(input())
print ("Ingresa Y")
y = int(input())
if (x + y) == n:
    avellanas = 0
    binX = bin(x).replace("0b", "")
    binY = bin(y).replace("0b", "")
    for i in binX:
        if i == "1":
            avellanas += 1
    
    for j in binY:
        if j == "1":
            avellanas += 1
    print("La nieta recibira " + str(avellanas) + " avellanas.")
else:
    print("la nieta no recibirá nada porque no sabe sumar")

