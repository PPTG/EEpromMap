#include <EEPROM.h>
byte zrobione = 0;
unsigned int E_L[]={93,94,95,96,139,185,231,232,233,234,277,323,369,370,371,372};
unsigned int Ea_L[]={98,99,100,101,144,190,236,237,238,239,282,328,374,375,376,377};
unsigned int P_L[]={103,104,105,106,149,152,195,198,241,242,243,244,287,333,379};
unsigned int R_L[]={108,109,110,111,154,157,200,203,246,247,248,249,292,293,338,340,384,387};
unsigned int O_L[]={114,115,159,162,205,208,251,254,297,300,343,346,390,391};
unsigned int M_L[]={118,122,164,165,167,168,210,212,214,256,260,302,306,348,352,394,398};
unsigned int Ma_L[]={461,465,507,508,510,511,553,555,557,599,603,645,649,691,695,737,741};
unsigned int A_L[]={470,515,517,561,563,606,610,652,653,654,655,656,697,703,743,749};
unsigned int Pa_L[]={475,476,477,478,521,524,567,570,613,614,615,616,659,705,751};


void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop() {

while(zrobione < 1 ){

  for (int i = 0 ; i < EEPROM.length() ; i++) {
      EEPROM.write(i, 0);
    }

  for (byte b = 0; b < sizeof(E_L) / sizeof(int); b++) {
      EEPROM.write(E_L[b], 230);
      Serial.print("E:");
      Serial.println(b);   
    }

   for (byte c = 0; c < sizeof(Ea_L) / sizeof(int); c++) {
    EEPROM.write(Ea_L[c], 230);
    Serial.print("E2:");
    Serial.println(c);    
  }

   for (byte d = 0; d < sizeof(P_L) / sizeof(int); d++) {
    EEPROM.write(P_L[d], 230);
    Serial.print("P:");
    Serial.println(d);    
  }

   for (byte e = 0; e < sizeof(R_L) / sizeof(int); e++) {
    EEPROM.write(R_L[e], 230);
    Serial.print("R:"); 
    Serial.println(e);   
  }
   for (byte f = 0; f < sizeof(O_L) / sizeof(int); f++) {
    EEPROM.write(O_L[f], 230);
    Serial.print("O:"); 
    Serial.println(f);   
  }
  for (byte g = 0; g < sizeof(M_L) / sizeof(int); g++) {
    EEPROM.write(M_L[g], 230);
    Serial.println("M:");
    Serial.println(g);      
  }

  for (byte h = 0; h < sizeof(Ma_L) / sizeof(int); h++) {
    EEPROM.write(Ma_L[h], 230);
    Serial.print("M2:"); 
    Serial.println(h);   
  }

  for (byte i = 0; i < sizeof(A_L) / sizeof(int); i++) {
    EEPROM.write(A_L[i], 230);
    Serial.print("A:");
    Serial.println(i);    
  }

  for (byte j = 0; j < sizeof(Pa_L) / sizeof(int); j++) {
    EEPROM.write(Pa_L[j], 230);
    Serial.print("P2:");
    Serial.println(j);
      
  }
  zrobione = 1;
}
digitalWrite(13, HIGH);


}
