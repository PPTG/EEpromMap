import PySimpleGUI as sg
from Serial import *
from PrepareMap import *
import os

window_width = 1000
window_height = 520
sg.theme('Dark 2')
com_select = ('COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7','COM8','COM9','COM10','COM20','COM22')
baudrate_select = ('9600','19200','11200','500000','2000000')
layout = [
    [sg.Canvas(background_color='grey', size=(window_width,window_height),key='canvas')],
    [sg.Text('Port:'),sg.Combo(com_select,default_value=com_select[0], s=(15,22), enable_events=True, readonly=True, k='-com-'),sg.Text('Baud:'),sg.Combo(baudrate_select,default_value=baudrate_select[0], s=(15,22), enable_events=True, readonly=True, k='-baud-')],
    [sg.Text('Display cell number: '),sg.Checkbox('saved cells', default=True, enable_events=True, key='-cellsave-'),sg.Checkbox('empty cells', default=False, enable_events=True, key='-cellempty-')],
    [sg.Submit('Read EEprom'), sg.Cancel('Exit')]
]
window = sg.Window('EEpromMap', layout)

def make_map():
#    eeprom_map.margin = eeprom_map.size -1
#    eeprom_map.x = eeprom_map.margin
#    eeprom_map.y = eeprom_map.size + eeprom_map.size
#    window['canvas'].TKCanvas.delete("all")

    dump.eeprom(1)
    Convert.to_map()
    eeprom_map.draw(1, "map.txt")

class eeprom_map:
    cellnumber=1
    size = 20
    margin = size - 1
    licznik = 0
    x = margin
    y = size + size
    window_width = 1000
    window_height = 500

    def draw(self, zrodlo):
        preparedmap_file = open(zrodlo, "r")
        map_file = preparedmap_file.read()
        liczba = map_file.split(",")
        ilosc = len(liczba) -1

        while (eeprom_map.licznik < ilosc):
            wartosc = int(liczba[eeprom_map.licznik])
            if (wartosc == 0):
                window['canvas'].TKCanvas.create_rectangle(eeprom_map.x, eeprom_map.y,eeprom_map.x + eeprom_map.size,eeprom_map.y + eeprom_map.size, fill="lime")
                if(eeprom_map.cellnumber == 3 or eeprom_map.cellnumber == 2 ):
                    window['canvas'].TKCanvas.create_text(eeprom_map.x + 10, eeprom_map.y + 8, fill="black",font="Times 6 italic bold", text=str(eeprom_map.licznik))

                eeprom_map.x = eeprom_map.x + (eeprom_map.size + 1)


            if (wartosc != 0):
                window['canvas'].TKCanvas.create_rectangle(eeprom_map.x, eeprom_map.y,eeprom_map.x + eeprom_map.size,eeprom_map.y + eeprom_map.size, fill="red")
                if (eeprom_map.cellnumber == 3 or eeprom_map.cellnumber == 1):
                    window['canvas'].TKCanvas.create_text(eeprom_map.x + 10, eeprom_map.y + 8, fill="black", font="Times 6 italic bold",text=str(eeprom_map.licznik) )
                eeprom_map.x = eeprom_map.x + (eeprom_map.size + 1)

            if (eeprom_map.x > eeprom_map.window_width - eeprom_map.size):
                eeprom_map.y = eeprom_map.y + eeprom_map.size
                eeprom_map.x = eeprom_map.margin
            eeprom_map.licznik += 1
        preparedmap_file.close()

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        if os.path.exists("dump.txt"):
            os.remove("dump.txt")
        if os.path.exists("map.txt"):
            os.remove("map.txt")
        break
    if (event == '-cellempty-' or event == '-cellsave-'):
        if(values['-cellempty-'] == False):
            eeprom_map.cellnumber=1

        if (values['-cellsave-'] == False):
            eeprom_map.cellnumber = 2

        if (values['-cellsave-'] == True and values['-cellempty-'] == True ):
            eeprom_map.cellnumber = 3

        if (values['-cellsave-'] == False and values['-cellempty-'] == False ):
            eeprom_map.cellnumber = 0

    if event == '-com-':
        selected_com = values['-com-']
        Serial.changeport(1,selected_com)
    if event == '-baud-':
        selected_baud = values['-baud-']
        Serial.changebaud(1,selected_baud)
    if event == 'Read EEprom':
        make_map()