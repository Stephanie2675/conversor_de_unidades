"""1) Módulo temperatura.py: Este módulo debe contener funciones para convertir entre diferentes unidades de temperatura, como Celsius, Fahrenheit y Kelvin.(0.5 puntos) """
"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
"""3) Crear el primer versionamiento con git de los dos módulos creados de temperatura y masa (usar git add y git commit ). (0.5 puntos) """
"""4) Crear una nueva rama llamada “desarrollo” y en esta nueva rama agregar los módulos tiempo.py y convertidor.py (recuerda usar git branch ). (0.5 puntos) """
"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
"""6) Módulo convertidor.py: Este módulo importa los módulos de masa, temperatura y tiempo. Actúa como el punto de entrada del programa. Debe permitir a los usuarios seleccionar la categoría de conversión deseada (temperatura, masa o tiempo), ingresar el valor a convertir y las unidades de origen y destino, y obtener el resultado de la conversión.(2 puntos) """
"""7) Versionar esta rama “desarrollo” con git add y git commit para luego fusionar con la rama master (para fusionar, usar: git merge). (1 punto) """
""" Desde la rama main o master subir al nuevo repositorio de github llamado conversor_de_unidades. (1 punto) """

""" Recuerda que cada uno de los módulos, deben incluir el bloque if __name__ == "__main__" para sus pruebas en cada módulo. """
#Stephanie Aguero Ramirez
import temperatura
import masa
import tiempo 

def main():
    while True:
        # Muestra el menú principal
        print("Menú Principal:")
        print("[1] covertidor de celsius a fahrenheit")
        print("[2] covertidor de celsius a Kelvin ")
        print("[3] covertidor de Fahrenheit a Celsius")
        print("[4] covertidor de Fahrenheit a Kelvin")
        print("[5] covertidor de Kelvin a Celsius ")
        print("[6] covertidor de Kelvin a fahrenheit")
        print("[7] covertidor de Kilogramos a Gramos")
        print("[8] covertidor de Kilogramos a Toneladas")
        print("[9] covertidor de Gramos a Kilogramos")
        print("[10] covertidor de Gramos a Toneladas")
        print("[11] covertidor de Toneladas a Kilogramos")
        print("[12] covertidor de Toneladas a Gramos")
        print("[13] covertidor de Segundos a Minutos")
        print("[14] covertidor de Segundos a Horas")
        print("[15] covertidor de Minutos a Segundos")
        print("[16] covertidor de Minutos a Horas")
        print("[17] covertidor de Horas a Segundos")
        print("[18] covertidor de Horas a Minutos")
        print("[0] Salir")
        
        # Solicita al usuario que ingrese una opción
        opcion = input("Ingrese una opción: ")
        valorinicial=int(input("ingrese valor inicial: "))
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                resp= temperatura.celsius_a_fahrenheit(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 2:
                resp= temperatura.celsius_a_Kelvin(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 3:
                resp= temperatura.Fahrenheit_a_Celsius(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 4:
                resp= temperatura.Fahrenheit_a_Kelvin(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 5:
                resp= temperatura.Kelvin_a_Celsius(valorinicial)
                print("el resultado es: ", resp)
            
            elif opcion == 6:
                resp= temperatura.Kelvin_a_fahrenheit(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 7:
                resp= masa.Kilogramos_a_Gramos(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 8:
                resp= masa.Kilogramos_a_Toneladas(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 9:
                resp= masa.Gramos_a_Kilogramos(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 10:
                resp= masa.Gramos_a_Toneladas(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 11:
                resp= masa.Toneladas_a_Kilogramos(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 12:
                resp= masa.Toneladas_a_Gramos(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 13:
                resp= tiempo.Segundos_a_Minutos (valorinicial)
                print("el resultado es: ", resp)  

            elif opcion == 14:
                resp= tiempo.Segundos_a_Horas(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 15:
                resp= tiempo.Minutos_a_Segundos(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 16:
                resp= tiempo.Minutos_a_Horas(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 17:
                resp= tiempo.Horas_a_Segundos(valorinicial)
                print("el resultado es: ", resp)

            elif opcion == 18:
                resp= tiempo.Horas_a_Minutos(valorinicial)
                print("el resultado es: ", resp)

            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

if __name__ == "__main__":
    main()
    #https://github.com/Stephanie2675/conversor_de_unidades.git
    