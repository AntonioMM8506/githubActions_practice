import random

def busqueda_binaria(lista, comienzo, final, objetivo, i=0):
    i += 1
    medio = (comienzo + final)//2
    print(f'{i} - buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
    
    if comienzo > final:
        return (False, i)

    if lista[medio] == objetivo:
        return (True, i)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1, final, objetivo, i=i)
    else:
        return busqueda_binaria(lista, comienzo, medio-1, objetivo, i=i)
#End of busqueda_binaria

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar?'))
    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])
    
    (encontrado, i) = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} { "esta" if encontrado else "no esta" } en la lista')

#End of main