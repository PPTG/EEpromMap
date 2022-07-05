#include <EEPROM.h>
#define COM_Speed 2000000
#define COM Serial

int zadanie=0;
byte command=0;

byte value;
int address = 0;

String readString, COM_String;
void setup() {
  COM.begin(COM_Speed);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

}

void loop() {
  com();
}
