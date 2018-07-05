import time #se necesita para usar las funciones de tiempo
from subprocess import call #la necesitamos para la interrupcion de teclado
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) #Queremos usar la numeracion de la placa

def setup(Trig,Echo):

    #Hay que configurar ambos pines del HC-SR04
    GPIO.setup(Trig, GPIO.OUT)
    GPIO.setup(Echo, GPIO.IN)

#Para leer la distancia del sensor al objeto, creamos una funcion
def detectarObstaculo(Trig,Echo):

   GPIO.output(Trig, False) #apagamos el pin Trig
   time.sleep(2*10**-6) #esperamos dos microsegundos
   GPIO.output(Trig, True) #encendemos el pin Trig
   time.sleep(10*10**-6) #esperamos diez microsegundos
   GPIO.output(Trig, False) #y lo volvemos a apagar

  #empezaremos a contar el tiempo cuando el pin Echo se encienda
   while GPIO.input(Echo) == 0:
      start = time.time()

   while GPIO.input(Echo) == 1:
      end = time.time()

   #La duracion del pulso del pin Echo sera la diferencia entre
   #el tiempo de inicio y el final
   duracion = end-start

   #Este tiempo viene dado en segundos. Si lo pasamos
   #a microsegundos, podemos aplicar directamente las formulas
   #de la documentacion
   duracion_micro = duracion*10**6
   medida = duracion_micro/58 #hay que dividir por la constante que pone en la documentacion, nos dara la distancia en cm
   
    return {"duracion":duracion,"medida":medida}

def destroy(Trig,Echo):
    #por ultimo hay que restablecer los pines GPIO
    print "Limpiando..."
    GPIO.output(Trig,GPIO.LOW)
    GPIO.cleanup()
    print "Acabado."

#Bucle principal del programa, lee el sensor. Se sale con CTRL+C
if __name__ == '__main__':
    #Definimos los dos pines del sensor que hemos conectado: Trigger y Echo
    Trig = 11
    Echo = 13
    setup(Trig, Echo)
    while True:
        try:
            resultado = detectarObstaculo(Trig,Echo)
            if resultado["medida"] <=5:
                print "%.2f" %resultado["medida"] #por ultimo, vamos a mostrar el resultado por pantalla
                time.sleep(0.5)
        except KeyboardInterrupt:
            destroy(Trig,Echo)