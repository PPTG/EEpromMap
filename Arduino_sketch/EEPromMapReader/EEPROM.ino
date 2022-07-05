void memread(){
  while(address != EEPROM.length()){
  value = EEPROM.read(address);
  Serial.print("E");
  Serial.print(value,DEC);
  Serial.print("\n");
  address = address + 1;
  if (address == EEPROM.length()) {
    return;
  }
}
}
