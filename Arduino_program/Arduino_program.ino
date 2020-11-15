/*
Automatic PC battery charger - Arduino_program v1.2
AkamaiSoftware © - 2019. All rights reserved.
*/

const int input = 2;
const int output = 8;

void setup() 
{
   Serial.begin(9600);
   pinMode(input,INPUT);
   pinMode(output,OUTPUT);
}
 
void loop()
{
  if(digitalRead(input)>0)
  {
    if(Serial.available()>0) 
    {
      int Q = Serial.read() - 48; //The input comes in 'char' type. We need to substract 48 to have its integer value because of the ASCII table.  
      
      for(int i=0; i<Q; i++)
      {
        digitalWrite(output,HIGH);
        delay(500);
        digitalWrite(output,LOW);
        delay(500);
      }
    }
  }
  else
  {
    Serial.println("E"); //If there's no power for the device, a signal is send for the program to quit working.
    delay(5000);
  }
}
