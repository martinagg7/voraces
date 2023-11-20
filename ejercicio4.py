"""Nos dan un array de N elementos y nos piden  desde k=2 hasta n 
Dividir el array en k trozos tal que la diferencia entre el máximo y el minimo de cada array sumada con la de los otros sea el minimo
si k=2
63412 [6,3,4] [1,2] 3+1=4
10,8,5,2,1 y k=3 [2,1][5][8,10] 1+0+2=3
--------------
IDEA
Siempre nos va a interesear coger elementos que esten cerca en la lista ordenada
ej:[6,1,3,2,10,9] k=3
[1,2,3,6,9,10]como queremos hacer tres particiones y nos tenemos que quitar los saltos más grandes
#quitándonos los saltos más grandes
[1,2,3] [6] [9,10]

"""
def particion(x,k):
    a=sorted(x)
    b=list(a[i+1])+a[i] for i in range (len(a)-1))
    b=sorted(enumerate(b),key=lambda x:x[1],reverse=True)
    s=a[len(a)-1]-a[0-sum(b[:k])]

