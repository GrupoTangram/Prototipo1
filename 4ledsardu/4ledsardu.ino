#include <EEPROM.h>

char tmpKey;  //Memory index
int i = 0;
void setup() {
  
  //Start Serial
  Serial.begin(9600);
  
  //configure input Buttons
  for(int i = 2;i<=4;i++){
      pinMode(i,INPUT);
    }
}

void loop() {
    //Check if there is data coming from Python
    if(Serial.available()>0){
        tmpKey = Serial.read();
        EEPROM.put(i,tmpKey);
        if(i == 2){
            i = 0;
          }else{
            i++;  
          }
        
      }
    
    
    
    //Buttons Handles
    for(int index = 0;index<3;index++){ 
      if(digitalRead(index+2) == HIGH){
          Serial.print(EEPROM.read(index));
          Serial.print("\n");
          delay(250);
      }
    }
  
}
  
 

