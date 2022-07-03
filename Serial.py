import serial
import time
import io
f = open("dump.txt", "a")
class Connection:
    port_selected = "COM5"
    baud_selected = 2000000
    ser = 0

    def changeport(self, b):
        Connection.port_selected = b
        print("Selected PORT: ")
        print(Connection.port_selected)

    def changeBaud(self, c):
        Connection.baud_selected = c
        print("Set Baud Rate to :")
        print(Connection.baud_selected)

    def connect(self):
        print("Connecting...")
        Connection.ser = serial.Serial(Connection.port_selected, Connection.baud_selected)
        print(Connection.ser.name)
        time.sleep(3)
        print("Conneced!")

    def disconnect(self):
        Connection.ser.close()
        print("Disconneced!")

    def send(self, a):
        Connection.ser.write(a)
        print("Sending:")
        print(a)


class dump:
    licznik=0
    def eeprom(self):
        f = open("dump.txt", "a")
        ser = serial.Serial(Connection.port_selected,Connection.baud_selected, timeout=2)
        time.sleep(3)
        ser.write(b'E')

        x = ser.readlines()

        for line in x:
            print(line)
            if(dump.licznik > 0):
                f.write(line.decode("utf-8"))
            dump.licznik+=1
        f.close()
    def dump_clear(self):
        dump.licznik = 0


