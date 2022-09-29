import RPi.GPIO as GPIO
import MFRC522
import signal
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

continue_reading = True

def end_read(signal, frame):
    global continue_reading
    print("Ctrl´´ captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)
#Crear el objeto de lectura


def readRFID():
    print("Acerque la tarjeta al lector")
    id, text = reader.read()
    print(text)

def readRFIDReturnText():
    print("Acerque la tarjeta al lector")
    id, text = reader.read()
    return text

menu = "Menú de opciones\n\t1.Leer registros.\nIngrese la opción que desesa ejecutar (ej:4\n"

def showTerminal():
    while True:
        option = input(menu)
        if option == "1":
            print("Leyendo registro")
            readRFID()
        else:
            print("Opción no válida")

showTerminal()