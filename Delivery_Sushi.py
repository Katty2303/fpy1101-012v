import os
import time

limpieza_pantalla = "cls"
respuesta = True
rolls_pikachu = 0
rolls_otaku = 0
rolls_pulpo = 0
rolls_anguila = 0
opcion = 0
descuento = 0
codigo_descuento = True
os.system(limpieza_pantalla)

while respuesta == True:
    while opcion !=5:
        time.sleep(2)
        os.system(limpieza_pantalla)
        print("******** Menú Sushi Python ********")
        print("1. Pikachu Roll\t\t\t$4500")
        print("2. Otaku Roll\t\t\t$5000")
        print("3. Pulpo Venenoso Roll\t\t$5200")
        print("4. Anguila Eléctrica Roll\t$4800")
        
        try:
            opcion = int(input("¿Qué Roll deseas agregar?, elige una opción (1-4): "))
        except ValueError:
            print("Selecciona una opción (1-4), ya que la elegida es incorrecta")
            continue

        if opcion == 1:
            rolls_pikachu = rolls_pikachu + 1
            total_productos = rolls_pikachu
            total_pagar = rolls_pikachu * 4500
            print(f"Has agregado: {total_productos} productos y el valor a cancelar es de: ${total_pagar}")
        elif opcion == 2:
            rolls_otaku = rolls_otaku + 1
            total_productos = rolls_otaku
            total_pagar = rolls_otaku * 5000
            print(f"Has agregado: {total_productos} productos y el valor a cancelar es de: ${total_pagar}")
        elif opcion == 3:
            rolls_pulpo = rolls_pulpo + 1
            total_productos = rolls_pulpo
            total_pagar = rolls_pulpo * 5200
            print(f"Has agregado: {total_productos} productos y el valor a cancelar es de: ${total_pagar}")
        elif opcion == 4:
            rolls_anguila = rolls_anguila + 1
            total_productos = rolls_anguila
            total_pagar = rolls_anguila * 4800
            print(f"Has agregado: {total_productos} productos y el valor a cancelar es de: ${total_pagar}")
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
        print("¿Desea agregar algo màs a su pedido?\n")
        respuesta_pedido = int(input("1. Si\n2. No\nResponda: "))
        if respuesta_pedido == 1:
            break
        else:
            print("¿Posee algùn còdigo de descuento?")
            
            while codigo_descuento == True:
                respuesta_codigo = int(input("1. Si\n2. No\nResponda: "))
                if respuesta_codigo == 1:
                    codigo = input("Ingrese su còdigo de descuento: ")
                    if codigo == "soyotaku":
                        descuento = total_pagar * 0.1
                        total = total_pagar - descuento
                    else:
                        print("Còdigo no vàlido")
                        print("¿Desea reingresar el còdigo, coloque una X")
                        opcion_codigo = (input("1. Si\n2. No\nResponda: "))
                        if opcion_codigo == "X":
                            codigo_descuento == True
                        else:
                            break 
                else:
                    print(f"TOTAL PRODUCTOS: {total_productos}")   
                    print(f"Pikachu Roll: {rolls_pikachu}") 
                    print(f"Otaku Roll: {rolls_otaku}") 
                    print(f"Pulpo Venenoso Roll: {rolls_pulpo}") 
                    print(f"Anguila Elèctrica Roll: {rolls_anguila}") 
                    print(f"Subtotal por pagar: {total_pagar}") 
                    print(f"Descuento por còdigo: {descuento}") 
                    print(f"Total: {total}") 
              
time.sleep(2)
os.system(limpieza_pantalla)
print(total_productos)
respuesta = False