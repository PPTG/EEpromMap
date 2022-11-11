import PySimpleGUI as sg
from Serial import *
from PrepareMap import *
from win32api import GetSystemMetrics
import os

screenWidth = GetSystemMetrics(0)
screenHeight = GetSystemMetrics(1)
window_width = screenWidth-920
window_height = screenHeight-560
sg.theme('Dark 2')
com_select = ('COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'COM10', 'COM20', 'COM22')
baudrate_select = ('9600', '19200', '11200', '500000', '2000000')
layout = [
    [sg.Canvas(background_color='grey', size=(window_width, window_height), key='canvas')],
    [sg.Text('Port:'),sg.Combo(com_select, default_value=com_select[0], s=(15, 22), enable_events=True, readonly=True, k='-com-'), sg.Text('Baud:'), sg.Combo(baudrate_select, default_value=baudrate_select[0], s=(15, 22), enable_events=True, readonly=True, k='-baud-')],
    [sg.Text('Display cell number: '), sg.Checkbox('saved cells', default=True, enable_events=True, key='-cellsave-'), sg.Checkbox('empty cells', default=False, enable_events=True, key='-cellempty-')],
    [sg.Submit('Read EEprom'), sg.Cancel('Exit')]
]
window = sg.Window('EEpromMap', layout)


def make_map():
    dump.eeprom()
    Convert.to_map()
    EEpromMap.draw("map.txt")


class EEpromMap:
    cellnumber = 1
    size = 20
    margin = size - 1
    licznik = 0
    x = margin
    y = size + size
    window_width = 1000
    window_height = 500

    def draw(zrodlo):
        preparedmap_file = open(zrodlo, "r")
        map_file = preparedmap_file.read()
        liczba = map_file.split(",")
        ilosc = len(liczba) - 1

        while (EEpromMap.licznik < ilosc):
            wartosc = int(liczba[EEpromMap.licznik])
            if (wartosc == 0):
                window['canvas'].TKCanvas.create_rectangle(EEpromMap.x, EEpromMap.y, EEpromMap.x + EEpromMap.size,
                                                           EEpromMap.y + EEpromMap.size, fill="lime")
                if (EEpromMap.cellnumber == 3 or EEpromMap.cellnumber == 2):
                    window['canvas'].TKCanvas.create_text(EEpromMap.x + 10, EEpromMap.y + 8, fill="black",
                                                          font="Times 6 italic bold", text=str(EEpromMap.licznik))

                EEpromMap.x = EEpromMap.x + (EEpromMap.size + 1)

            if (wartosc != 0):
                window['canvas'].TKCanvas.create_rectangle(EEpromMap.x, EEpromMap.y, EEpromMap.x + EEpromMap.size,
                                                           EEpromMap.y + EEpromMap.size, fill="red")
                if (EEpromMap.cellnumber == 3 or EEpromMap.cellnumber == 1):
                    window['canvas'].TKCanvas.create_text(EEpromMap.x + 10, EEpromMap.y + 8, fill="black",
                                                          font="Times 6 italic bold", text=str(EEpromMap.licznik))
                EEpromMap.x = EEpromMap.x + (EEpromMap.size + 1)

            if (EEpromMap.x > EEpromMap.window_width - EEpromMap.size):
                EEpromMap.y = EEpromMap.y + EEpromMap.size
                EEpromMap.x = EEpromMap.margin
            EEpromMap.licznik += 1
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
        if (values['-cellempty-'] == False):
            EEpromMap.cellnumber = 1

        if (values['-cellsave-'] == False):
            EEpromMap.cellnumber = 2

        if (values['-cellsave-'] == True and values['-cellempty-'] == True):
            EEpromMap.cellnumber = 3

        if (values['-cellsave-'] == False and values['-cellempty-'] == False):
            EEpromMap.cellnumber = 0

    if event == '-com-':
        selected_com = values['-com-']
        Serial.changeport(selected_com)
    if event == '-baud-':
        selected_baud = values['-baud-']
        Serial.changebaud(selected_baud)
    if event == 'Read EEprom':
        make_map()
