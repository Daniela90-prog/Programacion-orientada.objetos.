class JuegoAprenderProgramacion:
    def __init__(self):
        self.nombreDeUsuario = input("Ingresa tu nombre: ")
        self.maxintentos = 2
        self.continuar_juego = True

    def iniciar_juego(self):
        print("Juega y programa")
        print("¡Hola! ¡Bienvenidos! Te presento el juego donde aprenderás a programar con ejercicios que te ayudarán a mantener tu aprendizaje cada día.")
        print("Comencemos.")
        print("Las únicas reglas son: todas tus respuestas deben ingresarse en minúsculas y tienes un máximo de 2 intentos por pregunta.")
        
        print(f"¡Hola, {self.nombreDeUsuario}!")

        while self.continuar_juego:
            print("Tengo una pregunta.")
            intento = 0

            while intento < self.maxintentos:
                respuesta = input("¿Estás listo? (sí/no): ")
                if respuesta == "si":
                    print("Ok, puedes continuar.")
                    break
                elif respuesta == "no":
                    print("Respuesta incorrecta.")
                    self.continuar_juego = False
                    break
                else:
                    print("Respuesta incorrecta")
                    intento += 1
            else:
                print("Agotaste tus intentos. El juego termina.")
                self.continuar_juego = False

            if self.continuar_juego:  # este lo hago para que cuando el jugador agote su número de intentos se rompa el ciclo
                if not self.nivel_1():
                    break
                if not self.nivel_2():
                    break
                if not self.nivel_3():
                    break

        if self.continuar_juego:
            print("El juego ha terminado. Gracias por jugar y aprender.")   

    def nivel_1(self):
        intento = 0
        print("Lección 1 \n Definición de Python")
        pregunta1 = "Python es un lenguaje de alto nivel de programación que se utiliza para desarrollar aplicaciones de todo tipo, como Netflix, Spotify, Instagram, entre otros. \n De acuerdo a la definición anterior, selecciona la respuesta correcta "
        opciones1 = "a) Python es un lenguaje de alto nivel de programación que se utiliza para desarrollar aplicaciones de todo tipo.\nb) Python es un juego de acción."
        print(pregunta1)
        print(opciones1)

        while intento < self.maxintentos:
            respuesta1 = input("¿Cuál es la respuesta correcta? (a/b): ")
            if respuesta1 == "a":
                print("Respuesta correcta. ¡Bien hecho!")
                return True
            elif respuesta1 == "b":
                print("Respuesta incorrecta, inténtalo de nuevo.")
                intento += 1
            else:
                print("Respuesta incorrecta, por favor, elige 'a' o 'b'.")
        else:
            print("Agotaste tus intentos en el nivel 1.")
            return False

    def nivel_2(self):
        intento = 0
        print("Lección 2 \n Tipos de Variables")
        pregunta2 = "nombre = Diana #string.str , los textos van entre comillas. \n números = 25 #el formato de números siempre será int \n decimal = 45,9  # el formato de números decimales es float. \n Reto lección No.2 Elige la opción correcta \n tenemos el tipo de variable longitud_del_camino = 45.9 "
        opciones2 = "a) float \n b) str"
        print(pregunta2)
        print(opciones2)

        while intento < self.maxintentos:
            respuesta2 = input("¿Cuál es la respuesta correcta? (a/b): ")
            if respuesta2 == "a":
                print("Respuesta correcta. ¡Bien hecho!")
                return True
            elif respuesta2 == "b":
                print("Respuesta incorrecta, inténtalo de nuevo.")
                intento += 1
            else:
                print("Respuesta incorrecta, por favor, elige 'a' o 'b'.")
        else:
            print("Agotaste tus intentos en el nivel 2.")
            return False

    def nivel_3(self):
        intento = 0
        print("Lección 3 \n Condicionales if, elif y else")
        pregunta3 = "El condicional (if) se utiliza cuando se cumple una condición, adicionalmente, viene acompañado de (elif) para establecer otro punto de comparación y (else) es la negación de dichas condiciones. \n Reto lección No.3 Compila y diviértete"
        opciones3 = "a) Compilar y divertirse \n b) Esperar y ver"
        print(pregunta3)
        print(opciones3)

        while intento < self.maxintentos:
            respuesta3 = input("¿Cuál es la respuesta correcta? (a/b): ")
            if respuesta3 == "a":
                print("Respuesta correcta. ¡Bien hecho!")
                return True
            elif respuesta3 == "b":
                print("Respuesta incorrecta, inténtalo de nuevo.")
                intento += 1
            else:
                print("Respuesta incorrecta, por favor, elige 'a' o 'b'.")
        else:
            print("Agotaste tus intentos en el nivel 3.")
            return False

if __name__ == "__main__":
    juego = JuegoAprenderProgramacion()
    juego.iniciar_juego()



