#Examen
import os

import random

import csv

import time

import msvcrt

import math

cleanse=lambda: os.system('cls')
trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
empleados=[]
def menu():
    while True:
        try:
            cleanse()
            print('''----------Menu----------
1.-Asignar sueldos aleatorios
2.-Clasificar sueldos
3.-Estadisticas
4.-Reporte de sueldos
5.-Salir del programa
''')
            girasol=int(input('Opcion: '))
            if girasol in [1,2,4,5]:
                return girasol
            if girasol==3:
                cleanse()
                print('Opciones de reporte\n1.-Csv')
                girasol=int(input('Opcion: '))
                if girasol==1:
                    reporte()
                    print('Csv creado')
                    msvcrt.getch()
        except ValueError:
            print('Error')
            time.sleep(1)
def asignar():
    for melon in trabajadores:
        coco={}
        sueldo=random.randint(300000,2500000)
        coco={'Nombre':melon,'Sueldo':sueldo,'Descuento Salud':int(sueldo*0.07),'Descuento Afp':int(sueldo*0.12),'Descuento Liquido':int(sueldo*0.81)}
        empleados.append(coco)
def clasificar():
    total=0
    menor=[i for i in empleados if i['Sueldo']<=800000]
    mitad=[i for i in empleados if i['Sueldo']>800000 and i['Sueldo']<=2000000]
    mayor=[i for i in empleados if i['Sueldo']>2000000]
    print(f'Sueldos menores a $800.000 TOTAL: {len(menor)}')
    print('Nombre\t\tSueldo')
    for melon in menor:
        print(f'{melon['Nombre']}\t${melon['Sueldo']:,}')
    print(f'Sueldos entre $800.000 y $2.000.000 Total:{len(mitad)}')
    print('Nombre\t\tSueldo')
    for melon in mitad:
        print(f'{melon['Nombre']}\t${melon['Sueldo']:,}')
    print(f'Sueldos superiores a $2.000.000 TOTAL{len(mayor)}')
    print('Nombre\t\tSueldo')
    for melon in mayor:
        print(f'{melon['Nombre']}\t${melon['Sueldo']:,}')
    for melon in empleados:
        total+=melon['Sueldo']
    print(f'Total De Los Sueldos: ${total:,}')
def reporte():
    with open('Reporte De Sueldos.csv','w',newline='') as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(['Nombre empleado','Sueldo Base','Descuento Salud','Descuento AFP','Sueldo Liquido'])
        for melon in empleados:
            escritor.writerow([melon['Nombre'],melon['Sueldo'],melon['Descuento Salud'],melon['Descuento Afp'],melon['Descuento Liquido']])
def estadistica():
    if not empleados:
        asignar()
    larga=max(empleados,key=lambda x: x['Sueldo'])
    corta=min(empleados,key=lambda x: x['Sueldo'])
    print(f'Sueldo mas alto {larga['Nombre']} con un sueldo de ${larga['Sueldo']:,}')
    print(f'Sueldo mas bajo {corta['Nombre']} con un sueldo de ${corta['Sueldo']:,}')
    total2=sum(melon['Sueldo'] for melon in empleados)
    total2=int(total2/10)
    print(f'El promedio de sueldos es de ${total2:,}')
    total2=math.prod(melon['Sueldo'] for melon in empleados)
    total2=math.pow(total2,1/10)
    print(f'La media geometrica de los sueldos es ${int(total2):,}')
while True:
    nope=menu()
    if nope==1:
        asignar()
        print('Sueldos Establecidos!')
        msvcrt.getch()
    elif nope==2:
        cleanse()
        clasificar()
        msvcrt.getch()
    elif nope==4:
        cleanse()
        estadistica()
        msvcrt.getch()
    else:
        cleanse()
        print("Finalizando programa.....")
        time.sleep(0.3)
        cleanse()
        print('Desarrollador por Gonzalo')
        print('RUT 20.299.247-1')
        time.sleep(1)
        break