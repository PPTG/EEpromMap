
"""
class CallBack:

    def detect_eeprom(self,lenght):

        if (lenght == 512 + 1):
            tkMessageBox.showinfo("512 bytes", "Arduino Duemilanove EEprom Detected!")

        if (lenght == 1024 + 1):

            tkMessageBox.showinfo("1023 bytes", "Arduino Uno/Leonardo EEprom Detected!")

        if (lenght == 4096 + 1):
            tkMessageBox.showinfo("4096 bytes", "Arduino Mega EEprom Detected!")
"""



class draw_map:
    size=40
    margin=size - 1
    licznik=0
    x = margin
    y = size + size
    window_width = 1000
    window_height = 500
    def draw(self,zrodlo):
        file = open(zrodlo, "r").read()
        liczba = file.split(",")
        ilosc = len(liczba)
      #  CallBack.detect_eeprom(1,ilosc)
        print("EEprom size:", ilosc, "bytes")

        while (draw_map.licznik < ilosc):
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
        file.close()