import serial
import time
class Connection:
    port_selected = "COM5"
    baud_selected = 2000000
    ser = 0

    def changeport(self, b):
        Connection.port_selected = b

    def changebaud(self, c):
        Connection.baud_selected = c

    def connect(self):
      #  print("Connecting...")
        Connection.ser = serial.Serial(Connection.port_selected, Connection.baud_selected)
        time.sleep(3)

    def disconnect(self):
        Connection.ser.close()

    def send(self, a):
        Connection.ser.write(a)

class dump:
    licznik=0
    def eeprom(self):
        eeprom_copy = open("dump.txt", "a")
        f = eeprom_copy
        ser = serial.Serial(Connection.port_selected,Connection.baud_selected, timeout=2)
        time.sleep(3)
        ser.write(b'E')
        x = ser.readlines()

        for line in x:
         #   print(line)
            if(dump.licznik > 0):
                f.write(line.decode("utf-8"))
            dump.licznik+=1
        eeprom_copy.close()
    def dump_clear(self):
        dump.licznik = 0
