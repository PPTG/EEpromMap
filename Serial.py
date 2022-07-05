import serial
import time
class Serial:
    port_selected = "COM1"
    baud_selected = 9600
    ser = 0

    def changeport(self, b):
        Serial.port_selected = b

    def changebaud(self, c):
        Serial.baud_selected = c

    def connect(self):
      #  print("Connecting...")
        Serial.ser = serial.Serial(Serial.port_selected, Serial.baud_selected)
        time.sleep(3)

    def disconnect(self):
        Serial.ser.close()

    def send(self, a):
        Serial.ser.write(a)

class dump:
    licznik=0
    def eeprom(self):
        eeprom_copy = open("dump.txt", "a")
        f = eeprom_copy
        ser = serial.Serial(Serial.port_selected,Serial.baud_selected, timeout=2)
        time.sleep(3)
        ser.write(b'E')
        x = ser.readlines()

        for line in x:
            print(line)
            f.write(line.decode("utf-8"))
            dump.licznik+=1
        eeprom_copy.close()
    def dump_clear(self):
        dump.licznik = 0
