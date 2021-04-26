import pandas as pd
import datetime
import csv
import sys
import os.path

separador = ("-" * 20) + "\n"
ciclo = 1
opcion =1
ventas_num = 0

if os.path.exists("Productos.csv") == True:
    productos = pd.read_csv("Productos.csv", index_col=0)
else:
   prod_dict = {'Nombre':['Labial','Rimel','Sombras','Corrector','Esmalte de uñas','Delineador','Cejas'],
                 'Precio':[20,50,80,60,15,20,30],
                 'Descripcion':['Mate sin resecar labios','Pestañas largas','Diferentes colores','Con Glitter','No te saca arrugas','Delineadores mate','Solo colores cafes']}
   productos = pd.DataFrame(prod_dict)

if os.path.exists("Ventas.csv") == True:
    ventas = pd.read_csv("Ventas.csv", index_col=0)
else:
    ventas = pd.DataFrame(columns=["Fecha", "Hora", "Folio", "Cantidad", "Pago total"])

print ("*Menu de opciones* \n")
while ciclo == 1:
    print("1.- Añadir una nueva venta")
    print("2.- Consultar una venta")
    print("3. Salir")
    print()

    opcion = int(input("Elige la opcion deseada: \n"))
    print (separador)

    if opcion == 1:
        precio_total = 0
        while opcion == 1:
            print(productos['Nombre'])
            print(separador)

            folio_venta = int(input("Folio \n>"))
            venta_cantidad = int(input("Cantidad \n>"))
            opcion = int(input("Desea agregar otro producto? 1.Si 2.No \n>"))
            precio_total += productos.iloc[folio_venta,1] * venta_cantidad
            print(" ")

        fecha_hora = datetime.datetime.now().replace(microsecond=0)
        fecha_sola = fecha_hora.date()
        hora_sola = fecha_hora.time()

        ventas = ventas.append({'Fecha':fecha_sola.strftime('%d/%m/%y'), 'Hora':hora_sola.strftime('%H:%M:%S'), 'Folio':folio_venta, 'Cantidad':venta_cantidad, 'Pago total':precio_total}, ignore_index=True)
        print(f'Precio total a pagar: {precio_total}')
        print(separador)

    elif opcion == 2:
        fecha_capt = input("Que fecha desea consultar? Por ejemplo '22/04/2021' dd/mm/aa \n>")
        try:
            df = pd.read_csv('Ventas.csv')
            dfl = pd.DataFrame(df)
            print(dfl[dfl.Fecha == a])
        except:
            print(f'Ha ocurrido un error')

    elif opcion == 3:
        print("EJECUCION FINALIZADA")
        break