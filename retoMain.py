from retoLecturaRFID import readRFIDReturnText

#Librerias para el manejo de la matriz led
import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from lecturaLED import readRFIDReturnText

#Variables

listaPersonas = [None,None,None,None]

#Metodos
def imprimirMensaje(msg):
    # create matrix device
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=0 or 1, bloque_orientation=180, rotate=3 or 1)
    print("[-] Matriz initialized") #print para debuggear mas facil
    print("[-] Imprimiendo: %s" % msg) #print para debuggear mas facil
    show_message(device, msg, fill="red" , font=proportional(CP437_FONT), scroll_delay=0.1)

def imprimirEspacios():
    global listaPersonas
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=1)
    with canvas(device) as draw:
        # cuadrante1#
        if listaPersonas[0] is not None:
            draw.rectangle((0, 7, 3, 4), fill=1)
        # cuadrante2
        if listaPersonas[1] is not None:
            draw.rectangle((0, 0, 3, 3), fill=1)
        # cuadrante3#
        if listaPersonas[2] is not None:
            draw.rectangle((4,3,7,0),fill=1)
        # cuadrante3#
        if listaPersonas[3] is not None:
            draw.rectangle((7, 4, 4, 7), fill=1)
    print("INFO: Espacios actualizados") #print para debuggear mas facil


def eliminarPersona(informacionPersona):
    global listaPersonas
    for i in range(len(listaPersonas)):
        if listaPersonas[i]==informacionPersona:
            listaPersonas[i]=None
            print("INFO: Salio la persona: " + informacionPersona + ", espacio liberado #"+str(i+1)) #print para debuggear mas facil
    imprimirMensaje("Adios "+informacionPersona)

def anadirPersona(informacionPersona):
    global listaPersonas
    for i in range(len(listaPersonas)):
        if listaPersonas[i]==None:
            listaPersonas[i]=informacionPersona
            print("INFO: Llego la persona: " + informacionPersona + ", espacio asignado #"+str(i+1)) #print para debuggear mas facil
            break
    imprimirMensaje("Bienvenido "+informacionPersona)

#Main
while(True):
    informacionPersona = ""
    while informacionPersona == "":
        informacionPersona = readRFIDReturnText()
    print("RFID: " + informacionPersona) #print para debuggear mas facil
    if informacionPersona in listaPersonas:
        anadirPersona()
    else:
        eliminarPersona()
    imprimirEspacios()

