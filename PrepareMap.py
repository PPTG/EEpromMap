class Convert:
    licznik = 0
    dlugosc = 0
    @staticmethod
    def to_map():
        plik_eeprom = open("dump.txt", "r")
        dump = plik_eeprom.read()
        plik_mapa = open("map.txt", "a")
        mapfile = plik_mapa
        dump = dump.replace("E", "")
        rp = dump.split("\n")
        Convert.dlugosc = len(rp)
        for line in rp:
            if (Convert.licznik == Convert.dlugosc - 1):
                Convert.licznik = 0
                Convert.dlugosc = 0
                from Serial import dump
                dump.dump_clear(1)
                return
            line_to_table = line.split(';')
           # pisz = str(line_to_table[1] + ",")
            mapfile.write(line_to_table[0] + ",")
            Convert.licznik += 1
        plik_eeprom.close()
        plik_mapa.close()