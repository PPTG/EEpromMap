#Python EEpromMap drawer based on reding cell state from arduino eeprom


import PySimpleGUI as sg
#import random
from Serial import *
#from DrawMap import *
from PrepareMap import *

window_width = 1000
window_height = 520
sg.theme('Dark 2')
com_select = ('COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7')
baudrate_select = ('9600','11200','2000000')
layout = [
    [sg.Canvas(background_color='grey', size=(window_width,window_height),key='canvas')],
    [sg.Text('Port:'),sg.Listbox(com_select, size=(10), key='-com-')],
    [sg.Text('Baud:'),sg.Listbox(baudrate_select, size=(10), key='-baud-')],
    [sg.Submit('Read EEprom'), sg.Cancel()]
]
window = sg.Window('Arduino EEpromMap', layout, finalize=True)
cir = window['canvas'].TKCanvas.create_rectangle(0, 0, 10, 10)

class draw_map:
    size=20
    margin=size - 1
    licznik=0
    x = margin
    y = size + size
    window_width = 1000
    window_height = 500
    def draw(self,zrodlo):
        map_file = open(zrodlo, "r").read()
        liczba = map_file.split(",")
        ilosc = len(liczba) -1
      #  CallBack.detect_eeprom(1,ilosc)
        print("EEprom size:", ilosc, "bytes")

        while (draw_map.licznik < ilosc):
            print("drawmap: ",liczba[draw_map.licznik])
            wartosc=int(liczba[draw_map.licznik])
            if(wartosc == 0):
                window['canvas'].TKCanvas.create_rectangle(draw_map.x,draw_map.y, draw_map.x+draw_map.size, draw_map.y+draw_map.size, fill="lime")
                draw_map.x = draw_map.x + (draw_map.size + 1)

            if(wartosc != 0):
                window['canvas'].TKCanvas.create_rectangle(draw_map.x,draw_map.y, draw_map.x+draw_map.size, draw_map.y+draw_map.size, fill="red")
                draw_map.x=draw_map.x+(draw_map.size + 1)
            if(draw_map.x > draw_map.window_width - draw_map.size):
                draw_map.y=draw_map.y+draw_map.size
                draw_map.x=draw_map.margin
            draw_map.licznik +=1
        

def map():

  #  dump.eeprom(1)
  #  Convert.to_map()
    draw_map.draw(1, "map.txt")

"""
def draw(self,licznik):
    while(licznik < 70):
        color = random.randint(100, 255)
        window['canvas'].TKCanvas.create_rectangle(licznik,  licznik, 2,2, outline= "#" + str(color), width=2,fill="#"+str(color)) #fill= "#"+str(color)

     #   window['canvas'].TKCanvas.create_rectangle(20, 20, 40,  0, outline= "#" + str(color), width=2,fill="#"+str(color)) #fill= "#"+str(color)
     #   window['canvas'].TKCanvas.create_rectangle(40, 20, 60,  0, outline= "#" + str(color), width=2,fill="#"+str(color)) #fill= "#"+str(color)
        licznik+=1
"""
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == 'Read EEprom':
        #draw(1,10)
        map()











