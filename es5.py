from random import randint, random
num=[]
n=int(input("Inserire il numero di numeri random presenti nella lista: "))
for i in range(n):
    num.append(random,randint(0,100))   
max=[]

if num[0]>num[1]:
    max.append(num[0])
if num[n-1]>num[n-2]:
    max.append(num[n-1])
for i in range(1,n-1):
    if num[i]>num[i-1] and num[i]>num[i+1]:
        max.append(num[i])
        
print("I numeri massimi sono: ",max)
 
