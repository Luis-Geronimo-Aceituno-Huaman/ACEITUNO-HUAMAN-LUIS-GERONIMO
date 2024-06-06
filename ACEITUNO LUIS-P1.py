from tabulate import tabulate
matriz=[[None,None,None]for i in range(2)]
new_matriz=[[None,None,None]for i in range(2)]
matriz_2=[[None,None]for i in range(3)]
new_matriz_2=[[None,None]for i in range(3)]

def rellenar_matriz(matriz,matriz_2):
    for i in range(2):
        for k in range(3):
            x=float(input(f'Ingrese el elemento [{i}][{k}] de la matriz 2*3: '))
            while(x<1 or x>10):
                x=float(input('Ingrese numeros entre el 1 y 10: '))
            matriz[i][k]=x
            new_matriz[i][k]=x
    print('\n')
    for i in range(3):
        for k in range(2):
            y=float(input(f'Ingrese el elemento [{i}][{k}] de la matriz 3*2: '))
            while(y<1 or y>10):
                x=float(input('Ingrese numeros entre el 1 y 10: '))
            matriz_2[i][k]=y
            new_matriz_2[i][k]=y

def sustitucion(matriz,matriz_2,new_matriz,new_matriz_2):  
    for i in range(2):
        for k in range(3):
            if matriz[i][k]>5:
                new_matriz[i][k]=1
            else:
                continue
    for i in range(3):
        for k in range(2):
            if matriz_2[i][k]<6:
                new_matriz_2[i][k]=0
            else:
                continue
    
rellenar_matriz(matriz,matriz_2)
sustitucion(matriz,matriz_2,new_matriz,new_matriz_2)
print(f'La matriz 2*3 es: \n{tabulate(matriz)} \nY la matriz 2*3 modificada es: \n{tabulate(new_matriz)}')
print(f'La matriz 3*2 es: \n{tabulate(matriz_2)} \nY la matriz 3*2 modificada es: \n{tabulate(new_matriz_2)}')

