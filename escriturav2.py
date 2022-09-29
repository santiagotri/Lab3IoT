import RPi.GPIO as GPIO
import MFRC522
import signal
from mfrc522 import SimpleMFRC522

continue_reading = True

def end_read(signal,  frame):
    global continue_reading
    print("Ctrol+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)

#crear el objeto reader

MIFAREReader = MFRC522.MFRC522()
reader = SimpleMFRC522()

def griteRegistro():
    print("==================\n Agregar registro\n==================")
    nombres = input("Ingrese el texto a escribir\n")
    print("Coloque el chip RFID sobre el lector")
    reader.write(nombres)
    print("Escrito")

menu = "Menú de opciones\n\t1. Leer registros.\nIngrese la opciónque desea ejecutar (ej:1)\n"

def showTerminal():
    while True:
        option = input(menu)
        if option=="1":
            print("Leyendo registro")
            readRFID()
        elif option == "2":
            griteRegistro()
        else:
            print("Opción no valida")
showTerminal()
