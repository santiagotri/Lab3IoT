import RPi.GPIO as GPIO
import MFRC522
import signal
from mfrc522 import SimpleMFRC522

continue_reading = True

def end_read(signal, frame):
    global continue_reading
    print("Ctrl´´ captured, ending read.")
    continue_reading = False
    GPIO.cleanup()


#Crear el objeto de lectura

def readRFIDReturnText():
    reader = SimpleMFRC522()
    signal.signal(signal.SIGINT, end_read)
    print("Acerque la tarjeta al lector")
    id, text = reader.read()
    return text
