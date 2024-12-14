#include <LiquidCrystal.h>
//LCD pin to Arduino
const int pin_RS = 8; 
const int pin_EN = 9; 
const int pin_d4 = 4; 
const int pin_d5 = 5; 
const int pin_d6 = 6; 
const int pin_d7 = 7; 
int x;
//const int pin_BL = 10; 
int a;
int i=0;
int number;
int pres;
int numB;

LiquidCrystal lcd( pin_RS,  pin_EN,  pin_d4,  pin_d5,  pin_d6,  pin_d7);

void setup() {
  
  lcd.begin(16, 2);

  lcd.setCursor(5,0);
  Serial.begin(9600);
  Serial.setTimeout(2);
  lcd.print("Hello");
  delay(2000);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Welcome To Bank");
  delay(2000);
  lcd.clear();
  lcd.print("Number :");
  lcd.setCursor(0,1);
  lcd.print("Num :");
  lcd.setCursor(11,1);
  lcd.print("TO:");

  
}

void loop() {
  x = analogRead (0);
  if (x < 60 ) {
    number=number+1;
    delay(250);
    lcd.setCursor(11,0);
    lcd.print(number); 
  }
  else if (x < 200) {
    numB=numB+1;
    delay(250);
    lcd.setCursor(7,1);
    lcd.print(numB);
    lcd.setCursor(15,1);
    lcd.print ("1");
    Serial.print(numB);
    Serial.println(".1");
    
  }
  else if (x < 400){  
    numB=numB+1;
    delay(250);
    lcd.setCursor(7,1);
    lcd.print(numB);
    lcd.setCursor(15,1);
    lcd.print ("2");
    Serial.print(numB);
    Serial.println(".2");
    
  }
  else if (x < 600){
    numB=numB+1;
    delay(250);
    lcd.setCursor(7,1);
    lcd.print(numB);
    lcd.setCursor(15,1);
    lcd.print ("3");
    Serial.print(numB);
    Serial.println(".3");
    
  }
  else if (x < 800){
    numB=numB+1;
    delay(250);
    lcd.setCursor(7,1);
    lcd.print(numB);
    lcd.setCursor(15,1);
    lcd.print ("4");
    Serial.print(numB);
    Serial.println(".4");
    
  }
  Serial.print("0");
  Serial.println(".0");
  
}
