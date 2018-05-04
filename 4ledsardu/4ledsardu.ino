#include <EEPROM.h>

int i = 0;   //Memory index

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
       
    //Buttons Handles
    for(int index = 0;index<3;index++){ 
      if(digitalRead(index+2) == HIGH){
          Serial.print(EEPROM.read(index),DEC);
          Serial.print("\n");
          delay(250);
      }
    }
  
}
  
 

