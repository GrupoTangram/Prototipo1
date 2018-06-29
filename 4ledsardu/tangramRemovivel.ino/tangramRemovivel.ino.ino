/*
 * This is the Arduino code for the Tangram project
 * 
 * Tangram:
 * The tangram has 3 buttons. This programs sends to the serial a number corresponding to
 * the function of the button pressed. The function of the button is identified by a
 * resistance that is in it.
 * 
 * This Program:
 * 1) Waits to have some tension on any of the 3 analog pin inputs
 * 2) When receive some tension it means that a button is pressed, according to the tension,
 *    checks the value of the tension, to verify what is the function of the button
 * 3) Sends the corresponding tag to the serial
 */
#include <EEPROM.h>

 
const int analogPin[1] = {A3  }; 
const float tolerance = 0.5; 
const float sourceVoltage = 5;
const float fixedRes = 330; 
const float numberOfButtons = sizeof(analogPin)/sizeof(int);

  int functionKeys[2][3] = {
      {1,220},
      {2,995}
    };


  float pinResistance(int pin){
    float pinVoltage = analogRead(pin)*sourceVoltage/1024; //The tension on the pin
    if (pinVoltage != sourceVoltage){ //avoid division by zero
      //float functionRes = fixedRes * pinVoltage/(sourceVoltage - pinVoltage);
      float functionRes = fixedRes * (sourceVoltage - pinVoltage)/pinVoltage;
      return functionRes;
    }; // end if
    return 0; //returns 0 insted when the button is not being pressed.instead of infinie(error)
  }; //end pinResistance function



  int functionTag(float resistance){
    for(int i = 0; i<2; i++){
      if ( (resistance < functionKeys[i][1]*(1 + tolerance)) and 
         (resistance > functionKeys[i][1]*(1 - tolerance)) ){
          return functionKeys[i][0]; //Return the function tag
         }; //end if
    }//end for loop
    
    return 0; //if nothing was found
  };

  void setup() { 
    Serial.begin(9600);
    for(int i = 0; i<2;i++){
      functionKeys[i][2] = EEPROM.read(i);
   
    }

  }
  int isConnected = 0;
  void loop() {
  
  if (Serial.available() > 0) {
    
    Serial.read();
    int i = 0;
    while(i<2){
        Serial.println(functionKeys[i][2]);
        i++;
      }
    isConnected = 1;
  }else if(isConnected){
      int pressedKey = functionTag(pinResistance(A3));
      Serial.println(pressedKey); 
      if(pressedKey > 0 ){
          functionKeys[pressedKey-1][2] += 1;
          EEPROM.write(pressedKey-1,functionKeys[pressedKey-1][2]);
          delay(1000);
        }
        delay(100);
    }

  
  
}
