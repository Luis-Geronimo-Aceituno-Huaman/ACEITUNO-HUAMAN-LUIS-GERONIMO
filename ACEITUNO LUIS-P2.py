
num=int(input("Ingrese el numero de empleados a ingresar: "))
total_c=0
total_N=0
diccionario={'NOMBRE':[], 'SUELDO':[], 'TIPO': [None for i in range(num)],'SUELDO NETO':[],'SUELDO REDUCIDO':[],'BONO':[None for i in range(num)]}
while num<0:
    num=int(input("Ingrese una cantidad valida: "))
for i in range(num):
    diccionario['NOMBRE'].append(str(input(f"Ingrese el nombre del trabajador #{i+1}: ")))
    diccionario['SUELDO'].append(float(input("  Ingrese su sueldo base: ")))
    while diccionario['SUELDO'][i]<0:
        diccionario['SUELDO'][i]=float(input("  Ingrese un sueldo valido: "))
    
    TIPO=str(input("    Ingrese el tipo de emepleado (N/C): "))
        
    while TIPO!='C' and TIPO!='N':
        TIPO=str(input("    Ingrese un tipo valido (N/C): "))
    diccionario['TIPO'][i]=TIPO
    REDUCIDO=diccionario['SUELDO'][i]-(diccionario['SUELDO'][i]*0.08) -diccionario['SUELDO'][i]*0.05
    diccionario['SUELDO REDUCIDO'].append(REDUCIDO)
    if diccionario['TIPO'][i]=='C':
        diccionario['BONO'][i]=diccionario['SUELDO'][i]*0.08
        diccionario['SUELDO NETO'].append(diccionario['SUELDO REDUCIDO'][i]+diccionario['SUELDO'][i]*0.08) 
        total_c=total_c+diccionario['SUELDO NETO'][i]
    elif diccionario['TIPO'][i]=='N':
        diccionario['BONO'][i]=diccionario['SUELDO'][i]*0.12
        diccionario['SUELDO NETO'].append(diccionario['SUELDO REDUCIDO'][i]+diccionario['SUELDO'][i]*0.12) 
        total_N=total_N+diccionario['SUELDO NETO'][i]

print("TABLA DE DATOS")
print(("N°").rjust(5,' '),('NOMBRE').rjust(20,' '), ('SUELDO BASE').rjust(10,' '),('SUELDO REDUCIDO').rjust(15,' ')),('bonificacion').rjust(15,' '),('SUELDO NETO').rjust(15,' ')
for i in range(num):
    print(str(1+i).rjust(5,' '),str(diccionario['NOMBRE'][i]).rjust(20,' '), str(diccionario['SUELDO'][i]).rjust(10,' '),str(diccionario['SUELDO REDUCIDO'][i]).rjust(15,' ')),str(diccionario['BONO'][i]).rjust(15,' '),str(diccionario['SUELDO NETO'][i]).rjust(15,' ')
print(f'Total de sueldos de trabajadores N : {total_N} \nTotal de sueldos de trabajadores C:{total_c}')
