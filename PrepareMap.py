class Convert:
    licznik = 0
    dlugosc = 0

    @staticmethod
    def to_map():
        dump = open("dump.txt", "r").read()
        mapfile = open("map.txt", "a")
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
            print(line)
            line_to_table = line.split(';')

            print("linetotable:")
            print(line_to_table)
           # pisz = str(line_to_table[1] + ",")
            mapfile.write(line_to_table[0] + ",")
            Convert.licznik += 1
