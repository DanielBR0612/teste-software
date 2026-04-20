try:
    lista = list(map(int, input("digite os 3 numeros: ").split()))
except:
    raise ValueError("Deve ser 3 numeros espaçados sem virgula")

def triangulo(a,b,c):
    lista.sort()
    
    if (lista[0] + lista[1] <= lista[2] or len(lista) > 3):
        return "Triangulo nao valido"
    if (a == b and a == c):
        return "triangulo equilatero"
    elif (a == b or a == c or b == c):
        return "triangulo isoceles"
    else:
        return "triangulo escaleno"
    
print(triangulo(lista[0],lista[1],lista[2]))