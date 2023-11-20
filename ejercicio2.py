
"""Tenemos un arrays desordenado y en cada operacion podemos elegir un k(indice)y revertir todos los elemetos anteriores desde 1 hasta k(el array es una permutacion)
    3214 y cogemos k=3 ya esta 
    52134 
    buscar el más pequeño te lo pones al princpio y luego le das vuelta a todo el array
    y así sucesivamente
    
    """
def sort(x):
    n=len(x)
    ret=[]
    while n>1:
        i=x.index(n)
        if i==x-1:
            i-=1
            continue

        x[:i+1]=x[i:-1:-1]#para dar la vuelya a la lista
        ret.append(i)
        ret.append(len(x))
        x=x[::-1]

