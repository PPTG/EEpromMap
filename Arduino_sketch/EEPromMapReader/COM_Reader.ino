void com(){
while (COM.available()) { 
  if (COM.available() >0) {
    char c = COM.read();  
    readString += c; 
    if(c=='E'){
      command=1;
    }
  }
}
   
if (readString.length() >0) {
  COM_String = readString.substring(1,4); 
  int n1 = COM_String.toInt();
  if(command == 1 ){
    memread();
    zadanie=n1;
    command=0;
    address = 0;
    value=0;
    }
    readString="";
  }
}
